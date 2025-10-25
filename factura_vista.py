from tkinter import *
from tkinter import ttk
from factura_modelo import gestorDb
from tkinter import messagebox as ms


conexion = gestorDb()


class Ventana_Principal:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Bienvenido")
        self.labelframeABMUsuario = LabelFrame(self.ventana, text="ABM Usuario")
        self.labelframeABMUsuario.grid(column=0, row=0, padx=10, pady=10)
        self.botonCrearUsuariolabelframeABMUsuario = Button(
            self.labelframeABMUsuario,
            text="Alta Usuario",
            command=self.abrirVentanaSecundariaABMUsuarioAltaUsuario,
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
            self.labelframeABMUsuario,
            text="Listar Usuario",
            command=self.abrirVentanaSecundariaABMUsuarioListarUsuario,
        )
        self.botonListarUsuariolabelframeABMUsuario.grid(
            column=1, row=2, padx=10, pady=10
        )
        self.ventana.mainloop()

    def abrirVentanaSecundariaABMUsuarioAltaUsuario(self):
        ventana = Ventana_Alta_Usuario()

    def abrirVentanaSecundariaABMUsuarioListarUsuario(self):
        ventana = Ventana_Listar_Usuario()


class Ventana_Alta_Usuario:
    def __init__(self):
        self.ventanaSecundaria = Toplevel()
        self.labelframeVentanaSecundariaABMUsuario = LabelFrame(
            self.ventanaSecundaria, text="Datos del Usuario"
        )
        self.labelframeVentanaSecundariaABMUsuario.grid(
            column=0, row=0, padx=10, pady=10
        )
        self.labelNombreABMUsuarioLabelFrameVentanaSecundariaABMUsuario = Label(
            self.labelframeVentanaSecundariaABMUsuario, text="Nombre: "
        )
        self.labelNombreABMUsuarioLabelFrameVentanaSecundariaABMUsuario.grid(
            column=0, row=0, padx=10, pady=10
        )
        self.datoEntradaNombreABMUsuarioLabelFrameVentanaSecundariaABMUsuario = (
            StringVar()
        )
        self.entradaNombreABMUsuarioLabelFrameVentanaSecundariaABMUsuario = Entry(
            self.labelframeVentanaSecundariaABMUsuario,
            textvariable=self.datoEntradaNombreABMUsuarioLabelFrameVentanaSecundariaABMUsuario,
        )
        self.entradaNombreABMUsuarioLabelFrameVentanaSecundariaABMUsuario.grid(
            column=1, row=0, padx=10, pady=10
        )
        self.labelApellidoABMUsuarioLabelFrameVentanaSecundariaABMUsuario = Label(
            self.labelframeVentanaSecundariaABMUsuario, text="Apellido: "
        )
        self.labelApellidoABMUsuarioLabelFrameVentanaSecundariaABMUsuario.grid(
            column=0, row=1, padx=10, pady=10
        )
        self.datoEntradaApellidoABMUsuarioLabelFrameVentanaSecundariaABMUsuario = (
            StringVar()
        )
        self.entradaApellidoABMUsuarioLabelFrameVentanaSecundariaABMUsuario = Entry(
            self.labelframeVentanaSecundariaABMUsuario,
            textvariable=self.datoEntradaApellidoABMUsuarioLabelFrameVentanaSecundariaABMUsuario,
        )
        self.entradaApellidoABMUsuarioLabelFrameVentanaSecundariaABMUsuario.grid(
            column=1, row=1, padx=10, pady=10
        )
        self.labelEmailABMUsuarioLabelFrameVentanaSecundariaABMUsuario = Label(
            self.labelframeVentanaSecundariaABMUsuario, text="Correo: "
        )
        self.labelEmailABMUsuarioLabelFrameVentanaSecundariaABMUsuario.grid(
            column=0, row=2, padx=10, pady=10
        )
        self.datoEntradaEmailABMUsuarioLabelFrameVentanaSecundariaABMUsuario = (
            StringVar()
        )
        self.entradaEmailABMUsuarioLabelFrameVentanaSecundariaABMUsuario = Entry(
            self.labelframeVentanaSecundariaABMUsuario,
            textvariable=self.datoEntradaEmailABMUsuarioLabelFrameVentanaSecundariaABMUsuario,
        )
        self.entradaEmailABMUsuarioLabelFrameVentanaSecundariaABMUsuario.grid(
            column=1, row=2, padx=10, pady=10
        )
        self.labelTelefonoABMUsuarioLabelFrameVentanaSecundariaABMUsuario = Label(
            self.labelframeVentanaSecundariaABMUsuario, text="Telefono: "
        )
        self.labelTelefonoABMUsuarioLabelFrameVentanaSecundariaABMUsuario.grid(
            column=0, row=3, padx=10, pady=10
        )
        self.datoEntradaTelefonoABMUsuarioLabelFrameVentanaSecundariaABMUsuario = (
            StringVar()
        )
        self.entradaTelefonoABMUsuarioLabelFrameVentanaSecundariaABMUsuario = Entry(
            self.labelframeVentanaSecundariaABMUsuario,
            textvariable=self.datoEntradaTelefonoABMUsuarioLabelFrameVentanaSecundariaABMUsuario,
        )
        self.entradaTelefonoABMUsuarioLabelFrameVentanaSecundariaABMUsuario.grid(
            column=1, row=3, padx=10, pady=10
        )
        self.labelDireccionABMUsuarioLabelFrameVentanaSecundariaABMUsuario = Label(
            self.labelframeVentanaSecundariaABMUsuario, text="Direccion: "
        )
        self.labelDireccionABMUsuarioLabelFrameVentanaSecundariaABMUsuario.grid(
            column=0, row=4, padx=10, pady=10
        )
        self.datoEntradaDireccionABMUsuarioLabelFrameVentanaSecundariaABMUsuario = (
            StringVar()
        )
        self.entradaDireccionABMUsuarioLabelFrameVentanaSecundariaABMUsuario = Entry(
            self.labelframeVentanaSecundariaABMUsuario,
            textvariable=self.datoEntradaDireccionABMUsuarioLabelFrameVentanaSecundariaABMUsuario,
        )
        self.entradaDireccionABMUsuarioLabelFrameVentanaSecundariaABMUsuario.grid(
            column=1, row=4, padx=10, pady=10
        )
        self.botonRegistrarABMUsuarioLabelFrameVentanaSecundariaABMUsuario = Button(
            self.labelframeVentanaSecundariaABMUsuario,
            text="Registrar",
            command=self.registrarUsuario,
        )
        self.botonRegistrarABMUsuarioLabelFrameVentanaSecundariaABMUsuario.grid(
            column=0, row=5, padx=10, pady=10
        )
        self.botonCancelarABMUsuarioLabelFrameVentanaSecundariaABMUsuario = Button(
            self.labelframeVentanaSecundariaABMUsuario,
            text="Cancelar",
            command=self.cancelarRegistro,
        )
        self.botonCancelarABMUsuarioLabelFrameVentanaSecundariaABMUsuario.grid(
            column=1, row=5, padx=10, pady=10
        )

    def cancelarRegistro(self):
        self.ventanaSecundaria.destroy()

    def registrarUsuario(self):
        datos = (
            self.datoEntradaNombreABMUsuarioLabelFrameVentanaSecundariaABMUsuario.get(),
            self.datoEntradaApellidoABMUsuarioLabelFrameVentanaSecundariaABMUsuario.get(),
            self.datoEntradaEmailABMUsuarioLabelFrameVentanaSecundariaABMUsuario.get(),
            self.datoEntradaTelefonoABMUsuarioLabelFrameVentanaSecundariaABMUsuario.get(),
            self.datoEntradaDireccionABMUsuarioLabelFrameVentanaSecundariaABMUsuario.get(),
        )
        conexion.registrar_Usuarios(datos)
        self.entradaNombreABMUsuarioLabelFrameVentanaSecundariaABMUsuario.delete(0, END)
        self.entradaApellidoABMUsuarioLabelFrameVentanaSecundariaABMUsuario.delete(
            0, END
        )
        self.entradaEmailABMUsuarioLabelFrameVentanaSecundariaABMUsuario.delete(0, END)
        self.entradaTelefonoABMUsuarioLabelFrameVentanaSecundariaABMUsuario.delete(
            0, END
        )
        self.entradaDireccionABMUsuarioLabelFrameVentanaSecundariaABMUsuario.delete(
            0, END
        )
        ms.showinfo("Vamos", "Registrado")


class Ventana_Listar_Usuario:
    def __init__(self):
        self.ventana = Toplevel()
        
        self.labelFrameListarUsuarios = LabelFrame(self.ventana, text="Listar Usuarios")
        self.labelFrameListarUsuarios.grid(column=0, row=0, padx=10, pady=10)
        self.botonListarUsuarios = Button(
            self.labelFrameListarUsuarios,
            text="Listar Usuarios",
            command=self.listarUsuarios,
        )
        self.botonListarUsuarios.grid(column=0, row=0, padx=10, pady=10)
        self.listboxListarUsuarios = Listbox(self.labelFrameListarUsuarios)
        self.listboxListarUsuarios.grid(column=0, row=1, padx=10, pady=10)

    def listarUsuarios(self):
        self.listboxListarUsuarios.delete(0, END)
        resultado = conexion.listar_Usuarios()
        for id, nombre, apellido in resultado:
            self.listboxListarUsuarios.insert(
                END, f"{id} {nombre} {apellido}"
            )
        self.listboxListarUsuarios.config(width=0, height=0)


prueba = Ventana_Principal()
