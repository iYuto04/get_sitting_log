import slackweb
from config import slack_cfg

def Danpei():
    slack = slackweb.Slack(url = slack_cfg['url'])
    slack.notify(text="立て...立つんだYuto!")
