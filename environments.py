class Environment:
    '''Class containing all the necessary variables for building and sending notification'''
    def __init__(
        self,
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
        ):
        self.chat_id = chat_id
        self.token = token
        self.status = status
        self.commit = self.__fix_commit_message(commit)
        self.include_commit_info = include_commit_info
        self.docker_tags = docker_tags
        self.custom_message = custom_message
        self.github_workflow = github_workflow
        self.github_repository = github_repository
        self.github_sha = github_sha
        self.github_actor = github_actor
        self.tag = tag

    def get_link(self):
        '''Get link for sending message'''
        return f'https://api.telegram.org/bot{self.token}/sendMessage'
    def get_commit_link(self):
        '''Get link to commit'''
        return f'https://github.com/{self.github_repository}/commit/{self.github_sha}'
    def __fix_commit_message(self, message):
        '''Replacing unsupported characters'''
        replace_dict = {'<':'(', '>':')', '\n':'\n        '}
        result = ''.join(i if i not in replace_dict else replace_dict[i] for i in message)
        return result
    def get_version(self):
        '''GITHUB_REF contain "refs/tags/v0.0.2" or "refs/heads/main". If second part is "tags",
        return tag with version number, else - None'''
        tags = self.tag.split("/")
        return tags[2] if tags[1] == "tags" else None
