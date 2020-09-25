'''
NAME:
    test.py
'''
from .display import ConsoleDisplay
from order_book.logging_utils import JsonLogger

class TradeObject():
    '''
    '''
    def __init__(self, pairs, trade_type='bids'):
        self.pairs = pairs
        self.trade_type = trade_type

class OrderBook():
    '''
    '''
    def __init__(self, bids, asks, commodity_name='stocks'):
        self.bids = bids
        self.asks = asks
        self.commodity_name = commodity_name

    def display_book(self, display=ConsoleDisplay):
        '''
        '''
        trade_objects = (self.asks, self.bids)
        for trade_object in trade_objects:
            display(trade_object).display()

    def buy(self, quantity):
        '''
        buy for cheap
        '''
        data = self.asks.pairs
        while quantity and data:
            cheapest_commodity = min(data)
            if cheapest_commodity[1] <= quantity:
                quantity -= cheapest_commodity[1]
                data.remove(cheapest_commodity)
            else:
                cheapest_commodity[1] = cheapest_commodity[1] - quantity
                quantity = 0

    def sell(self, quantity):
        '''
        '''
        data = self.bids.pairs
        while quantity and data:
            expensive_commodity = max(data)
            if expensive_commodity[1] <= quantity:
                quantity -= expensive_commodity[1]
                data.remove(expensive_commodity)
            else:
                expensive_commodity[1] = expensive_commodity[1] - quantity
                quantity = 0

    def buy_limit(self, quantity, limit):
        '''
        '''
        bids_data = self.bids.pairs
        asks_data = self.asks.pairs
        if limit >= min(asks_data)[0]:
            self.buy(quantity)
        elif lis := [pos for pos, pair in enumerate(bids_data) if pair[0]==limit]:
            pos = lis[0]
            bids_data[pos][1] += quantity
        else:
            bids_data.insert(0, [limit, quantity])

    def sell_limit(self, quantity, limit):
        '''
        '''
        bids_data = self.bids.pairs
        asks_data = self.asks.pairs
        if limit <= max(bids_data)[0]:
            self.sell(quantity)
        elif lis := [pos for pos, pair in enumerate(asks_data) if pair[0]==limit]:
            pos = lis[0]
            asks_data[pos][1] += quantity
        else:
            asks_data.append([limit, quantity])


if __name__ == "__main__":
    pass