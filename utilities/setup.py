'''
'''
import os
import json
from order_book import TradeObject, OrderBook
from order_book.logging_utils import get_filenames

CONFIG_PATH = 'order_book/logging_utils/backup_files/' 

def setup(json_file='demo.json'):
    '''
    '''
    with open(json_file) as json_data:
        data = json.load(json_data)

    bids = TradeObject(data['bids'])
    asks = TradeObject(data['asks'], 'asks')

    order_book = OrderBook(bids, asks)
    return order_book

def reset():
    '''
    '''
    config_file_path = ''.join([
        CONFIG_PATH,
        'config_file.txt'
    ])
    with open(config_file_path, 'w') as config_file:
        config_file.write('0')

    for json_filename in get_filenames(CONFIG_PATH, 'json'):
        os.remove(json_filename)