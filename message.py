import requests
import constant
import environments

class Message:
    '''A class that builds and sends messages'''
    def __init__(self, envs: environments.Environment):
        self.envs = envs

    def __build_message(self):
        '''Building message from different parts'''
        message = f'''{constant.ICON[self.envs.status]} {self.envs.status}: <b>{self.envs.github_workflow}</b>\n
          Repository: <b>{self.envs.github_repository}</b>'''
        
        version = self.envs.get_version()
        if version is not None:
            message = f'''{message}
          Version: <b>{version}</b>'''
        
        if self.envs.docker_tags is not None:
            message = f'''{message}
          Docker image tags: <b>{self.envs.docker_tags}</b>'''
        
        if self.envs.include_commit_info == "true":
            message = f'''{message}
          Author: <b>{self.envs.github_actor}</b>
          Commit message: <b>{self.envs.commit}</b>
          <a href="{self.envs.get_commit_link()}">See changes</a>'''
                
        return message

    def send_message(self):
        '''Sending message to telegram chat'''
        message = self.__build_message() if self.envs.custom_message is None else self.envs.custom_message
        parameters = {
        'chat_id': self.envs.chat_id,
        'text': message,
        'parse_mode': 'HTML',
        'disable_web_page_preview': True
        }
        
        request = requests.get(self.envs.get_link(), params = parameters)
        request.raise_for_status()
