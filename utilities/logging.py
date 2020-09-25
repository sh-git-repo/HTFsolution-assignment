'''
'''
import json
from order_book.logging_utils import FetchLogger
from utilities import setup

CONFIG_PATH = setup.CONFIG_PATH

def display_logs(logger):
    '''
    '''
    for log_filename in logger.fetch_logs():
        with open(log_filename) as log_file:
            data = json.load(log_file)
        print(data['trade_type'], '-', data['id'])
        print('  ', data['quantity'], data['limit'], data['date'], '\n')

def logging(order_book):
    '''
    '''
    print('Warning, selecting any order to be cancelled will undo all the changes upto that order \n')
    logger = FetchLogger(CONFIG_PATH)
    display_logs(logger)
    option = int(input('Enter the order number to be undone \n'))
    status, bids, asks = logger.fetch_trades(option)
    if status:
        order_book.bids.pairs = bids
        order_book.asks.pairs = asks
