# !./bin/python3
# *-* coding: utf-8 *-*
'''
SnippyStatus
=============================================================================
:: Description
    short description
'''
from __future__ import annotations

from dataclasses import dataclass

@dataclass
class Status:
    '''
    Print a status message with different formats.
    '''
    message: str

    def fmt_print(self, format:str):
        message = '╍╍╍✂ ' + \
        '╌'*72+'\n' + \
        f'{self.message:^78s}'

        print(f'\033{format}{message}\033[0m')

    @property
    def bold(self):
        self.fmt_print('[1m')
        
    @property
    def success(self):
        self.fmt_print('[92m')

    @property
    def warning(self):
         self.fmt_print('[93m')

    @property
    def failed(self):
        self.fmt_print('[91m')

if __name__ == '__main__':
    pass