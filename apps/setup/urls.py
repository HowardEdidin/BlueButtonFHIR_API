#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

"""
BlueButtonFHIR_API
FILE: urls
Created: 3/8/16 1:42 AM


"""
__author__ = 'Mark Scrimshire:@ekivemark'

from django.conf.urls import patterns, url
from apps.setup.views import getpatient, geteob, user_list

urlpatterns = [
                       url(r'^getpatient/$',
                           getpatient,
                           name='getpatient'),

                       url(r'^geteob/$',
                           geteob,
                           name='geteob'),

                       url(r'^userlist/(?P<fmt>\w+|)$',
                           user_list,
                           name='userlist'),

]