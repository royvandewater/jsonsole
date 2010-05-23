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

    server   = config["connection"]["server"]
    username = config["connection"]["username"]
    password = config["connection"]["password"]

    while True:
        page = raw_input(">>>")
        response = httpauth.get_https_response(server,page,username,password)

        json_response = response.read()
        remote_data = json.loads(json_response)

        print( json.dumps(remote_data,indent=4) )

if __name__=="__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print()
        sys.exit(0)
