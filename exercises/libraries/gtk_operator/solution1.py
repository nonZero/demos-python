#!/usr/bin/python

import gtk

w=gtk.Window()
w.connect('delete_event', lambda *ignored: gtk.main_quit())

hbox=gtk.HBox()
w.add(hbox)

entry1=gtk.Entry()
entry2=gtk.Entry()
result=gtk.Label()
for widget in [entry1, gtk.Label('+'), entry2, gtk.Label('='), result]:
	hbox.pack_start(widget)

def compute(*ignored):
	'''Recompute result.'''
	try:
		arg1=float(entry1.get_text())
		arg2=float(entry2.get_text())
		result.set_text(str(arg1+arg2))
	except ValueError:
		result.set_text('<ERROR>')
entry1.connect('changed', compute)
entry2.connect('changed', compute)

# Initialize so it's immediately useful
entry1.set_text('3')
entry2.set_text('2')

w.show_all()
gtk.main()
