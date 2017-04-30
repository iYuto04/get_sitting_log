from get_data import sitting_time
from plot_graph import plot_week_log
from post_slack import post_graph

def main():
    data = sitting_time()
    plot_week_log(data)
    post_graph()

if __name__ == '__main__':
    main()