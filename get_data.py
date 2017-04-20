import fitbit
from config import fitbit_cfg

def sitting_time():
    CLIENT_ID = fitbit_cfg['client_id']
    CLIENT_SECRET = fitbit_cfg['client_secret']
    ACCESS_TOKEN = fitbit_cfg['access_token']
    REFRESH_TOKEN = fitbit_cfg['refresh_token']
    authd_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET,
    access_token = ACCESS_TOKEN, refresh_token = REFRESH_TOKEN)
    rsp = authd_client.intraday_time_series('activities/minutesSedentary')
    return rsp['activities-minutesSedentary'][0]['value']

if __name__ == '__main__':
    print(sitting_time())
