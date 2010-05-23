#!/usr/bin/env python
import base64
import string
import httplib

class HttpAuth:
    """
    Class to interact with an https service that may or may not
    require authentication
    """
    def __init__(self, server, ssl=True, username=None, password=None):
        """
        If username and password are not provided, https request
        will not send authentication headers
        """
        self.server   = server

        authstring = 'Basic ' + string.strip(base64.encodestring(username + ':' + password))
        self.auth  = authstring if username and password else None

        self.connection_method = httplib.HTTPSConnection if ssl else httplib.HTTPConnection

    def get_https_response(self, page):
        """
        "Basic" authentication encodes userid:password in base64. Note
        that base64.encodestring adds some extra newlines/carriage-returns
        to the end of the result. string.strip is a simple way to remove
        these characters.
        """

        # h = httplib.HTTP(server)
        connection = self.connection_method(self.server)
        connection.connect()
        connection.putrequest('GET', self.ensure_path(page))
        if self.auth:
            connection.putheader('Authorization', self.auth )
        connection.endheaders()
        return connection.getresponse()

    def ensure_path(self, page):
        """
        Ensures that the path starts with a '/'
        """
        return page if page.startswith('/') else "/{0}".format(page)
