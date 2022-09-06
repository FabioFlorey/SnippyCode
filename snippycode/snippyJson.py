# !./bin/python3
# *-* coding: utf-8 *-*
'''
SnippyJson
=============================================================================
:: Description
    short description
'''
from __future__ import annotations

from dataclasses import dataclass

from .snippyCopy import clipboard
from .snippyDocument import Document

@dataclass
class Json:
    '''
    '''
    prefix: str
    body: str
    description: str

    def __repr__(self) -> str:
        return str(self.content)
        
    @property
    def name(self):
        return f'Snippycode.{self.prefix}'

    @property
    def content(self):
        return {self.name:{'prefix' :self.prefix,
                           'body'   :self.body,
                           'description':self.description}}


@dataclass
class JsonFromClipboard(Json):
    '''
    '''
    body : str = clipboard()
    description: str = '# Snippy from `clipboard`.'

    def __post_init__(self):
        super().__init_subclass__()


@dataclass
class JsonFromDocument(Json):
    '''
    '''
    path : str

    def __post_init__(self):
        document = Document(self.path)
        self.body : str = document.body
        self.description: str = document.description
        super().__init_subclass__()

if __name__ == '__main__':
    pass