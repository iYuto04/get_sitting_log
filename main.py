from post_slack import Danpei
import datetime

def check_data():
    d = datetime.datetime.today()
    today = '{0}-{1}-{2}'.format(d.year, d.month, d.day)
if __name__ == '__main__':
    check_data()
