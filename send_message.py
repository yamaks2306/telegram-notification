import os
import requests

chat_id = os.getenv('INPUT_CHAT_ID')
if chat_id == "":
    raise SystemExit('Variable chat_id is required. Exit.')
token = os.getenv('INPUT_TOKEN')
if token == "":
    raise SystemExit('Variable chat_id is required. Exit.')
status = os.getenv('INPUT_STATUS')
commit = os.getenv('INPUT_COMMIT_MESSAGE')
include_commit_info = os.getenv('INPUT_INCLUDE_COMMIT_INFO')
docker_tags = os.getenv('INPUT_DOCKER_TAGS')
custom_message = os.getenv('INPUT_MESSAGE')


link=f'https://api.telegram.org/bot{token}/sendMessage'

icon = {
    "failure":   "🔴",
	  "cancelled": "⚪",
	  "success":   "🟢",
}

#GitHub environment variables
github_workflow = os.getenv('GITHUB_WORKFLOW')
github_repository = os.getenv('GITHUB_REPOSITORY')
github_sha = os.getenv('GITHUB_SHA')
github_actor = os.getenv('GITHUB_ACTOR')
tag = os.getenv('GITHUB_REF')

commit_link = f'https://github.com/{github_repository}/commit/{github_sha}'

def get_version(tag_string):
    '''GITHUB_REF contain "refs/tags/v0.0.2" or "refs/heads/main". If second part is "tags",
    return tag with version number, else - None'''
    tags = tag_string.split("/")
    return tags[2] if tags[1] == "tags" else None

def build_message():
    '''Building message from different parts'''
    message = f'''{icon[status]} {status}: <b>{github_workflow}</b>\n
      Repository: <b>{github_repository}</b>'''
    
    version = get_version(tag)
    if version is not None:
        message = f'''{message}
      Version: <b>{version}</b>'''
    
    if docker_tags != "":
        message = f'''{message}
      Docker image tags: <b>{docker_tags}</b>'''
    
    if include_commit_info == "true":
        message = f'''{message}
      Author: <b>{github_actor}</b>
      Commit message: <b>{commit}</b>
      <a href="{commit_link}">See changes</a>'''
            
    return message

def send_message():
    '''Sending message to telegram chat'''
    message = build_message() if custom_message == "" else custom_message
    parameters = {
    'chat_id': chat_id,
    'text': message,
    'parse_mode': 'HTML',
    'disable_web_page_preview': True
    }
    
    request = requests.get(link, params = parameters)
    request.raise_for_status()

send_message()
