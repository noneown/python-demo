from nose.tools import *

from apply.http_request import test_request

from apply.pthread import test

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"
    test_request()
