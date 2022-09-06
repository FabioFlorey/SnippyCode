# !./bin/python3
# *-* coding: utf-8 *-*
'''
SnippyCode

:: Description
    A command line extension to add snippets directly in Visual Studio Code.

:: Copyright
    SnippyCode, Copyright (C) 2022, Fabio Craig Wimmer Florey 
    All Rights Reserved.
'''
from __future__ import annotations

from argparse import ArgumentParser

from .snippyFile import SnippetFromDocument, SnippetFromClipboard
from .snippyStatus import Status


parser = ArgumentParser(description = __doc__)

parser.add_argument('name', 
                    help  = 'Name that you will type into vscode.',
                    nargs = '?')
parser.add_argument('path', 
                    help  = 'Path of the file you want to snip.',
                    nargs = '?') 

arguments = parser.parse_args()

json = (SnippetFromDocument(arguments.name, arguments.path) 
            if arguments.path else
            SnippetFromClipboard(arguments.name))

def list():
    Status(f'You have the following snippets:').bold
    for snippet in json.keys:
        print(snippet)

def write():
    try:
        json.write()
        Status(f'Successfully added `{json.json.prefix}` to your snippets!').success
    except Exception:
        Status(Exception).failed

def update():
    try:
        json.update()
        Status(f'Successfully updated `{json.json.prefix}` in your snippets!').success
    except Exception:
        Status(Exception).failed

def delete():
    try:
        json.delete()
        Status(f'Successfully deleted `{json.json.prefix}` from your snippets!').success
    except Exception:
        Status(Exception).failed

if __name__ == '__main__':
    pass