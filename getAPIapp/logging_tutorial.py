# 0220.2/25. 13:00, created by Queenie
# 0220.2/27. 09:00, modified by Queenie
# url : https://docs.python.org/3/library/logging.html
# event logging for app 
# app log can include msg from 3rd party modules

# Track Event & Monitor Investigation & Raise Exception
# add log call to code to indicate certain events have occured.
# and ass Level & Severity let us subscribes to.

import logging, re, sys

# lambda
# row_to_dic = lambda row: { col.name: str(getattr(row, col.name)) for col in row.__table__.columns} if row else {}

# init the logging
filename = r'C:\Users\109009\Desktop\logging\LogFile\file.txt'

# param : stram, level, format
# logging.basicConfig(filename=filename)
# logging.getlogger('Name').setLevel(Level_Nmae)
##logging.getLogger('Function Called').setLevel(logging.DEBUG)
##format_setting = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
# logging.basicConfig(filename=filename)
##logging.basicConfig(stream=sys.stdout, level=logging.Info, format=format_setting)

# logger shall never be intantiated directly,
# alway thru the module-level func called logging.getlogger()
# Multi calls to get() with same name will return a ref to the same

##logging.info('hi i am going now...')

def set_log_config():

    # global||static variable, not local variable
    # just wanna doing decouple & modulization
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    logging.getLogger("process_name").setLevel(logging.ERROR)

def test_result():

    a = 'haha' # immutable
    b = ['', '', ''] # mutable
    c = b.append(a)
    d = 'egg, luv,  , cloud' 
    print(a, b, c)
    e = d.split(',')
    f = d.split()
    print(e)
    print(f)
    # logging.info('process completed')

if __name__ == '__main__':
    set_log_config()
    test_result()

# string format
# % syntax in old python version
# code example: '% 12s'

# :> syntax in new python version
# code example: '{:>12}'

# alternative
# using rjust() method called

# to make the info in cell aligned
# line can be delimited by calling stringvaribale.split() 
