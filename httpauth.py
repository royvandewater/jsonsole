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
    connection = httplib.HTTPSConnection(server)
    connection.connect()
    connection.putrequest('GET', ensure_path(page))
    connection.putheader('Authorization', auth )
    connection.endheaders()
    return connection.getresponse()

def ensure_path(page):
    """
    Ensures that the path starts with a '/'
    """
    return page if page.startswith('/') else "/{0}".format(page)
