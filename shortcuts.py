import sys

from gi.repository import Gtk, Gio

class ShortcutsApplication(Gtk.Application):
	def __init__(self):
		self._init_signal_connections()

	def _init_signal_connections(self):

		self.builder = Gtk.Builder()
		self.builder.add_from_file("shortcuts.ui")

		self.window = self.builder.get_object("ShortcutsWindow")
		self.window.show_all()

win = ShortcutsApplication().window
win.connect("delete-event", Gtk.main_quit)
Gtk.main()

		



