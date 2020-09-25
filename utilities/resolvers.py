'''
'''
from order_book.logging_utils import JsonLogger
from utilities import setup

CONFIG_PATH = setup.CONFIG_PATH

def market_orders(order_book):
    '''
    '''
    logger = JsonLogger(CONFIG_PATH)
    option_string = ''.join([
        '1 for Market Buy\n',
        '2 for Market Sell\n'
    ])
    option = int(input(option_string))
    if option == 1:
        quantity = float(input('Enter quantity\n'))
        logger.save(order_book, 'Market Buy', quantity)
        order_book.buy(quantity)
    elif option == 2:
        quantity = float(input('Enter quantity\n'))
        logger.save(order_book, 'Market Sell', quantity)
        order_book.sell(quantity)

def limit_orders(order_book):
    '''
    '''
    logger = JsonLogger(CONFIG_PATH)
    option_string = ''.join([
        '1 for Limit Buy\n',
        '2 for Limit Sell\n'
    ])
    option = int(input(option_string))
    if option == 1:
        quantity, limit = tuple(map(float, input('Enter quantity, limit\n').split()))
        logger.save(order_book, 'Limit Buy', quantity, limit)
        order_book.buy_limit(quantity, limit)
    elif option == 2:
        quantity, limit = tuple(map(float, input('Enter quantity, limit\n').split()))
        logger.save(order_book, 'Limit Sell', quantity, limit)
        order_book.sell_limit(quantity, limit)
