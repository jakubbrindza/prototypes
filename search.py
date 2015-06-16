import sys

from gi.repository import Gtk, Gio

class HeaderBarApplication(Gtk.Application):
    def __init__(self):
        self._init_signal_connections()

    def _init_signal_connections(self):
        '''connect signals on UI elements in headerbar.ui'''

        self.builder = Gtk.Builder()
        self.builder.add_from_file("search.ui")

        SIGNAL_CONNECTIONS_DIC = {
        "on_search_activate": self.on_search_activate,
        "on_search_toggled": self.on_search_toggled
        }

        self.builder.connect_signals(SIGNAL_CONNECTIONS_DIC)

        self.window = self.builder.get_object("MainWindow")
        self.window.show_all()

    def on_search_activate(self, button):
        print("searching")

    def on_search_toggled(self, widget):
        search = self.builder.get_object("search")
        self.bar = self.builder.get_object("search_bar")
        self.entry = self.builder.get_object("search_entry")
        if self.bar.get_search_mode():
            search.set_active(False)
            self.bar.set_search_mode(False)
        else:
            search.set_active(True)
            self.bar.set_search_mode(True)
            self.entry.grab_focus()

win = HeaderBarApplication().window
win.connect("delete-event", Gtk.main_quit)
Gtk.main()