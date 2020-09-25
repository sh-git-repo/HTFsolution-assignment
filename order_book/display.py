'''
NAME:
    utilities.py
'''
from datetime import datetime

class Display():
    '''
    '''
    def __init__(self, trade_object):
        self.trade_object = trade_object

class ConsoleDisplay(Display):
    '''
    '''
    def display(self):
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(self.trade_object.trade_type.upper())
        print('-'*40)
        print('Prize', '   ', 'Size', '\n')
        for price, size in self.trade_object.pairs:
            print(price, '  :  ', size)
        print('-'*40)
        print('-'*40)
        print()