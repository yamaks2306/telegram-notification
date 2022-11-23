import os
from message import Message
from environments import Environment

chat_id = os.getenv('CHAT_ID')
if chat_id == "" or chat_id is None:
    raise SystemExit('Variable chat_id is required. Exit.')
token = os.getenv('TOKEN')
if token == "" or token is None:
    raise SystemExit('Variable token is required. Exit.')
status = os.getenv('STATUS')
commit = os.getenv('COMMIT_MESSAGE')
include_commit_info = os.getenv('INCLUDE_COMMIT_INFO')
docker_tags = os.getenv('DOCKER_TAGS')
custom_message = os.getenv('MESSAGE')
#GitHub environment variables
github_workflow = os.getenv('WORKFLOW')
github_repository = os.getenv('REPOSITORY')
github_sha = os.getenv('SHA')
github_actor = os.getenv('ACTOR')
tag = os.getenv('TAG')

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
