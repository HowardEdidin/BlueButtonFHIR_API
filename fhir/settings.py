#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

"""
BlueButtonFHIR_API
FILE: django-fhir.settings
Created: 1/9/16 11:58 AM


Create settings that can be overriden with an alternative package

"""
import os
from django.conf import settings

from importlib import import_module

__author__ = 'Mark Scrimshire:@ekivemark'


# You can override this default by replicating DJANGO_FHIR_CONFIG in your apps
# settings.py. The only restriction is to create your pluggable replacement for
# fhir_io_mongo as a top level module in your application.
# We also encourage you to follow the fhir_io_{backend_name} convention
# The pluggable backend should replicate all of the functions included in the default
# fhir_io_mongo or fhir_io_hapi pluggable modules.

DJANGO_FHIR_CONFIG = {
    "DF_APPS": ('fhir_io_mongo',),
    "DF_EXTRA_INFO": False,
}
# We should revamp DJANGO_FHIR_CONFIG to add reference for each FHIR call.
# ie. SEARCH, DELETE etc.


DJANGO_FHIR_CONFIG.update(getattr(settings, 'DJANGO_FHIR_CONFIG', {}))
if settings.DEBUG:
    print("DJANGO_FHIR_CONFIG:", DJANGO_FHIR_CONFIG)

DF_EXTRA_INFO = DJANGO_FHIR_CONFIG['DF_EXTRA_INFO']
if settings.DEBUG:
    print("DF_EXTRA_INFO:", DF_EXTRA_INFO)

for df_app in DJANGO_FHIR_CONFIG['DF_APPS']:
    if settings.DEBUG:
        print("Module:",df_app)

    # Build a series of Variables that specify the module that will contain a function
    # This is then used in the core FHIR module to call a pluggable routine
    # This is an early implementation. I expect to move the major call entrypoints to
    # values in the DJANGO_FHIR_CONFIG dict.
    # Here is an example to use read inside the views.get module
    # return FHIR_BACKEND_VIEW.read(request, resource_type, id)

    FHIR_BACKEND = import_module(df_app)
    FHIR_BACKEND_VIEW = import_module(df_app+".views.get")
    FHIR_BACKEND_FIND = import_module(df_app+".views.search")
    FHIR_BACKEND_DELETE = import_module(df_app+".views.delete")


    if settings.DEBUG:
        print("django-FHIR Pluggable Module:", FHIR_BACKEND)

    if df_app not in settings.INSTALLED_APPS:
        if settings.DEBUG:
            print("Adding %s to INSTALLED_APPS" % df_app)
        settings.INSTALLED_APPS += (df_app, )

    if settings.DEBUG:

        print("FHIR_BACKEND_VIEW:", FHIR_BACKEND_VIEW)
        print("FHIR_BACKEND_FIND:", FHIR_BACKEND_FIND)
        print("FHIR_BACKEND_DELETE:", FHIR_BACKEND_DELETE)


        my_method = getattr(FHIR_BACKEND_VIEW,'hello_world') #\("search", "Patient", "1")
        result = my_method("search", "Patient", "1")
        print("")
        print("Testing Pluggable Module %s via hello world:" % FHIR_BACKEND)
        print("Answer from Hello World:", result)
