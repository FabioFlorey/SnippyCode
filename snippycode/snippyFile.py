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

from .snippyJson import Json, JsonFromDocument, JsonFromClipboard

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
        if not(exists(self.path) 
               and self.read()):
            self.write(HELLO)

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
        
    def update(self, name, body) -> None:
        file: dict = self.read()
        file[name] |= {'body':body}
        self.write(file)

    def write(self, content= {}) -> None:
        old_content = self.read()
        with open(self.path, mode='w',
                  encoding=ENCODING) as file:
            file.write(dumps(old_content |
                             content,
                             indent=4))

    def delete(self, name) -> None:
        file: dict = self.read()
        del file[name]
        self.write(file)


class SnippetFile(File):
    '''
    '''
    def __init__(self, json: Json) -> None:
        self.json = json
        super().__init__()

    def __repr__(self) -> str:
        return super().__repr__()

    def update(self) -> None:
        return super().update(self.json.name, self.json.body)

    def write(self) -> None:
        return super().write(self.json.content)

    def delete(self) -> None:
        return super().delete(self.json.name)


class SnippetFromDocument(SnippetFile):
    '''
    '''
    def __init__(self, prefix: str, path: str) -> None:
        json = JsonFromDocument(prefix, None, None, path)
        super().__init__(json)


class SnippetFromClipboard(SnippetFile):
    '''
    '''
    def __init__(self, prefix: str) -> None:
        json = JsonFromClipboard(prefix)
        super().__init__(json)


if __name__ == '__main__':
    pass