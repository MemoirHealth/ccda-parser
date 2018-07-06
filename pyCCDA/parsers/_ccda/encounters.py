#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 21:17:08 2018

@author: mansooralam, yanjingwang
"""

"""
Parser for the CCDA encounters section
"""

from ...core import wrappers
from ...documents import parse_address, parse_date


def encounters(ccda):

    data = []
    
    encounters = ccda.section('encounters')

    for entry in encounters.entries():

        date = parse_date(entry.tag('effectiveTime').attr('value'))

        el = entry.tag('code')
        name = el.attr('displayName')
        code = el.attr('code')
        code_system = el.attr('codeSystem')
        code_system_name = el.attr('codeSystemName')
        code_system_version = el.attr('codeSystemVersion')
        
        # translation
        el = entry.tag('translation')
        translation_name = el.attr('displayName')
        translation_code = el.attr('code')
        translation_code_system = el.attr('codeSystem')
        translation_code_system_name = el.attr('codeSystemName')
        
        # performer
        el = entry.tag('performer').tag('code')
        performer_name = el.attr('displayName')
        performer_code = el.attr('code')
        performer_code_system = el.attr('codeSystem')
        performer_code_system_name = el.attr('codeSystemName')
      
        # participant => location
        el = entry.tag('participant')
        organization = el.tag('code').attr('displayName')
        
        location_dict = parse_address(el)
        location_dict.organization = organization
    
        # findings
        findings = []
        findings_els = entry.els_by_tag('entryRelationship')
        for current in findings_els:
            el = current.tag('value')
            findings.append(wrappers.ObjectWrapper(
                name=el.attr('displayName'),
                code=el.attr('code'),
                code_system=el.attr('codeSystem'),
            ))

        data.append(wrappers.ObjectWrapper(
            date=date,
            name=name,
            code=code,
            code_system=code_system,
            code_system_name=code_system_name,
            code_system_version=code_system_version,
            findings=findings,
            translation=wrappers.ObjectWrapper(
                name=translation_name,
                code=translation_code,
                code_system=translation_code_system,
                code_system_name=translation_code_system_name
            ),
            performer=wrappers.ObjectWrapper(
                name=performer_name,
                code=performer_code,
                code_system=performer_code_system,
                code_system_name=performer_code_system_name
            ),
            location=location_dict
        ))

    return wrappers.ListWrapper(data)