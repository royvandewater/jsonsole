#!/usr/bin/env python
import base64
import string
import httplib

def get_https_response(server,page,username,password):
    """
    "Basic" authentication encodes userid:password in base64. Note
    that base64.encodestring adds some extra newlines/carriage-returns
    to the end of the result. string.strip is a simple way to remove
    these characters.
    """
    auth = 'Basic ' + string.strip(base64.encodestring(username + ':' + password))

    # h = httplib.HTTP(server)
    h = httplib.HTTPSConnection(server)
    h.connect()
    h.putrequest('GET', page)
    h.putheader('Authorization', auth )
    h.endheaders()
    return h.getresponse()
