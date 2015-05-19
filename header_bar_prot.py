
from gi.repository import Gtk, Gio

class HeaderBarWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, 
        				title="Header Bar")
        self.set_border_width(10)
        self.set_default_size(800, 500)

        hb = Gtk.HeaderBar()
        hb.props.title = "Getting Things GNOME"
        self.set_titlebar(hb)

        new_task = Gtk.Button(label="New Task")
        new_task.connect("clicked", self.on_new_task_clicked)
        hb.pack_start(new_task)

        search = Gtk.Button(label="Search icon")
        search.connect("clicked", self.on_search_clicked)
        hb.pack_end(search)
        
        

    def on_new_task_clicked(self, widget):
        print("Horray, you created a new task!")

    def on_search_clicked(self, widget):
    	print("Search for the icon, bugger!")

win = HeaderBarWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()