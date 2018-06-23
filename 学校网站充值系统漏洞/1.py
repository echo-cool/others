#!/usr/bin/env python
"""
Copyright (c) 2006-2017 sqlmap developers (http://sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""
import requests
from lib.core.enums import PRIORITY
from random import sample
__priority__ = PRIORITY.NORMAL
def dependencies():
    pass
def new_cookie():
    session = requests.Session()
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36","Connection":"close","Accept-Language":"en-US,en;q=0.5","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Upgrade-Insecure-Requests":"1"}
    response = session.get("http://targetwebapp/", headers=headers)
    XSRF_TOKEN = response.headers['Set-Cookie'].split(';')[0]
    SESSION = response.headers['Set-Cookie'].split(';')[3].split(',')[1].replace(" ", "")
    return "Cookie: {0}; {1}".format(XSRF_TOKEN, SESSION)
def tamper(payload, **kwargs):
    headers = kwargs.get("headers", {})
    headers["Cookie"] = new_cookie()
    return payload
