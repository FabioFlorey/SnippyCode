# !./bin/python3
# *-* coding: utf-8 *-*
'''
                                     SETUP
===============================================================================
                               Short Description.
-------------------------------------------------------------------------------

:Description:
   ...

:Usage:
    ...

:Authors:
    Fabio Craig Wimmer Florey

:Version:
    0.0.1-dev

'''
from __future__ import annotations

from dataclasses import dataclass
from os.path import abspath, dirname, exists, join
from pkg_resources import get_distribution, DistributionNotFound
from subprocess import check_call
from sys import executable

from setuptools import find_packages, setup

ENCODING = ("encoding", "utf8")

# NOTE :: Custom Classes and Functions.

@dataclass
class Status:
    '''
    Print a status message with different formats.
    '''
    message: str

    def fmt_print(self, format:str):
        print(f'\033{format}{self.message}\033[0m')

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


@staticmethod
def checkAndGetTwine():
    '''
    - Check if `twine` is installed;
    - Collect `twine`, if it is not;
    '''
    try:
        get_distribution('twine')
        Status('`twine` is installed.').success
    except DistributionNotFound:
        Status('`twine` is not installed.').warning
        check_call([executable, '-m', 'pip', 'install', 'twine'])

def read(*args, **kwargs) -> str:
    with open(join(dirname(__file__), *args), 
         encoding=kwargs.get(*ENCODING)) as fp:
        return fp.read()

def readlines(*args, **kwargs) -> list[str]:
    with open(join(dirname(__file__), *args), 
         encoding=kwargs.get(*ENCODING)) as fp:
        return fp.readlines()

# NOTE :: Get current working directory.

cwd : str = dirname(abspath(__file__))

# NOTE :: Create Essential Files and Installing Essential Packages.

MANIFEST_FNAME : str = 'MANIFEST.ini'
README_FNAME   : str = 'README.md'
LICENSE_FNAME  : str = 'LICENSE.md'
INIT_FNAME     : str = 'snippycode/__init__.py'
VERSION_FNAME  : str = '__version__.py'

if not exists(manifest_path := join(cwd, MANIFEST_FNAME)):
    Status(f'`{MANIFEST_FNAME}` needed to import `{README_FNAME}`.').warning
    with open(manifest_path, 'w', encoding=ENCODING[1]) as manifest:
        print(f'Writing a new `{MANIFEST_FNAME}`.')
        manifest.write(f'include {README_FNAME} {LICENSE_FNAME} requirements.txt\n')
        Status(f'New `{MANIFEST_FNAME}` created.').success

if not exists(init_path := join(cwd, INIT_FNAME)):
    with open(init_path, 'w', encoding=ENCODING[1]) as init:
        init.write(f'')

# NOTE :: Package Medatada.

NAME             : str = 'SnippyCode'
FULLNAME         : str = 'SnippyCode'
VERSION          : str = '0.1.6b0'
DESCRIPTION      : str = 'A command line extension to add snippets directly in Visual Studio Code.'
try:
    long_description : str = read(cwd, README_FNAME)
except FileNotFoundError:
    long_description : str = DESCRIPTION
URL              : str = 'https://github.com/FabioFlorey/SnippyCode'
DOWNLOAD_URL     : str = 'https://pypi.org/project/snippycode/'
KEYWORDS         : list[str] = [
                                'CLI','Command Line Interface',
                                'VSCode', 'Visual Studio Code',
                                'Snippets',
                                'Python 3.9', 'Python 3.10'
                                ]
try:
    license : str = read(cwd, LICENSE_FNAME)
except FileNotFoundError:
    Status(f'`{LICENSE_FNAME}` not found.').failed
    license : str = 'GPL-v3'
    Status(f'Package license will be updated to `{license}`.').warning
    Status(f'Consider adding a `{LICENSE_FNAME}` to your repo!').warning
AUTHOR           : str = 'Fabio Craig Wimmer Florey'
AUTHOR_EMAIL     : str = 'fabioflorey@icloud.com'
MAINTAINER       : str = ''
MAINTAINER_EMAIL : str = ''

# NOTE :: Package Informations.

PYTHON_REQUIRES = '>=3.9.0'

PACKAGES : list[str] = find_packages()
CLASSIFIERS : list[str] = [
                          'Development Status :: 4 - Beta',
                          'Environment :: Console',
                          'Environment :: Win32 (MS Windows)',
                          'Intended Audience :: Developers',
                          'Intended Audience :: End Users/Desktop',
                          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                          'Operating System :: Microsoft :: Windows',
                          'Programming Language :: Python',
                          'Programming Language :: Python :: 3 :: Only',
                          'Topic :: Software Development',
                          'Topic :: Terminals',
                          'Topic :: Utilities'
                         ]

# NOTE :: How to run the script from the CLI.

SNIPPYCODE = 'snippycode.snippyCode'
ENTRYPOINTS : dict[str,
              list[str]] = {
                            'console_scripts': [f'snip={SNIPPYCODE}:write',
                                                f'snip-up={SNIPPYCODE}:update',
                                                f'snip-rm={SNIPPYCODE}:delete',
                                                f'snip-ls={SNIPPYCODE}:list'],
                           }

if __name__ == '__main__':
    setup(
            name=NAME, fullname=FULLNAME, version=VERSION,
            description=DESCRIPTION, long_description=long_description,
            long_description_content_type='text/markdown',
            url=URL, download_url=DOWNLOAD_URL,
            keywords=KEYWORDS, classifiers=CLASSIFIERS,
            license=license,

            author=AUTHOR, author_email=AUTHOR_EMAIL,
            maintainer=MAINTAINER, maintainer_email=MAINTAINER_EMAIL,

            python_requires=PYTHON_REQUIRES,
            packages=PACKAGES,
            entry_points=ENTRYPOINTS
            
         )