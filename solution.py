'''
NAME:
    solution.py

DESCRIPTION:
    Highly simplistic solution for the assignment
    by HTFsolution.
'''
import json
import time
import os
from utilities import resolvers, setup, logging

def resolve(option, order_book):
    '''
    Chooses the appropriate function based
    on the user's option.
    '''
    if option not in (1, 2, 3):
        return False
    elif option == 1:
        resolvers.market_orders(order_book)
    elif option == 2:
        resolvers.limit_orders(order_book)
    else:
        logging.logging(order_book)
    return True

def main():
    '''
    The main function of the solution,
    this solution mimics the style of
    '5-minute-finance' explanation for
    the limit order books.
    '''
    order_book = setup.setup()
    condition = True
    while condition:
        order_book.display_book()
        option_string = ''.join([
            'Enter 1 for Market orders \n',
            'Enter 2 for Limit orders \n',
            'Enter 3 to cancel a particular order\n',
            'Enter any other number to exit\n>> '
        ])
        condition = resolve(int(input(option_string)), order_book)
        os.system('cls')
    setup.reset()


if __name__ == "__main__":
    main()