# Guia2-U2
Guia evaluada N°2 U2 modulo programacion avanzada 2022

# Finalidad de programa
Este pograma tiene por objetivo facilitar el manejo de data asociada al rendimiento de estudiantes en un ramo hipotetico.

# Estructura de codigo
En este programa se ha optado que cada codigo de clase creada sea contenido en un archivo propio, habiendo 5 clases (subclases) creadas e importadas al archivo main. Del mismo modo, otros dos archivos son importados al archivo main; 'data_alunos.json' y 'file_actions.py' son los archivos encargados de la data asociada y el manejo de esta, respectivamente. 


# Fragmentos de codigo a destacar

1. 
    (file:///home/raimundoosf/Im%C3%A1genes/Captura%20de%20pantalla%20de%202022-06-01%2011-28-43.png![image](https://user-images.githubusercontent.com/89752816/171444899-65c2915e-9576-4184-910f-c886f3a42922.png)

    
    Descripcion: Funcion 'button_open_file_clicked()' es asociada como callback de señal 'clicked' en boton 'self.button_open_file' (ver linea 25 de archivo 'main.py'). Dentro de la funcion, se crea objeto de clase 'FileChooser', que es una clase heredada de 'Gtk.FileChooser' (ver archivo 'file_chooser.py') e incorpora filtros de busqueda añadidos en codigo. Al aplicar metodo run(), se evalua respuesta asociada; si respuesta es de tipo 'OK' se procedera al analisis de archivo seleccionado y revisar si tal archivo es el adecuado para mostrar eventualmente en TreeView. En caso de que archivo sea el correspondiente al programa, "data_alumnos.json", se llamara a funcion 'display_TreeView()' que muestra Tree con data asociada (ver archivo tree_view.py).
    
2. (file:///home/raimundoosf/Im%C3%A1genes/Captura%20de%20pantalla%20de%202022-06-01%2012-06-33.png![image](https://user-images.githubusercontent.com/89752816/171449721-49ca105c-4ef6-436e-bbe8-40c1ea813a7a.png)

    
    Descripcion: Funcion 'button_edit_line_clicked()' es asociada como callback de señal 'clicked' en boton 'button_edit_line' (ver linea 43 de archivo 'main.py'). Dentro de la funcion, primero se evalua si linea seleccionada en TreeView existe. Si accion ha sido validada, se crea objeto de clase 'Dialog', que es una clase heredada de 'Gtk.Dialog' (ver archivo 'dialog.py') e incorpora 'etiquetas' y 'entradas' asociadas para la edicion de data. Al aplicar metodo run(), se evalua respuesta asociada; si respuesta es de tipo 'OK' se procedera a la manipulacion de data.
    Nota: Metodos 'button_remove_line_clicked' y 'button_add_line_clicked' de clase 'main' presentan codigo similar al contenido en metodo recien descrito, pero implementan menos funciones. 
    
    
