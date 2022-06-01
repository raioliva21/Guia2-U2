import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from tree_view import TreeView
from dialog import Dialog
from about_dialog import AboutDialog
from file_chooser import FileChooser
from file_actions import open_file, save_data


class Main(Gtk.Window):

    def __init__(self):
        super().__init__(title="HeaderBar Demo")
        self.set_border_width(10)
        self.set_default_size(400, 100)

        HB = Gtk.HeaderBar()
        HB.set_show_close_button(True)
        HB.props.title = "PROGRAMACION AVANZADA"
        self.set_titlebar(HB)

        self.button_open_file = Gtk.Button.new_from_icon_name(
            "gtk-open", Gtk.IconSize.MENU)
        self.button_open_file.connect("clicked", self.button_open_file_clicked)
        HB.pack_start(self.button_open_file)

        self.button_about = Gtk.Button.new_from_icon_name(
            "gtk-about", Gtk.IconSize.MENU)
        self.button_about.connect("clicked", self.button_about_clicked)
        HB.pack_start(self.button_about)

        self.listbox = Gtk.ListBox()
        self.listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(self.listbox)

        box_1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        button_add_line = Gtk.Button(label="Agregar data")
        button_add_line.connect("clicked", self.button_add_line_clicked)
        box_1.pack_start(button_add_line, True, True, 0)

        button_edit_line = Gtk.Button(label="Editar linea seleccionada")
        button_edit_line.connect("clicked", self.button_edit_line_clicked)
        box_1.pack_start(button_edit_line, True, True, 0)

        button_remove_line = Gtk.Button(label="Borrar linea seleccionada")
        button_remove_line.connect("clicked", self.button_remove_line_clicked)
        box_1.pack_start(button_remove_line, True, True, 0)


        row_1 = Gtk.ListBoxRow()
        row_1.add(box_1)
        self.listbox.add(row_1)
        self.row_2 = Gtk.ListBoxRow()
        self.listbox.add(self.row_2)

        self.connect("destroy", Gtk.main_quit)

        self.show()
        HB.show()
        self.button_about.show()
        self.button_open_file.show()
        

    def button_open_file_clicked(self, widget):
        
        flchooser = FileChooser(parent=self)

        response = flchooser.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            self.file = flchooser.get_filename()
            print("File selected: " + self.file)
            file_name = flchooser.get_filename()
            file_name = file_name.split("/")
            if file_name[-1] == "data_alumnos.json":
                self.display_TreeView()
            else:
                print("Archivo es incompatible a mostrar en TreeView.")
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        flchooser.destroy()
    
    def display_TreeView(self):
        self.tree = TreeView()
        self.row_2.add(self.tree)
        self.tree.load_json_data(self.file)
        self.show_all()

    def button_about_clicked(self, widget):
        AboutDialog()
        pass

    def button_add_line_clicked(self, widget):
        print("Boton 'Añadir' ha sido presionado")

        dialog = Dialog(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("OK clicked")
            dialog.ok_button_clicked(self.file)
            self.tree.delate_displayed_data()
            self.tree.load_json_data(self.file)
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()


    def button_edit_line_clicked(self, widget):
        
        print("Boton 'Editar' ha sido presionado")

        model, it = self.tree.get_selection().get_selected()
        # Validación no selección
        if model is None or it is None:
            print("Error")
            return

        """ se abre dialogo con textos prefijos """
        dialog = Dialog(self)
        dialog.name.set_text(model.get_value(it, 0))
        dialog.score.set_text(model.get_value(it, 1))
        dialog.notes.set_text(model.get_value(it, 2))

        response = dialog.run()

        # usuario cancela operacion editar
        if response == Gtk.ResponseType.CANCEL:
            pass
        # usuario realiza edicion en linea 
        elif response == Gtk.ResponseType.OK:
            # retorna data no modificada
            data = open_file(self.file)
            """remueve ex-linea (editada) de data"""
            for item in data:
                if item['Nombre'] == model.get_value(it, 0):
                    data.remove(item)
            # se guarda data editada en archivo
            save_data(data, self.file)
            dialog.ok_button_clicked(self.file)
            # borra data mostrada en TreeView
            self.tree.delate_displayed_data()
            # carga data de archivo ya ediatada en TreeView
            self.tree.load_json_data(self.file)

        dialog.destroy() 

    def button_remove_line_clicked(self, widget):

        print("Boton 'Borrar' ha sido presionado")

        model, it = self.tree.get_selection().get_selected()
        # Validación no selección
        if model is None or it is None:
            print("Error")
            return

        # retorna data no modificada
        data = open_file(self.file)
        """remueve ex-linea (editada) de data"""
        for item in data:
            if item['Nombre'] == model.get_value(it, 0):
                data.remove(item)
        save_data(data, self.file)
        self.tree.delate_displayed_data()
        self.tree.load_json_data(self.file) 


if __name__ == "__main__":
    # Llama
    Main()
    Gtk.main()

