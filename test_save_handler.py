#!/usr/bin/python
import sys
import pygvoicelib
try:
    input = raw_input
except NameError:
    input = input

save_loc = None

def handle_captcha(voice):
    voice.passwd = passwd
    print 'Captcha URL is: %s\n' % (voice.captcha_url)
    print 'Enter captcha value: '
    voice.captcha_entry = input()

def handle_save_token(voice):
    global save_loc
    print 'Saving Credentials ...'
    save_loc = voice.get_state()

def run_test(uesr, passwd)
    voice = pygvoicelib.GoogleVoice(user, passwd)
    voice.handle_captcha_entry = handle_captcha
    voice.handle_save_token = handle_save_token

    try:
        ret = voice.get_numbers()
        ret2 = voice.cancel()
        print 'Test 1 OK - We succeeded to login'
    except pygvoicelib.LoginError, e:
        if e.reason == 'failed':
            print 'Test 1 FAILED - We failed to login (Wrong passwod)'
        elif e.reason == 'captcha':
            print 'Test 1 FAILED - We failed to login (Captcha locked)'
        else:
            print 'Test 1 FAILED - Unknown Error'
    except:
        print 'Test 1 FAILED - Unknown Error'

    if not save_loc:
        print 'Test 2 FAILED - Token not saved'
    else:
        voice2 = pygvoicelib.GoogleVoice(*save_loc)
        try:
            ret = voice2.get_numbers()
            ret2 = voice2.cancel()
            print 'Test 2 OK - The state was loaded properly'
        except Exception, e:
            print e.reason
            print 'Test 2 FAILED - The state was not loaded properly'

if __name__ == '__main__':
    print 'Please enter your Google Username:',
    user = input()
    print 'Please enter your Password:',
    passwd = input()

    run_test(user, passwd)
