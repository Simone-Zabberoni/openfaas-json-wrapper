#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
entrypoint.py : JSON I/O wrapper for Openfaas

- read from stdin
- customize internals (or uncomment one of the samples)
- return json output

"""

import json
import sys

### Json input from STDIN
jsonInput = json.load(sys.stdin)
jsonOutput = {}


### DoStuff - customize here or uncomment one of the samples

## Just echo input back
"""
jsonOutput = jsonInput
"""
#-----------------------------------------------------

## Extract only some fields from the input
"""
data = []
for item in jsonInput:
    data.append( { 'name': item['name'], 'username': item['username']  }  )
jsonOutput = data
"""
#-----------------------------------------------------

## Sample dns resolver - little to none error checking
#
# Expects input like:
#    {
#        "query": "somedomain.com",
#        "recordtype": "MX"
#    }
# OR
#    {
#        "query": "FQDN.somedomain.com",
#        "recordtype": "CNAME"
#    }
#
# Requires dnspython (pip install dnspython)
"""
import dns.resolver
rrset = []

try:
    answer = dns.resolver.query(jsonInput['query'], jsonInput['recordtype'])
    for rdata in answer.rrset:
        rrset.append ( { 'response': rdata.to_text() } )
    jsonOutput = { 'status': 'OK', 'response_set': rrset  }

except:
    status = 'ERR'
    jsonOutput = { 'status': 'ERR', 'response_set': rrset  }
"""
#-----------------------------------------------------

## wc word counting - no input checking
#
# Expects input like:
#    {
#        "text": "some random text"
#    }
# Json couldn't be multiline, so only words and chars are meaningful

"""
import os
(rows, words, chars) = os.popen('echo \"' + jsonInput['text']  + '\" | wc ').read().split()

jsonOutput = { 'rows': rows, 
    'words': words,
    'chars': chars  }
"""
#-----------------------------------------------------


### Return json response
print ( json.dumps(jsonOutput, indent=4, separators=(',', ': ')) )
