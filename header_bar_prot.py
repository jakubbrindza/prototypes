
import sys
from gi.repository import Gtk, Gio

class HeaderBarWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, 
        				title="Header Bar App")
        self.set_border_width(10)
        self.set_default_size(800, 500)

        hb = Gtk.HeaderBar()
        hb.props.title = "Tasks"
        hb.props.subtitle = "Your personal task manager"
        self.set_titlebar(hb)

        new_task = Gtk.Button(label="New Task")
        new_task.connect("clicked", self.on_new_task_clicked)
        hb.pack_start(new_task)
        
        select = Gtk.Button(label="Select Tasks")
        select.connect("clicked", self.on_select_clicked)
        hb.pack_end(select)

        search = Gtk.Button(label="Search")
        search.connect("clicked", self.on_search_clicked)
        hb.pack_end(search)
        

    def on_new_task_clicked(self, widget):
        print("Horray, you created a new task!")

    def on_search_clicked(self, widget):
    	print("Search for the icon, bugger!")

    def on_select_clicked(self, widget):
    	print("You are selecting tasks to be done/dismissed now!")

win = HeaderBarWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()