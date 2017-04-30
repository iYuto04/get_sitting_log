import matplotlib.pyplot as plt
import datetime

week_name = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def plot_week_log(data):
    # x = [(datetime.date.today() - datetime.timedelta(days=(6 - date))).weekday() for date in range(7)]
    x = [0,1,2,3,4,5,6]
    plt.bar(x,data)
    plt.savefig('sitting_log.png')


if __name__ == '__main__':
    data = [848, 741, 737, 755, 756, 856, 768]
    plot_week_log(data)