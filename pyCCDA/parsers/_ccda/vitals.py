#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 21:33:17 2018

@author: mansooralam, yanjingwang
"""

"""
Parser for the CCDA vitals section
"""

from ...core import wrappers
from ... import documents


def vitals(ccda):

    parse_date = documents.parse_date
    data = wrappers.ListWrapper()

    vitals = ccda.section('vitals')

    for entry in vitals.entries():

        el = entry.tag('effectiveTime')
        entry_date = parse_date(el.attr('value'))

        results = entry.els_by_tag('component')
        results_data = wrappers.ListWrapper()

        for result in results:

            el = result.tag('code')
            name = el.attr('displayName')
            code = el.attr('code')
            code_system = el.attr('codeSystem')
            code_system_name = el.attr('codeSystemName')

            el = result.tag('value')
            value = wrappers.parse_number(el.attr('value'))
            unit = el.attr('unit')

            results_data.append(wrappers.ObjectWrapper(
                name=name,
                code=code,
                code_system=code_system,
                code_system_name=code_system_name,
                value=value,
                unit=unit
            ))

        data.append(wrappers.ObjectWrapper(
            date=entry_date,
            results=results_data
        ))

    return data