#!/usr/bin/python3

'''
This is an example of how to use the subprocess module for streaming
'''

import subprocess  # for Popen

p = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
for line in p.stdout:
    print(line.decode().rstrip())
