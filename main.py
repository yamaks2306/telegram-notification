import os
from message import Message
from environments import Environment

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
#GitHub environment variables
github_workflow = os.getenv('GITHUB_WORKFLOW')
github_repository = os.getenv('GITHUB_REPOSITORY')
github_sha = os.getenv('GITHUB_SHA')
github_actor = os.getenv('GITHUB_ACTOR')
tag = os.getenv('GITHUB_REF')

envs = Environment(
    chat_id,
    token,
    status,
    commit,
    include_commit_info,
    docker_tags,
    custom_message,
    github_workflow,
    github_repository,
    github_sha,
    github_actor,
    tag
)
message = Message(envs)

message.send_message()
