import sys

from gi.repository import Gtk, Gio

class HeadeBarApplication(Gtk.Application):

   	def _init_signal_connections(self):
   		'''connect signals on UI elements in headerbar.ui'''

   		SIGNAL_CONNECTIONS_DIC = {
   		"on_add_task": self.on_add_task
   		}

   		builder.connect_signals(SIGNAL_CONNECTIONS_DIC)

   	def on_add_task(self, button):
   		print("Success!")


builder = Gtk.Builder()
builder.add_from_file("headerbar.ui")
        
window = builder.get_object("MainWindow")
window.show_all
		
Gtk.main()


