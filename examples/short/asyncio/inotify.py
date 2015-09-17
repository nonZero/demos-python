#!/usr/bin/python3

'''
This is an example of integrating pyinotify with asyncio

Notes:
- this is a python3 example since python2 does not have 'asyncio'.

References:
http://stackoverflow.com/questions/26414052/watch-for-a-file-with-asyncio
'''

import pyinotify
import asyncio
import os.path


class AsyncioNotifier(pyinotify.Notifier):

    '''
    Notifier subclass that plugs into the asyncio event loop.
    '''

    def __init__(self, watch_manager, loop, callback=None, default_proc_fun=None, read_freq=0, threshold=0, timeout=None):
        self.loop = loop
        self.handle_read_callback = callback
        pyinotify.Notifier.__init__(
            self, watch_manager, default_proc_fun, read_freq, threshold, timeout)
        loop.add_reader(self._fd, self.handle_read)

    def handle_read(self, *args, **kwargs):
        self.read_events()
        self.process_events()
        if self.handle_read_callback is not None:
            self.handle_read_callback(self)


class EventHandler(pyinotify.ProcessEvent):

    def my_init(self, loop):
        self.loop = loop

    def process_IN_CREATE(self, event):
        print('Creating:', event.pathname)


loop = asyncio.get_event_loop()

# set up pyinotify stuff
wm = pyinotify.WatchManager()
mask = pyinotify.IN_CREATE  # watched events
dir = '/tmp'
wm.add_watch(dir, mask)
handler = EventHandler(loop=loop)
notifier = pyinotify.AsyncioNotifier(wm, loop, default_proc_fun=handler)

loop.run_forever()
