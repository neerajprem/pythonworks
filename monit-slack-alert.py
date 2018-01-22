#!/usr/bin/env python
## Author - Neeraj Prem Verma
import sys
import json
import requests

SlackWebHookUrl = 'https://hooks.slack.com/services/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'
SlackChannelName = '#serveralerts'
SlackUserDisplayName = 'Monit'
SlackEmojiCode = ':sos:'

def SlackNotif(ServiceName, ServiceMessage):
    PostData = "Alert : "+ServiceName+" : "+ServiceMessage
    slack_data = {'text': PostData ,"channel": SlackChannelName ,"username": SlackUserDisplayName , "icon_emoji": SlackEmojiCode }
    response = requests.post(SlackWebHookUrl, data=json.dumps(slack_data),headers={'Content-Type': 'application/json'})
    if response.status_code != 200:
       raise ValueError('Slack Error Code : %s \nError Detail -\n%s' %(response.status_code, response.text))

SlackNotif(sys.argv[1], sys.argv[2])
