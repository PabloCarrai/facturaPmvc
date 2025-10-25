from tkinter import *
from tkinter import ttk


class Ventana_Principal:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Bienvenido")
        self.labelframeABMUsuario = LabelFrame(self.ventana, text="ABM Usuario")
        self.labelframeABMUsuario.grid(column=0, row=0, padx=10, pady=10)
        self.botonCrearUsuariolabelframeABMUsuario = Button(
            self.labelframeABMUsuario,
            text="Alta Usuario",
            command=self.abrirVentanaSecundariaABMUsuario,
        )
        self.botonCrearUsuariolabelframeABMUsuario.grid(
            column=0, row=0, padx=10, pady=10
        )

        self.botonBorrarUsuariolabelframeABMUsuario = Button(
            self.labelframeABMUsuario, text="Borrar Usuario"
        )
        self.botonBorrarUsuariolabelframeABMUsuario.grid(
            column=1, row=0, padx=10, pady=10
        )

        self.botonEditarUsuariolabelframeABMUsuario = Button(
            self.labelframeABMUsuario, text="Editar Usuario"
        )
        self.botonEditarUsuariolabelframeABMUsuario.grid(
            column=0, row=2, padx=10, pady=10
        )

        self.botonListarUsuariolabelframeABMUsuario = Button(
            self.labelframeABMUsuario, text="Alta Usuario"
        )
        self.botonListarUsuariolabelframeABMUsuario.grid(
            column=1, row=2, padx=10, pady=10
        )
        self.ventana.mainloop()

    def abrirVentanaSecundariaABMUsuario(self):
        Ventana_Alta_Usuario()


class Ventana_Alta_Usuario:
    def __init__(self):
        self.ventanaSecundaria = Toplevel()
        self.etiquetaVentanaSecundaria = Label(
            self.ventanaSecundaria, text="Probando Ando"
        )
        self.etiquetaVentanaSecundaria.grid(column=0, row=0, padx=10, pady=10)


prueba = Ventana_Principal()
