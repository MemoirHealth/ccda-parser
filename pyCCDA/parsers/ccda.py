#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 21:36:34 2018

@author: mansooralam, yanjingwang
"""

from ._ccda.allergies import allergies
from ._ccda.care_plan import care_plan
from ._ccda.demographics import demographics
from ._ccda.document import document
from ._ccda.encounters import encounters
from ._ccda.free_text import free_text
from ._ccda.functional_statuses import functional_statuses
from ._ccda.immunizations import immunizations
from ._ccda.instructions import instructions
from ._ccda.medications import medications
from ._ccda.problems import problems
from ._ccda.procedures import procedures
from ._ccda.results import results
from ._ccda.smoking_status import smoking_status
from ._ccda.vitals import vitals
from ..core import wrappers


def run(ccda):
    data = wrappers.ObjectWrapper()

    data.document = document(ccda)
    data.allergies = allergies(ccda)
    data.care_plan = care_plan(ccda)
    data.chief_complaint = free_text(ccda, 'chief_complaint')
    data.demographics = demographics(ccda)
    data.encounters = encounters(ccda)
    data.functional_statuses = functional_statuses(ccda)
    data.immunizations = immunizations(ccda).administered
    data.immunization_declines = immunizations(ccda).declined
    data.instructions = instructions(ccda)
    data.results = results(ccda)
    data.medications = medications(ccda)
    data.problems = problems(ccda)
    data.procedures = procedures(ccda)
    data.smoking_status = smoking_status(ccda)
    data.vitals = vitals(ccda)

    return data