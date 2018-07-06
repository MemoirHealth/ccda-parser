#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 15:51:50 2018

@author: mansooralam, yanjingwang
"""

"""
Parser for the CCDA allergies section
"""
from ...documents import parse_date
from ...core import wrappers
from ... import core


def allergies(ccda):

    data = []

    allergies = ccda.section('allergies')

    for entry in allergies.entries():

        el = entry.tag('effectiveTime')
        start_date = parse_date(el.tag('low').attr('value'))
        end_date = parse_date(el.tag('high').attr('value'))

        el = entry.template('2.16.840.1.113883.10.20.22.4.7').tag('code')
        name = el.attr('displayName')
        code = el.attr('code')
        code_system = el.attr('codeSystem')
        code_system_name = el.attr('codeSystemName')

        # value => reaction_type
        el = entry.template('2.16.840.1.113883.10.20.22.4.7').tag('value')
        reaction_type_name = el.attr('displayName')
        reaction_type_code = el.attr('code')
        reaction_type_code_system = el.attr('codeSystem')
        reaction_type_code_system_name = el.attr('codeSystemName')

        # reaction
        el = entry.template('2.16.840.1.113883.10.20.22.4.9').tag('value')
        reaction_name = el.attr('displayName')
        reaction_code = el.attr('code')
        reaction_code_system = el.attr('codeSystem')

        # severity
        el = entry.template('2.16.840.1.113883.10.20.22.4.8').tag('value')
        severity = el.attr('displayName')

        # participant => allergen
        el = entry.tag('participant').tag('code')
        allergen_name = el.attr('displayName')
        allergen_code = el.attr('code')
        allergen_code_system = el.attr('codeSystem')
        allergen_code_system_name = el.attr('codeSystemName')

        # this is not a valid place to store the allergen name but some vendors
        # use it
        if not allergen_name:
            el = entry.tag('participant').tag('name')
            if not el.is_empty():
                allergen_name = el.val()

        if not allergen_name:
            el = entry.template('2.16.840.1.113883.10.20.22.4.7').tag('originalText')
            if not el.is_empty():
                allergen_name = core.strip_whitespace(el.val())

        # status
        el = entry.template('2.16.840.1.113883.10.20.22.4.28').tag('value')
        status = el.attr('displayName')

        data.append(wrappers.ObjectWrapper(
            date_range=wrappers.ObjectWrapper(
                start=start_date,
                end=end_date
            ),
            name=name,
            code=code,
            code_system=code_system,
            code_system_name=code_system_name,
            status=status,
            severity=severity,
            reaction=wrappers.ObjectWrapper(
                name=reaction_name,
                code=reaction_code,
                code_system=reaction_code_system
            ),
            reaction_type=wrappers.ObjectWrapper(
                name=reaction_type_name,
                code=reaction_type_code,
                code_system=reaction_type_code_system,
                code_system_name=reaction_type_code_system_name
            ),
            allergen=wrappers.ObjectWrapper(
                name=allergen_name,
                code=allergen_code,
                code_system=allergen_code_system,
                code_system_name=allergen_code_system_name
            )
        ))

    return wrappers.ListWrapper(data)