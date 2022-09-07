# !./bin/python3
# *-* coding: utf-8 *-*
'''
SnippyFile
=============================================================================
:: Description
    short description
'''

from __future__ import annotations

from json import loads, dumps
from os import getenv
from os.path import join, exists

from snippycode.snippyJson import Json, JsonFromDocument, JsonFromClipboard

ENCODING: str = "utf-8"
HELLO   : dict = {"Snippycode":{
                        "prefix":"Hello!",
                        "body":"# Thank you for downloading SnippyCode!",
                        "description":"Welcome to SnippyCode!" }}
PATH = join(getenv('appdata'), 'Code/User/snippets/python.json' )


class File:
    '''
    '''
    def __init__(self) -> None:
        self.path = PATH
        if not(exists(self.path) and self.read()):
            self.write(HELLO, False)

    def __repr__(self) -> str:
        return str(self.keys)

    @property
    def keys(self) -> list:
        return [*self.read().keys()]

    def read(self) -> dict[dict[str]]:
        with open(self.path, mode='r',
                  encoding=ENCODING) as file:
            content = file.read()
        return loads(content) if content else dict()
        
    def update(self, name:str, body:str) -> None:
        reader = self.read()
        reader[name] |= {'body':body}
        self.write(reader, False)

    def write(self, content={}, read_flag=True) -> None:
        reader = self.read() if read_flag else content
        with open(self.path, mode='w',
                  encoding=ENCODING) as file:
            file.write(dumps(reader | content,
                             indent=4))

    def delete(self, name) -> None:
        reader: dict = self.read()
        del reader[name]
        self.write(reader, False)


class SnippetFile():
    '''
    '''
    def __init__(self, json: Json) -> None:
        self.file = File()
        self.json = json
        
    def update(self) -> None:
        self.file.update(self.json.name,
                    self.json.body)

    def write(self) -> None:
        self.file.write(self.json.content)

    def delete(self) -> None:
        self.file.delete(self.json.name)


class SnippetFromDocument(SnippetFile):
    '''
    '''
    def __init__(self, prefix: str, path: str) -> None:
        self.json = JsonFromDocument(prefix, None, None, path)
        super().__init__(self.json)


class SnippetFromClipboard(SnippetFile):
    '''
    '''
    def __init__(self, prefix: str) -> None:
        self.json = JsonFromClipboard(prefix)
        super().__init__(self.json)

if __name__ == '__main__':
    pass
