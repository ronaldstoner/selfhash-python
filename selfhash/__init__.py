#!/usr/bin/python
# Hash: 62cf98a0590f5ddea116edc071cc70815397ba71d2ff25e30a814ec5598ee3fe

"""SelfHash __init__.py"""

import inspect

from .selfhash import SelfHash


def _get_caller_file():
    stack = inspect.stack()
    caller_frame = stack[-1]
    caller_file = caller_frame.filename
    return caller_file


# Automatically hash the caller
SelfHash().hash(_get_caller_file())
