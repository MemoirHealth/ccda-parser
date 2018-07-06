#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 21:55:35 2018

@author: mansooralam, yanjingwang
"""

from .. import documents


def process(ccda):
    """
    Preprocesses the CCDA docuemnt
    """
    ccda.section = section
    return ccda


def section(ccda, name):
    """
    Finds the section of a CCDA document
    """

    entries = documents.entries

    if 'document' == name:
        return ccda.template('2.16.840.1.113883.10.20.22.1.1')
    if 'allergies' == name:
        el = ccda.template('2.16.840.1.113883.10.20.22.2.6.1')
        el.entries = entries
        return el
    if 'care_plan' == name:
        el = ccda.template('2.16.840.1.113883.10.20.22.2.10')
        el.entries = entries
        return el
    if 'chief_complaint' == name:
        el = ccda.template('2.16.840.1.113883.10.20.22.2.13')
        if el.is_empty():
            el = ccda.template('1.3.6.1.4.1.19376.1.5.3.1.1.13.2.1')
        # no entries in Chief Complaint
        return el
    if 'demographics' == name:
        return ccda.template('2.16.840.1.113883.10.20.22.1.1')
    if 'encounters' == name:
        el = ccda.template('2.16.840.1.113883.10.20.22.2.22')
        if el.is_empty():
            el = ccda.template('2.16.840.1.113883.10.20.22.2.22.1')
        el.entries = entries
        return el
    if 'functional_statuses' == name:
        el = ccda.template('2.16.840.1.113883.10.20.22.2.14')
        el.entries = entries
        return el
    if 'immunizations' == name:
        el = ccda.template('2.16.840.1.113883.10.20.22.2.2.1')
        if el.is_empty():
            el = ccda.template('2.16.840.1.113883.10.20.22.2.2')
        el.entries = entries
        return el
    if 'instructions' == name:
        el = ccda.template('2.16.840.1.113883.10.20.22.2.45')
        el.entries = entries
        return el
    if 'results' == name:
        el = ccda.template('2.16.840.1.113883.10.20.22.2.3.1')
        if el.is_empty():
            el = ccda.template('2.16.840.1.113883.10.20.22.2.3')
        el.entries = entries
        return el
    if 'medications' == name:
        el = ccda.template('2.16.840.1.113883.10.20.22.2.1.1')
        el.entries = entries
        if el.is_empty():
            el = ccda.template('2.16.840.1.113883.10.20.22.2.1')
        return el
    if 'problems' == name:
        el = ccda.template('2.16.840.1.113883.10.20.22.2.5.1')
        if el.is_empty():
            el = ccda.template('2.16.840.1.113883.10.20.22.2.5')
        el.entries = entries
        return el
    if 'procedures' == name:
        el = ccda.template('2.16.840.1.113883.10.20.22.2.7.1')
        if el.is_empty():
            el = ccda.template('2.16.840.1.113883.10.20.22.2.7')
        el.entries = entries
        return el
    if 'social_history' == name:
        el = ccda.template('2.16.840.1.113883.10.20.22.2.17')
        el.entries = entries
        return el
    if 'vitals' == name:
        el = ccda.template('2.16.840.1.113883.10.20.22.2.4.1')
        if el.is_empty():
            el = ccda.template('2.16.840.1.113883.10.20.22.2.4')
        el.entries = entries
        return el

    return None