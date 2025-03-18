#!/bin/python

import subprocess

file = open("/home/msjtw/bin/paths.txt", "r")
paths = file.read()
file.close()

p1 = subprocess.Popen(["/usr/bin/wofi", "-dmenu"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
wofi_out = p1.communicate(input=(paths+'add\nremove').encode())[0]
ret_value = wofi_out.decode()[:-1]

if ret_value == 'remove':
    file = open("/home/msjtw/bin/paths.txt", "w")

    p1 = subprocess.Popen(["/usr/bin/wofi", "-dmenu"], stdin=subprocess.PIPE,  stdout=subprocess.PIPE)
    wofi_out = p1.communicate(input=(paths).encode())[0]
    ret_value = wofi_out.decode()
    paths = paths.replace(ret_value, '')
    file.write(paths)
    file.close()
elif ret_value == 'add':
    file = open("/home/msjtw/bin/paths.txt", "w")

    p1 = subprocess.Popen(["/usr/bin/wofi", "-dmenu"],  stdout=subprocess.PIPE)
    wofi_out = p1.communicate()[0]
    ret_value = wofi_out.decode()
    paths += ret_value
    file.write(paths)
    file.close()
elif ret_value != "" and paths.find(ret_value) != -1:
    p2 = subprocess.Popen(["foot", "--", "fish", "-C", f'source ~/bin/open.sh {ret_value}'])



