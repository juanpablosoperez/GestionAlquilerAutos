import wx
from database import crear_usuario, verificar_usuario
from utils import mostrar_mensaje_error


class LoginFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(LoginFrame, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Establecer la paleta de colores
        panel.SetBackgroundColour(wx.Colour(240, 240, 240))

        # Título
        titulo = wx.StaticText(panel, label="Iniciar Sesión")
        font = wx.Font(18, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        titulo.SetFont(font)
        sizer.Add(titulo, 0, wx.ALL | wx.CENTER, 10)

        # Nombre de usuario
        self.etiqueta_usuario = wx.StaticText(panel, label="Nombre de usuario:")
        sizer.Add(self.etiqueta_usuario, 0, wx.ALL, 5)
        self.texto_usuario = wx.TextCtrl(panel)
        sizer.Add(self.texto_usuario, 0, wx.ALL | wx.EXPAND, 5)

        # Contraseña
        self.etiqueta_contrasena = wx.StaticText(panel, label="Contraseña:")
        sizer.Add(self.etiqueta_contrasena, 0, wx.ALL, 5)
        self.texto_contrasena = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        sizer.Add(self.texto_contrasena, 0, wx.ALL | wx.EXPAND, 5)

        # Botones
        self.boton_iniciar_sesion = wx.Button(panel, label="Iniciar Sesión")
        sizer.Add(self.boton_iniciar_sesion, 0, wx.ALL | wx.CENTER, 5)

        # Texto y botón de registro
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        texto_registro = wx.StaticText(panel, label="¿No tienes usuario?")
        boton_registro = wx.Button(panel, label="Crear aquí")
        hbox.Add(texto_registro, 0, wx.ALL | wx.CENTER, 5)
        hbox.Add(boton_registro, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(hbox, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(sizer)

        # Bind eventos
        self.boton_iniciar_sesion.Bind(wx.EVT_BUTTON, self.iniciar_sesion)
        boton_registro.Bind(wx.EVT_BUTTON, self.registrarse)

    def iniciar_sesion(self, event):
        usuario = self.texto_usuario.GetValue()
        contrasena = self.texto_contrasena.GetValue()

        if not usuario or not contrasena:
            mostrar_mensaje_error("Todos los campos son obligatorios")
            return

        if verificar_usuario(usuario, contrasena):
            wx.MessageBox(f"Bienvenido {usuario}!", "Inicio de Sesión Exitoso", wx.OK | wx.ICON_INFORMATION)
        else:
            mostrar_mensaje_error("Nombre de usuario o contraseña incorrectos")

    def registrarse(self, event):
        registro_frame = RegistroFrame(self)
        registro_frame.Show()


class RegistroFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(RegistroFrame, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Establecer la paleta de colores
        panel.SetBackgroundColour(wx.Colour(240, 240, 240))

        # Título
        titulo = wx.StaticText(panel, label="Registrar Usuario")
        font = wx.Font(18, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        titulo.SetFont(font)
        sizer.Add(titulo, 0, wx.ALL | wx.CENTER, 10)

        # Nombre de usuario
        self.etiqueta_usuario = wx.StaticText(panel, label="Nombre de usuario:")
        sizer.Add(self.etiqueta_usuario, 0, wx.ALL, 5)
        self.texto_usuario = wx.TextCtrl(panel)
        sizer.Add(self.texto_usuario, 0, wx.ALL | wx.EXPAND, 5)

        # Contraseña
        self.etiqueta_contrasena = wx.StaticText(panel, label="Contraseña:")
        sizer.Add(self.etiqueta_contrasena, 0, wx.ALL, 5)
        self.texto_contrasena = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        sizer.Add(self.texto_contrasena, 0, wx.ALL | wx.EXPAND, 5)

        # Botón de registro
        self.boton_registrar = wx.Button(panel, label="Registrar")
        sizer.Add(self.boton_registrar, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(sizer)

        # Bind evento
        self.boton_registrar.Bind(wx.EVT_BUTTON, self.registrar_usuario)

    def registrar_usuario(self, event):
        usuario = self.texto_usuario.GetValue()
        contrasena = self.texto_contrasena.GetValue()

        if not usuario or not contrasena:
            mostrar_mensaje_error("Todos los campos son obligatorios")
            return

        if crear_usuario(usuario, contrasena, "Cliente"):
            wx.MessageBox(f"Usuario {usuario} creado exitosamente!", "Registro Exitoso", wx.OK | wx.ICON_INFORMATION)
            self.Close()
        else:
            mostrar_mensaje_error("El nombre de usuario ya existe")
