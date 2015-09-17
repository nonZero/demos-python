#!/usr/bin/python3

'''
This example is very similar to the command line groups(1) or id(1) utilities.

References:
http://stackoverflow.com/questions/9323834/python-how-to-get-group-ids-of-one-username-like-id-gn
'''

import grp  # for getgrall, getgrgid
import pwd  # for getpwnam
import getpass  # for getuser

#
# code #
#

username = getpass.getuser()
userid = pwd.getpwnam(username).pw_uid
print('current username is [{0}] and uid is [{1}]'.format(username, userid))
groups = [(g.gr_name, g.gr_gid)
          for g in grp.getgrall() if username in g.gr_mem]
primary_gid = pwd.getpwnam(username).pw_gid
details = (grp.getgrgid(primary_gid).gr_name, primary_gid)
groups.append(details)
print(groups)
