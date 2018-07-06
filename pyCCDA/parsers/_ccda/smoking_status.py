#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 21:32:38 2018

@author: mansooralam, yanjingwang
"""

"""
Parser for the CCDA smoking status in social history section
"""

from ...core import wrappers
from ... import documents


def smoking_status(ccda):

    parse_date = documents.parse_date

    name = None
    code = None
    code_system = None
    code_system_name = None
    entry_date = None

    # We can parse all of the social_history sections
    # but in practice, this section seems to be used for
    # smoking status, so we're just going to break that out.
    # And we're just looking for the first non-empty one.
    social_history = ccda.section('social_history')
    entries = social_history.entries()
    for entry in entries:

        smoking_status_ = entry.template('2.16.840.1.113883.10.20.22.4.78')
        if smoking_status_.is_empty():
            smoking_status_ = entry.template('2.16.840.1.113883.10.22.4.78')

        if smoking_status_.is_empty():
            continue

        el = smoking_status_.tag('effectiveTime')
        entry_date = parse_date(el.attr('value'))

        el = smoking_status_.tag('value')
        name = el.attr('displayName')
        code = el.attr('code')
        code_system = el.attr('codeSystem')
        code_system_name = el.attr('codeSystemName')

        if name:
            break

    data = wrappers.ObjectWrapper(
        date=entry_date,
        name=name,
        code=code,
        code_system=code_system,
        code_system_name=code_system_name
    )

    return data