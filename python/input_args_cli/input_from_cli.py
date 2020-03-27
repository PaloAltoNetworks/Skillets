#!/usr/bin/env python3
#
# This example uses CLI arguments to gather input from the user
# The .meta-cnc file defines 3 input variables:
# username, password, and secret
#
# This script shows how to obtain the values entered from the user
#

import argparse
import sys


def main():
    print('*' * 80)

    print('This is an example python script. All stdout will be returned to the user')
    print('The user has entered 3 values from the Panhandler UI')

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="Example Username", type=str)
    parser.add_argument("-p", "--password", help="Example Password", type=str)
    parser.add_argument("-s", "--secret", help="Example Secret", type=str)
    parser.add_argument("-w", "--wishlist", help="Wish List", type=str)
    args = parser.parse_args()
    if len(sys.argv) < 2:
        parser.print_help()
        parser.exit()
        sys.exit(1)

    username = args.username
    password = args.password
    secret = args.secret
    wishlist = args.wishlist

    print(f'The entered username is: {username}')
    print(f'The entered secret has a length of {len(secret)}')

    if len(password) < 12:
        print('That password is pretty weak!')
    else:
        print('The entered password is pretty strong!')

    print(f'Wishlist is {wishlist}')
    print('*'*80)


if __name__ == '__main__':
    main()
