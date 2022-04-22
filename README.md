# telegram-notification
Notification to Telegram chat about GitHub Action workflow status with customizable messages

## Usage
To be notified in the Telegram chat about the results of a wokflow, add the next step to the end of your wokflow:
```yaml
- name: Send message
        uses: yamaks2306/telegram-notification@main
        if: always()
        with:
          chat_id: ${{ secrets.TG_CHAT_ID }}
          token: ${{ secrets.TG_TOKEN }}
```
Where ```chat_id``` is the chat ID and ```token``` is the token of the telegram bot

You can specify additional parameters to customize the messages:
- ```include_commit_info``` - string "true" or "false" ("true" by default). If true, message to Telegram will contain information about commit - author, commit message and link to commit page.
- ```commit_message``` - the default setting is ```github.event.head_commit.message```. ```github.event.commits[0].message``` can be used instead. In the first case, if there were several commits, the message of the last commit will be displayed, in the second - the first one.
- ```docker_tags``` - if the previous step was to build docker images, you can specify docker tags, for example ```steps.docker_meta.outputs.tags```
- ```message``` - custom message, if specified, will be used instead of the standard message.