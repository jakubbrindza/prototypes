import sys

from gi.repository import Gtk, Gio

class HeaderBarApplication(Gtk.Application):
    def __init__(self):
        self._init_signal_connections()

    def _init_signal_connections(self):
        '''connect signals on UI elements in headerbar.ui'''

        self.builder = Gtk.Builder()
        self.builder.add_from_file("headbar.ui")

        SIGNAL_CONNECTIONS_DIC = {
            "on_add_task": self.on_add_task
        }

        self.builder.connect_signals(SIGNAL_CONNECTIONS_DIC)

        self.window = self.builder.get_object("MainWindow")
        self.window.show_all()


    def on_add_task(self, button):
        print("Success!")

win = HeaderBarApplication().window
win.connect("delete-event", Gtk.main_quit)
Gtk.main()