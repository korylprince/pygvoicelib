#!/usr/bin/python
import pygvoicelib
username = raw_input('username:')
apppass = raw_input('application password:')
client = pygvoicelib.GoogleVoice(username,apppass)
client.validate_credentials()
print """
import pygvoicelib                                                                                                                          
username="{0}"
apppass="{1}"
auth_token="{2}"
rnr_se="{3}"
client = pygvoicelib.GoogleVoice(username,apppass,auth_token,rnr_se)
#replace number with phone number below
#client.sms(number,"test")
""".format(username,apppass,client.auth_token,client.rnr_se)
