#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 21:23:37 2018

@author: mansooralam, yanjingwang
"""

"""
Parser for any freetext section (i.e., contains just a single <text> element)
"""
from ... import core
from ccda.core import wrappers


def free_text(ccda, section_name):

    doc = ccda.section(section_name)
    text = core.strip_whitespace(doc.tag('text').val())

    return wrappers.ObjectWrapper(
        text=text
    )