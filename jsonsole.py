#!/usr/bin/env python
import os
import sys
import json
import httplib

import httpauth

def main(argv):
    """ Main method of application """
    config_file = file("config.json")
    config = json.loads(config_file.read())

    connection = config["connection"]
    server   = connection["server"]
    username = connection["username"]
    password = connection["password"]
    ssl = True if connection["ssl"].lower() == "true" else False

    http = httpauth.HttpAuth(server, ssl, username, password)

    while True:
        page = raw_input(">>>")
        response = http.get_https_response(page)

        json_response = response.read()
        remote_data = json.loads(json_response)

        print( json.dumps(remote_data,indent=4) )

if __name__=="__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print("")
        sys.exit(0)
