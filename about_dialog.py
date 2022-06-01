from gi.repository import Gtk
import gi
gi.require_version("Gtk", "3.0")

class AboutDialog(Gtk.AboutDialog):

    def __init__(self) -> None:
        super().__init__()
    
        self.set_modal(True)
        self.set_title("Manipulacion data de rendimiento de estudiantes")
        self.set_program_name("Programa Programacion Avanzada")
        #self.set_name("Nosekeponer")
        self.set_authors(["Profesor: Fabio Durán Verdugo\
\nEstudiante: Raimundo Oliva San Feliú"])
        self.set_comments("Este programa tiene por objetivo facilitar la manipulacion de data\
 asociada al rendimiento de alumnos en el modulo 'Programacion Avanzada' utilizando GUI.")
        self.set_logo_icon_name("go-home")

        self.show_all()

        self.run()
        self.destroy()