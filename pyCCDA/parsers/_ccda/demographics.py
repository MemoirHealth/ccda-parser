#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 16:48:03 2018

@author: mansooralam, yanjingwang
"""

from bluebutton import core
from bluebutton.core import codes
from bluebutton import documents
from ...core import wrappers


def demographics(ccda):
    parse_date = documents.parse_date
    parse_name = documents.parse_name
    parse_address = documents.parse_address

    demographics = ccda.section('demographics')

    patient = demographics.tag('patientRole')
    el = patient.tag('patient').tag('name')
    patient_name_dict = parse_name(el)

    el = patient.tag('patient')
    dob = parse_date(el.tag('birthTime').attr('value'))
    gender = codes.gender(el.tag('administrativeGenderCode').attr('code'))
    marital_status = codes.marital_status(el.tag('maritalStatusCode').attr('code'))

    el = patient.tag('addr')
    patient_address_dict = parse_address(el)

    el = patient.tag('telecom')
    home = el.attr('value')
    work = None
    mobile = None

    email = None

    language = patient.tag('languageCommunication').tag('languageCode').attr('code')
    race = patient.tag('raceCode').attr('displayName')
    ethnicity = patient.tag('ethnicGroupCode').attr('displayName')
    religion = patient.tag('religiousAffiliationCode').attr('displayName')

    el = patient.tag('birthplace')
    birthplace_dict = parse_address(el)

    el = patient.tag('guardian')
    guardian_relationship = el.tag('code').attr('displayName')
    guardian_relationship_code = el.tag('code').attr('code')
    guardian_home = el.tag('telecom').attr('value')

    el = el.tag('guardianPerson').tag('name')
    guardian_name_dict = parse_name(el)

    el = patient.tag('guardian').tag('addr')
    guardian_address_dict = parse_address(el)

    el = patient.tag('providerOrganization')
    provider_organization = el.tag('name').val()
    provider_phone = el.tag('telecom').attr('value')

    provider_address_dict = parse_address(el.tag('addr'))

    return wrappers.ObjectWrapper(
        name=patient_name_dict,
        dob=dob,
        gender=gender,
        marital_status=marital_status,
        address=patient_address_dict,
        phone=wrappers.ObjectWrapper(
            home=home,
            work=work,
            mobile=mobile
        ),
        email=email,
        language=language,
        race=race,
        ethnicity=ethnicity,
        religion=religion,
        birthplace=wrappers.ObjectWrapper(
            state=birthplace_dict.state,
            zip=birthplace_dict.zip,
            country=birthplace_dict.country
        ),
        guardian=wrappers.ObjectWrapper(
            name=wrappers.ObjectWrapper(
                given=guardian_name_dict.given,
                family=guardian_name_dict.family
            ),
            relationship=guardian_relationship,
            relationship_code=guardian_relationship_code,
            address=guardian_address_dict,
            phone=wrappers.ObjectWrapper(
                home=guardian_home
            )
        ),
        provider=wrappers.ObjectWrapper(
            organization=provider_organization,
            phone=provider_phone,
            address=provider_address_dict
        )
    )
