#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 16:50:25 2018

@author: mansooralam, yanjingwang
"""

from ...core import wrappers
from ... import core
from ... import documents


def document(ccda):

    parse_date = documents.parse_date
    parse_name = documents.parse_name
    parse_address = documents.parse_address

    doc = ccda.section('document')

    date = parse_date(doc.tag('effectiveTime').attr('value'))
    title = core.strip_whitespace(doc.tag('title').val())

    author = doc.tag('author')
    el = author.tag('assignedPerson').tag('name')
    name_dict = parse_name(el)

    el = author.tag('addr')
    address_dict = parse_address(el)

    el = author.tag('telecom')
    work_phone = el.attr('value')

    documentation_of_list = wrappers.ListWrapper()
    performers = doc.tag('documentationOf').els_by_tag('performer')

    for el in performers:
        performer_name_dict = parse_name(el)
        performer_phone = el.tag('telecom').attr('value')
        performer_addr = parse_address(el.tag('addr'))
        documentation_of_list.append(wrappers.ObjectWrapper(
            name=performer_name_dict,
            phone=wrappers.ObjectWrapper(
                work=performer_phone
            ),
            address=performer_addr
        ))

    el = doc.tag('encompassingEncounter').tag('location')
    location_name = core.strip_whitespace(el.tag('name').val())
    location_addr_dict = parse_address(el.tag('addr'))

    encounter_date = None
    el = el.tag('effectiveTime')
    if not el.is_empty():
        encounter_date = parse_date(el.attr('value'))

    data = wrappers.ObjectWrapper(
        date=date,
        title=title,
        author=wrappers.ObjectWrapper(
            name=name_dict,
            address=address_dict,
            phone=wrappers.ObjectWrapper(
                work=work_phone
            )
        ),
        documentation_of=documentation_of_list,
        location=wrappers.ObjectWrapper(
            name=location_name,
            address=location_addr_dict,
            encounter_date=encounter_date
        )
    )

    return data