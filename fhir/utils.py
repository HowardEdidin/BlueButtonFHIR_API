#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

import json

from collections import OrderedDict
from django.http import HttpResponse

def kickout_301(reason, status_code=301):
    response= OrderedDict()
    response["code"] = status_code
    response["errors"] = [reason,]
    return HttpResponse(json.dumps(response, indent = 4),
                        status=status_code,
                        content_type="application/json")



def kickout_400(reason, status_code=400):
    response= OrderedDict()
    response["code"] = status_code
    response["errors"] = [reason,]
    return HttpResponse(json.dumps(response, indent = 4),
                        status=status_code,     
                        content_type="application/json")


def kickout_401(reason, status_code=401):
    response= OrderedDict()
    response["code"] = status_code
    response["errors"] = [reason,]
    return HttpResponse(json.dumps(response, indent = 4),
                        status=status_code,     
                        content_type="application/json")


def kickout_403(reason, status_code=403):
    response= OrderedDict()
    response["code"] = status_code
    response["errors"] = [reason,]
    return HttpResponse(json.dumps(response, indent = 4),
                        status=status_code,
                        content_type="application/json")


def kickout_404(reason, status_code=404):
    response= OrderedDict()
    response["code"] = status_code
    response["errors"] = [reason,]
    return HttpResponse(json.dumps(response, indent = 4),
                        status=status_code, 
                        content_type="application/json")


def kickout_500(reason, status_code=500):
    response= OrderedDict()
    response["code"] = status_code
    response["errors"] = [reason,]
    return HttpResponse(json.dumps(response, indent = 4),
                        status=status_code, 
                        content_type="application/json")


def kickout_502(reason, status_code=502):
    response= OrderedDict()
    response["code"] = status_code
    response["errors"] = [reason,]
    return HttpResponse(json.dumps(response, indent = 4),
                        status=status_code,
                        content_type="application/json")


def kickout_504(reason, status_code=504):
    response= OrderedDict()
    response["code"] = status_code
    response["errors"] = [reason,]
    return HttpResponse(json.dumps(response, indent = 4),
                        status=status_code,
                        content_type="application/json")