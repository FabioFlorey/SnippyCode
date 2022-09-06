# !./bin/python3
# *-* coding: utf-8 *-*
'''
SnippyCopy
=============================================================================
:: Description
    short description
'''

from __future__ import annotations

import ctypes

def clipboard() -> str:
    '''

    '''    
    lib  : ctypes.LibraryLoader = ctypes.windll
    void : ctypes.c_void_p = ctypes.c_void_p
    
    kernel_lock   = lib.kernel32.GlobalLock
    kernel_unlock = lib.kernel32.GlobalUnlock

    kernel_lock.argtypes = [void]
    kernel_lock.restype = void
    kernel_unlock.argtypes = [void]

    user = lib.user32
    clipboardData = user.GetClipboardData
    clipboardData.restype = void
    user.OpenClipboard(0)
    
    try:
        if user.IsClipboardFormatAvailable(1):
            data = clipboardData(1)
            data_locked = kernel_lock(data)
            text = ctypes.c_char_p(data_locked)
            value = text.value
            kernel_unlock(data_locked)
            return value.decode('utf-8')
    finally:
            user.CloseClipboard()

if __name__ == '__main__':
    pass