from nose.tools import *

from apply.apply.pthread import test

from apply.apply.http_request import test_request

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"
    test_request()
