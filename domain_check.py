#!/usr/bin/python

from domainr import *
from time import sleep
import sys

# read strings in from stdin
# output available domains on stdout
# pauses between API calls with message to stderr
#
# usage: echo "pizza" | ./domain_check.py
#    or
#        ./examples/ambigrams.py | ./domain_check.py

pausetime = 10

for line in sys.stdin:
	domainname = line.strip()
	sys.stderr.write("checking "+domainname+"...\n")
	results_json = domainr_search_json(domainname)
	
	for name in results_json['results']:
		if (name['availability'] == 'available'):
			sys.stdout.write(name['domain']+'\n')
	sys.stderr.write( "sleeping " + str(pausetime) + " seconds...\n" )
	sleep(pausetime)
