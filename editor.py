import sys

from gi.repository import Gtk, Gio

class EditorApplication(Gtk.Application):
   def __init__(self):
      self._init_signal_connections()

   def _init_signal_connections(self):

      self.builder = Gtk.Builder()
      self.builder.add_from_file("editor.ui")

      SIGNAL_CONNECTIONS_DIC = {
      "on_mark_as_done": self.on_mark_as_done,
      "on_dismiss": self.on_dismiss
      }

      self.builder.connect_signals(SIGNAL_CONNECTIONS_DIC)

      self.window = self.builder.get_object("MainWindow")
      self.window.show_all()

   def on_mark_as_done(self, button):
      print("Task marked as done")

   def on_dismiss(self, button):
      print("Task dismissed")

win = EditorApplication().window
win.connect("delete-event", Gtk.main_quit)
Gtk.main()