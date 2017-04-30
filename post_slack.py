import os
from slacker import Slacker
from config import slack_token

def post_graph():
    token = slack_token
    channel_name = 'sitting_log'
    file_path = os.getcwd() + '/sitting_log.png'
    slacker = Slacker(token)
    slacker.files.upload(file_path,channels=[channel_name], title='1週間のデータです')

if __name__ == '__main__':
    post_graph()
