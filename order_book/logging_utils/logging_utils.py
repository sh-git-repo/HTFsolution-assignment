'''
'''
import json
import os
from datetime import datetime

class Logger():
    '''
    '''
    def __init__(self, config_path=''):
        self.config_path = config_path

class JsonLogger(Logger):
    '''
    '''
    def _get_version(self):
        '''
        '''
        full_path = ''.join([
            self.config_path,
            '/config_file.txt'
        ])
        with open(full_path, 'r+') as config_file:
            version = int(config_file.read()) + 1
            config_file.seek(0)
            # if version > 19:
            #     config_file.write(0)
            config_file.write(str(version))
        return version

    def save(self, book, trade_type, quantity, limit=None):
        '''
        '''
        version = self._get_version()
        full_path = ''.join([
            self.config_path,
            '/backup_json_',
            str(version),
            '.json'
        ])

        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        json_compatible_book = {
            'trade_type': trade_type,
            'id': version,
            'date': date,
            'quantity': quantity,
            'limit': limit,
            'bids': book.bids.pairs,
            'asks': book.asks.pairs
        }
        with open(full_path, 'w') as json_file:
            json.dump(json_compatible_book, json_file, indent=2)

class FetchLogger(Logger):
    '''
    '''
    def fetch_logs(self):
        '''
        '''
        return get_filenames(self.config_path, 'json')

    def fetch_trades(self, config_version):
        '''
        '''
        file_name = ''.join([
            self.config_path,
            'backup_json_',
            str(config_version),
            '.json'
        ])
        try:
            with open(file_name) as json_file:
                data = json.load(json_file)
            return True, data['bids'], data['asks']
        except FileNotFoundError:
            return False, None, None

def get_filenames(path, extension):
    '''
    '''
    extension_len = len(extension)
    file_path_generator = (
        ''.join([path, file_name])\
        for file_name in os.listdir(path)\
        if file_name[-extension_len:] == extension
    )
    return file_path_generator