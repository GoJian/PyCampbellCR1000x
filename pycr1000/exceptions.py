# -*- coding: utf-8 -*-
'''
    pycr1000.exceptions
    -------------------

    Exceptions

    :copyright: Copyright 2012 Salem Harrache and contributors, see AUTHORS.
    :license: GNU GPL v3.

'''
from __future__ import division, unicode_literals


class NoDeviceException(Exception):
    '''Can not access to device.'''
    value = __doc__


class BadAckException(Exception):
    '''No valid acknowledgement.'''
    def __str__(self):
        return self.__doc__


class BadCRCException(Exception):
    '''No valid checksum.'''
    def __str__(self):
        return self.__doc__


class BadDataException(Exception):
    '''No valid data.'''
    def __str__(self):
        return self.__doc__