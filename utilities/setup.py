'''
'''
import json
from order_book import TradeObject, OrderBook

CONFIG_PATH = 'order_book/logging_utils/backup_files/' 

def setup():
    '''
    '''
    with open('demo.json') as json_data:
        data = json.load(json_data)

    bids = TradeObject(data['bids'])
    asks = TradeObject(data['asks'], 'asks')

    order_book = OrderBook(bids, asks)
    return order_book