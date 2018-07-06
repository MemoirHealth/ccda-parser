#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 16:13:02 2018

@author: mansooralam, yanjingwang
"""



from bluebutton import core
from bluebutton.core import codes
from bluebutton import documents
from ...core import wrappers

def care_plan(ccda):

    data = []

    care_plan = ccda.section('care_plan')

    for entry in care_plan.entries():

        name = None
        code = None
        code_system = None
        code_system_name = None

        # Plan of care encounters, which have no other details
        el = entry.template('2.16.840.1.113883.10.20.22.4.40')
        if not el.is_empty():
            name = 'encounter'
        else:
            el = entry.tag('code')

            name = el.attr('displayName')
            code = el.attr('code')
            code_system = el.attr('codeSystem')
            code_system_name = el.attr('codeSystemName')

        text = core.strip_whitespace(entry.tag('text').val())

        data.append(
            wrappers.ObjectWrapper(
                text=text,
                name=name,
                code=code,
                code_system=code_system,
                code_system_name=code_system_name
                ))

    return wrappers.ListWrapper(data)