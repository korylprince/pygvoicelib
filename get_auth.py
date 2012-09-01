#!/usr/bin/python
import pygvoicelib
username = raw_input('username:')
apppass = raw_input('application password:')
client = pygvoicelib.GoogleVoice(username,apppass)
client.validate_credentials()
print "\nusername:"
print username
print "\napplication password:"
print apppass
print "\nauth_token:"
print client.auth_token
print "\nrnr_se:"
print client.rnr_se
print '\n'
