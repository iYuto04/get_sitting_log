import fitbit
# from config import fitbit_cfg
import sys, os
import datetime
sys.path.append(os.getcwd() + '/python-fitbit/')
import gather_keys_oauth2


def sitting_time():
    fitbit_cfg = gather_keys_oauth2.write_config_file()
    CLIENT_ID = fitbit_cfg['client_id']
    CLIENT_SECRET = fitbit_cfg['client_secret']
    ACCESS_TOKEN = fitbit_cfg['access_token']
    REFRESH_TOKEN = fitbit_cfg['refresh_token']
    authd_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET,
    access_token = ACCESS_TOKEN, refresh_token = REFRESH_TOKEN)
    yesterday = datetime.date.today() + datetime.timedelta(days=-1)
    week_ago = yesterday + datetime.timedelta(days=-6)
    rsp = authd_client.time_series('activities/minutesSedentary',base_date=week_ago,end_date=yesterday)
    return [int(data['value']) for data in rsp['activities-minutesSedentary']]

if __name__ == '__main__':
    print(sitting_time())
