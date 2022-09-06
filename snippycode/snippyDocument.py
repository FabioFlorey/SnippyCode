# !./bin/python3
# *-* coding: utf-8 *-*
'''
SnippyDocument
=============================================================================
:: Description
    short description
'''
from __future__ import annotations

from ast import get_docstring, parse
from dataclasses import dataclass
from os.path import basename

@dataclass
class Document:
    path : str

    def __post_init__(self):
        self.read()

    def read(self) -> str:
        with open(self.path, mode='r',
                    encoding='utf-8') as file:
            self.body = file.read()

    @property
    def file(self) -> str:
        return basename(self.path)

    @property
    def description(self) -> str:
        description = get_docstring(parse(self.body))
        return (description 
                if description
                else f"# Snippy from `{self.file}`.")

if __name__ == '__main__':
    pass