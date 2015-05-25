import sys

from gi.repository import Gtk, Gio

class HeadeBarApplication(Gtk.Application):

   	def _init_signal_connections(self):
   		'''connect signals on UI elements in headerbar.ui'''

		self.builder = Gtk.Builder()
		self.builder.add_from_file("headerbar.ui")
		        

   		SIGNAL_CONNECTIONS_DIC = {
   		"on_add_task": self.on_add_task
   		}

   		self.builder.connect_signals(SIGNAL_CONNECTIONS_DIC)

		self.window = builder.get_object("MainWindow")
		self.window.show_all

		Gtk.main()


   	def on_add_task(self, button):
   		print("Success!")




		



