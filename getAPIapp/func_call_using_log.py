# -*- coding: utf-8 -*-
'''
 to practice POC of logging tool at 10:00 
 on @2020.2.27 - Noon, by @Queenie
'''

import os, sys, re, logging, itertools
import requests
import pandas as pd
#from flaskTool import flaskInstance

#from urllib.parse import urlparse

#logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
#logging.getLogger("process_name").setLevel(logging.ERROR)

def parser(query_name='poupou'):

    print('Get API')
    #logging.info('Get API for {topic} at timing on {date}'.format(topic=query_name, date=pd.Timestamp.date()))

    try:
        res_info = requests_connect_to(query_name)
        print(res_info.url, res_info.status_code)
        return res_info.status_code, res_info.url

    except Exception as e:
        print(e)
        #@ Log Msg - info
        #logging.warning('Cannot get {n} into from internet for {date}'.format(n=query_name, date=pd.Timestamp.now()))

def modifier(name='poupou', query_date=pd.Timestamp.now()):
    
    print('modifier process')
    #@ Log Msg - info
    #logging.info('Modify Table for {topic} at timing on {date}'.format(topic=name, date=query_date.date()))


def parse_tabel(query_date=pd.Timestamp.now()):

    print('table parsing process')
    
    #@ Log Msg - debug
    #logging.debug('file is decrypted, get raw data.')
                          
    #for txt in re.split('\n\n', text):
        #record = re.split('[\x0c\n]', txt)
        #record = list(filter(table_header_name, record))
                            
    list_df = []
    df = pd.DataFrame([])
    #df = pd.DataFrame(np.array(list(filter(header_bndcrvpx, l)), dtype=object).reshape(-1,7),
    #columns=[' ', ' ', ' ', ' ', ' ', ' ', ' '])
    df['timestamp'] = query_date.date # using pandas timestamp tool
    list_df.append(df)
                                    
    new_df = pd.concat(list_df, axis=0).sort_values(by=['']) 

    #@ Log Msg - warn
    #logging.warning('Cannot get cells or rows info on at timeing on { }'.format(query_date.date()))
    return new_df

def requests_connect_to(name):
    
    icat_link = 'https://icatcare.org/'
    python_link = 'https://docs.python.org/3/library/logging.html'
    google_link = 'https://www.google.com.tw/'
    
    if name == 'poupou' or 'POUPOU' or 'PouPou' or 'Poupou':

        link = icat_link
        res = requests.get(link)
        return res

    elif name == "python" or "PYTHON" or "Python" or "PYTHON":

        link = python_link
        res = requests.get(link)
        return res

    else:
         
         link = google_link
         res = requests.get(link)
         return res

if __name__ == "__main__":

    insert_name = 'poupou'
    parser(insert_name)
    # pandas using its function called option_context()
    #with pd.option_context('display.max_rows', None, 'display.max_columns', 10):
    #name = 'poupou'