#!/usr/bin/env python
import os
import sys
import urllib2
from mechanize import Browser

#variable for dealing with browser
br = Browser()

os.chdir('..')
os.chdir('motion/')
os.system('"motion"')
print "motion started!!"
#req = urllib2.Request('http://localhost:8081','<Request></Request>')
#page = br.open('http://localhost:8081')
