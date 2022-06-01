from gi.repository import Gtk
import gi
gi.require_version("Gtk", "3.0")
from file_actions import open_file, save_data


class Dialog(Gtk.Dialog):

    def __init__(self, parent):
        super().__init__(title="Ventana de Agragacion/Edicion", transient_for=parent, flags=0)
        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK
        )

        self.set_default_size(150, 100)


        """ Gtk.Grid """

        label_name = Gtk.Label(label="Nombre")
        label_score = Gtk.Label(label="Puntaje")
        label_notes = Gtk.Label(label="Feedback")
        self.name = Gtk.Entry()
        self.score = Gtk.Entry()
        self.notes = Gtk.Entry()

        grid = Gtk.Grid()
        grid.add(label_name)
        grid.attach(self.name, 1, 0, 2, 1)
        grid.attach_next_to(label_score, label_name, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.score, label_score, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(label_notes, label_score, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.notes, label_notes, Gtk.PositionType.RIGHT, 2, 1)

        box = self.get_content_area()
        box.add(grid)
        self.show_all()

    """ se aprieta boton Ok tal que se añade data ingresada por usuario"""
    def ok_button_clicked(self, file):

        data = open_file(file)
        new_data = {"Nombre": self.name.get_text(),
                    "Puntaje": self.score.get_text(),
                    "Feedback": self.notes.get_text()
                    }

        data.append(new_data)
        save_data(data, file)