import requests
import multiprocessing 
from datetime import datetime
import time
from datetime import timedelta
import collections
import os

Social_endpoints = collections.namedtuple('Social_endpoints', [ 'endpoint_name','endpoint','execution_frequency_in_sec'])

# social_endpoints_data = (
#     Social_endpoints(endpoint_name='Instagram',endpoint='http://localhost:4001/cron-jobs/insta-hashtag-poll', execution_frequency_in_sec=3610),
#     Social_endpoints(endpoint_name='Facebook',endpoint='http://localhost:4001/cron-jobs/fb-poll', execution_frequency_in_sec=3610)
# )
mutex = 0

social_endpoints_data = (
    Social_endpoints(endpoint_name='insta_facebook',endpoint=['https://www.google.com', 'https://www.gmail.com'], execution_frequency_in_sec=10),
    # Social_endpoints(endpoint_name='youtube',endpoint=['https://www.youtube.com'], execution_frequency_in_sec=15),
    # Social_endpoints(endpoint_name='yahoo',endpoint=['https://www.yahoo.com'], execution_frequency_in_sec=15),

)


def transform(x):
    while True:
        if x.endpoint_name.lower() == 'insta_facebook':
            print(f"{os.getpid()} {x.endpoint[0]}")
            starttime = datetime.now()
            data = requests.get(x.endpoint[0])
            endtime = datetime.now()
            no_of_sec = (endtime-starttime).total_seconds()
            if no_of_sec <= x.execution_frequency_in_sec:
                print(f"{datetime.now()}-{x.endpoint_name} insta api executed before {x.execution_frequency_in_sec - no_of_sec} seconds...puting system in wait mode for {x.execution_frequency_in_sec - no_of_sec} seconds")
                time.sleep(x.execution_frequency_in_sec - no_of_sec)
            
            print(no_of_sec)

            print(f"{os.getpid()} {x.endpoint[1]}")
            starttime = datetime.now()
            data = requests.get(x.endpoint[1])
            endtime = datetime.now()
            no_of_sec = (endtime-starttime).total_seconds()
            if no_of_sec <= x.execution_frequency_in_sec:
                print(f"{datetime.now()}-{x.endpoint_name} facebook api executed before {x.execution_frequency_in_sec - no_of_sec} seconds...puting system in wait mode for {x.execution_frequency_in_sec - no_of_sec} seconds")
                time.sleep(x.execution_frequency_in_sec - no_of_sec)
            
            print(no_of_sec)
        else:    
            print(f"{os.getpid()} {x.endpoint[0]}")
            starttime = datetime.now()
            data = requests.get(x.endpoint[0])
            endtime = datetime.now()
            no_of_sec = (endtime-starttime).total_seconds()
            if no_of_sec <= x.execution_frequency_in_sec:
                print(f"{datetime.now()}-{x.endpoint_name} api executed before {x.execution_frequency_in_sec - no_of_sec} seconds...puting system in wait mode for {x.execution_frequency_in_sec - no_of_sec} seconds")
                time.sleep(x.execution_frequency_in_sec - no_of_sec)
            
            print(no_of_sec)
        # return data

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pool.map(transform,social_endpoints_data)
    