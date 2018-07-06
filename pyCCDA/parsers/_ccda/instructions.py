#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 21:27:36 2018

@author: mansooralam, yanjingwang
"""

"""
Parser for the CCDA "plan of care" section
"""
from ...core import wrappers
from ... import core


def instructions(ccda):

    data = wrappers.ListWrapper()

    instructions = ccda.section('instructions')

    for entry in instructions.entries():

        el = entry.tag('code')
        name = el.attr('displayName')
        code = el.attr('code')
        code_system = el.attr('codeSystem')
        code_system_name = el.attr('codeSystemName')

        text = core.strip_whitespace(entry.tag('text').val())

        data.append(wrappers.ObjectWrapper(
            text=text,
            name=name,
            code=code,
            code_system=code_system,
            code_system_name=code_system_name
        ))

    return data