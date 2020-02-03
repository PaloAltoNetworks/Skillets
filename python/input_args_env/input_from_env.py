#!/usr/bin/env python3
#
# This example uses ENV variables to gather input from the user
# The .meta-cnc file defines 4 input variables:
# USERNAME, PASSWORD, SECRET, WISHLIST
# This script shows how to obtain the values entered from the user
#
import os

print('*'*80)
print('This is an example python script. All stdout will be returned to the user')
print('\n')
print('The user has entered 3 values from the Panhandler UI')

# this example uses the 'get' method to ensure we get the 'default' value in case it doesn't exist
username = os.environ.get('USERNAME', 'default')
password = os.environ.get('PASSWORD', 'password')
secret = os.environ.get('SECRET', 'secret')
wishlist = os.environ.get('WISHLIST', '')

print(f'The entered username is: {username}')
print(f'The entered secret has a length of {len(secret)}')

if len(password) < 12:
    print('That password is pretty weak!')
else:
    print('The entered password is pretty strong!')

print('Here are all the items you wished for:')
for i in wishlist.split(','):
    print(f'{i}\n')


print('*'*80)
