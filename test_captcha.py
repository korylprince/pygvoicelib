#!/usr/bin/python
import sys
import pygvoicelib
try:
    input = raw_input
except NameError:
    input = input

def handle_captcha(voice):
    voice.passwd = passwd
    print 'Captcha URL is: %s\n' % (voice.captcha_url)
    print 'Enter captcha value: '
    voice.captcha_entry = input()

def run_test(user, passwd)
    print 'We will try random wrong passwords to get a captcha lock ...'
    voice = pygvoicelib.GoogleVoice(user, passwd)
    voice.handle_captcha_entry = handle_captcha

    for i in range(50):
        print 'Wrong password - try %d' % (i)
        voice.passwd = str(i+111111)
        try:
            voice.validate_credentials()
        except pygvoicelib.LoginError, e:
            if e.reason != 'failed':
                raise
        if voice.auth_token:
            break

    try:
        ret = voice.get_numbers()
        ret1 = voice.call('1222333444', '15556667777')
        ret2 = voice.cancel()
        print 'Test OK - We succeeded to login'
    except:
        print 'Test FAILED - We failed to login'

if __name__ == '__main__':
    print 'Please enter your Google Username:',
    user = input()
    print 'Please enter your Password:',
    passwd = input()
    print 'Please enter a number to call:',
    call_number = input()

    run_test(user, passwd)
