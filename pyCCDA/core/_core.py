#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 21:43:56 2018

@author: mansooralam, yanjingwang
"""

def strip_whitespace(text):
    """ Remove leading and trailing whitespace from a string """
    if not isinstance(text, basestring):
        return text
    return text.strip()