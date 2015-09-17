#!/usr/bin/python3

import sys  # for stdout
import contextlib  # for contextmanager
import os  # for remove

outfile = '/tmp/out3.txt'


@contextlib.contextmanager
def redirect_output_to(fname):
    '''Context manager to run with stdout redirected to fname.
    The file is opened for appending and closed when the block
    finishes.
    '''
    old_stdout = sys.stdout
    new_stdout = sys.stdout = open(fname, 'a')
    try:
        yield
    finally:
        sys.stdout = old_stdout
        new_stdout.close()


# Running this will destroy [outfile]!
# make sure file is empty
open(outfile, 'w').close()
# test
print('This should output nothing:')
for name in ['Fred', 'Barney']:
    with redirect_output_to(outfile):
        print('Hello, {0}!'.format(name))
print('The file now contains this:')
print(open(outfile).read())
# clean up
os.remove(outfile)
