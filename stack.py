import sys

from gi.repository import Gtk, Gio

class StackSwitcherApplication(Gtk.Application):
	def __init__(self):
		self._init_signal_connections()

	def _init_signal_connections(self):

		self.builder = Gtk.Builder()
		self.builder.add_from_file("stack.ui")

		self.window = self.builder.get_object("MainWindow")
		self.window.show_all()

win = StackSwitcherApplication().window
win.connect("delete-event", Gtk.main_quit)
Gtk.main()

		



