import requests
import multiprocessing 
from datetime import datetime
import time
from datetime import timedelta
import collections
import os

import sys
import logging


Social_endpoints = collections.namedtuple('Social_endpoints', [ 'endpoint_name','endpoint','logfile','execution_frequency_in_sec'])

# social_endpoints_data = (
#     Social_endpoints(endpoint_name='insta_facebook',endpoint=['https://www.google.com', 'https://www.gmail.com'], logfile='insta-facebook.log', execution_frequency_in_sec=10),
#     Social_endpoints(endpoint_name='yahoo',endpoint=['https://www.yahoo.com'], logfile='pintrest.log', execution_frequency_in_sec=15)
# )

social_endpoints_data = (
    Social_endpoints(endpoint_name='insta_facebook',endpoint=['http://localhost:4001/cron-jobs/insta-hashtag-poll', 'http://localhost:4001/cron-jobs/fb-poll'], logfile='insta-facebook.log', execution_frequency_in_sec=3610),
    Social_endpoints(endpoint_name='youtube_delete',endpoint=['http://localhost:4001/cron-jobs/youtube-delete'], logfile='youtube-delete.log', execution_frequency_in_sec=86400),
    Social_endpoints(endpoint_name='youtube',endpoint=['http://localhost:4001/cron-jobs/youtube-poll'], logfile='youtube.log', execution_frequency_in_sec=3610),
    Social_endpoints(endpoint_name='Blogs and Forums',endpoint=['http://localhost:4001/cron-jobs/blog-forum-poll'], logfile='blogs-forums.log', execution_frequency_in_sec=86400),
    Social_endpoints(endpoint_name='Pintrest',endpoint=['http://localhost:4001/cron-jobs/pinterest-poll'], logfile='pintrest.log', execution_frequency_in_sec=86400)
)

def transform(x):
    while True:
        try:
            logging.basicConfig(filename=x.logfile, level=logging.INFO)
            if x.endpoint_name.lower() == 'insta_facebook':
                
                starttime = datetime.now()
                log_text = f"start time = {starttime} process id ={os.getpid()} endpoint={x.endpoint[0]}"
                data = requests.get(x.endpoint[0])
                
                # print(f'mapping topics for instragram feeds {data}')
                data1 = requests.get('http://localhost:4001/cron-jobs/topic-feed-map')
                endtime = datetime.now()
                no_of_sec = (endtime-starttime).total_seconds()
                log_text = log_text + f" end_time = {endtime} execution time = {no_of_sec} seconds"
                
                if no_of_sec <= x.execution_frequency_in_sec:
                    log_text = log_text + f" instagram api executed before {x.execution_frequency_in_sec - no_of_sec} seconds...puting system in wait mode for {x.execution_frequency_in_sec} seconds"
                    logging.info(log_text)
                    time.sleep(x.execution_frequency_in_sec)
                else:
                    log_text = log_text + f" instagram api execution time = {no_of_sec}"
                    logging.warning(log_text)
                    time.sleep(x.execution_frequency_in_sec)

                starttime = datetime.now()
                log_text = f"start time = {starttime} process id ={os.getpid()} endpoint={x.endpoint[1]}"
                data = requests.get(x.endpoint[1])
                endtime = datetime.now()
                no_of_sec = (endtime-starttime).total_seconds()
                log_text = log_text + f" end_time = {endtime} execution time = {no_of_sec} seconds"
                
                if no_of_sec <= x.execution_frequency_in_sec:
                    log_text = log_text + f" facebook api executed before {x.execution_frequency_in_sec - no_of_sec} seconds...puting system in wait mode for {x.execution_frequency_in_sec} seconds"
                    logging.info(log_text)
                    time.sleep(x.execution_frequency_in_sec)
                else:
                    log_text = log_text + f" facebook api execution time = {no_of_sec}"
                    logging.warning(log_text)
                    time.sleep(x.execution_frequency_in_sec)
                
            else:    
                
                starttime = datetime.now()
                log_text = f"start time = {starttime} process id ={os.getpid()} endpoint={x.endpoint[0]}"
                data = requests.get(x.endpoint[0])
                endtime = datetime.now()
                no_of_sec = (endtime-starttime).total_seconds()
                log_text = log_text + f" end_time = {endtime} execution time = {no_of_sec} seconds"

                if no_of_sec <= x.execution_frequency_in_sec:
                    log_text = log_text + f" api executed before {x.execution_frequency_in_sec - no_of_sec} seconds...puting system in wait mode for {x.execution_frequency_in_sec - no_of_sec} seconds"
                    logging.info(log_text)
                    time.sleep(x.execution_frequency_in_sec - no_of_sec)
                else:
                    log_text = log_text + f" api execution time = {no_of_sec}"
                    logging.warning(log_text)
        except Exception as e:
            logging.warning(f'[{datetime.now()}]:exception occured while hitting endpoint {x.endpoint_name} putting process in sleep mode for {x.execution_frequency_in_sec} sec...{e}')
            time.sleep(x.execution_frequency_in_sec)
            

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pool.map(transform,social_endpoints_data)
    