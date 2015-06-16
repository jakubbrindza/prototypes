import sys

from gi.repository import Gtk, Gio

class Editorlication(Gtk.Application):

   	def _init_signal_connections(self):
   		'''connect signals on UI elements in headerbar.ui'''

		self.builder = Gtk.Builder()
		self.builder.add_from_file("editor.ui")
		        

   		SIGNAL_CONNECTIONS_DIC = {
   		"on_mark_as_done": self.on_mark_as_done,
         "on_dismiss": self.on_dismiss
   		}

   		self.builder.connect_signals(SIGNAL_CONNECTIONS_DIC)

		self.window = builder.get_object("MainWindow")
		self.window.show_all

		Gtk.main()


   	def on_mark_as_done(self, button):
   		print("Task marked as done")

      def on_dismiss(self, button):
         print("Task dismissed")




		



