import wx
import sqlite3
from formulario_registro import FormularioRegistro
from pantalla_principal_admin import PantallaPrincipalAdministrador
from pantalla_principal_usuario import PantallaPrincipalUsuario
###########################################################################
## Class InicioSesion
###########################################################################

class InicioSesion(wx.Frame):

    def __init__(self, parent):
        estilo = wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Inicio de Sesión", pos=wx.DefaultPosition,
                          size=wx.Size(300, 320), style=estilo)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

        icon = wx.Icon(
            u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/gestion-de-proyectos.png",
            wx.BITMAP_TYPE_PNG)

        self.SetIcon(icon)
        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText156 = wx.StaticText(self, wx.ID_ANY, u"Iniciar Sesión", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText156.Wrap(-1)
        self.m_staticText156.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        bSizer1.Add(self.m_staticText156, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_bitmap11 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/iniciar-sesion.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_bitmap11, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        sbSizer17 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Ingrese sus datos"), wx.VERTICAL)

        fgSizer20 = wx.FlexGridSizer(4, 2, 0, 0)
        fgSizer20.SetFlexibleDirection(wx.BOTH)
        fgSizer20.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"Usuario:    ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        self.m_staticText5.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

        fgSizer20.Add(self.m_staticText5, 0, wx.ALIGN_CENTER | wx.ALIGN_TOP, 5)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.Point(-1, -1), wx.DefaultSize, 0)
        self.m_textCtrl1.SetMaxLength(100)
        self.m_textCtrl1.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.m_textCtrl1.SetToolTip(wx.ToolTip(u"Nombre de Usuario"))

        fgSizer20.Add(self.m_textCtrl1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"Contraseña:   ", wx.DefaultPosition, wx.DefaultSize, 0,
                                            u"usuario")
        self.m_staticText11.Wrap(-1)
        self.m_staticText11.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.m_staticText11.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))

        fgSizer20.Add(self.m_staticText11, 0, wx.ALIGN_CENTER | wx.ALIGN_TOP, 5)

        self.m_textCtrl11 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.Point(-1, -1), wx.DefaultSize,
                                        wx.TE_PASSWORD)
        self.m_textCtrl11.SetMaxLength(100)
        self.m_textCtrl11.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.m_textCtrl11.SetToolTip(wx.ToolTip(u"Contraseña de Usuario"))

        fgSizer20.Add(self.m_textCtrl11, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        sbSizer17.Add(fgSizer20, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer1.Add(sbSizer17, 1, wx.EXPAND, 5)

        bSizer38 = wx.BoxSizer(wx.VERTICAL)

        bSizer39 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText69 = wx.StaticText(self, wx.ID_ANY, u"No tienes cuenta?", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText69.Wrap(-1)
        bSizer39.Add(self.m_staticText69, 0, wx.ALL, 5)

        bSizer38.Add(bSizer39, 0, wx.ALIGN_CENTER, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"Registrarse", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button2.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.m_button2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button2.SetToolTip(wx.ToolTip(u"Registrarse"))

        bSizer38.Add(self.m_button2, 0, wx.ALIGN_CENTER, 5)

        bSizer1.Add(bSizer38, 1, wx.ALIGN_CENTER, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"Iniciar Sesión", wx.DefaultPosition, wx.DefaultSize,
                                   wx.BU_EXACTFIT)
        self.m_button1.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.m_button1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button1.SetToolTip(wx.ToolTip(u"Iniciar Sesión"))

        bSizer4.Add(self.m_button1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)  # Actualizado

        bSizer1.Add(bSizer4, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button2.Bind(wx.EVT_BUTTON, self.formularioderegistro)
        self.m_button1.Bind(wx.EVT_BUTTON, self.iniciar_sesion)

    def __del__(self):
        pass

    def formularioderegistro(self, event):
        # Crear e iniciar la ventana de registro
        frm_registro = FormularioRegistro(self)
        frm_registro.Show()
        event.Skip()

    def iniciar_sesion(self, event):
        usuario = self.m_textCtrl1.GetValue()
        contrasena = self.m_textCtrl11.GetValue()

        if self.verificar_credenciales(usuario, contrasena):
            wx.MessageBox('Inicio de sesión exitoso', 'Info', wx.OK | wx.ICON_INFORMATION)

            rol = self.obtener_rol_usuario(usuario)
            if rol == 'administrador':
                # Aquí abres la ventana correspondiente al administrador
                self.abrir_ventana_administrador()
            elif rol == 'cliente':
                # Aquí abres la ventana correspondiente al cliente
                self.abrir_ventana_cliente()
        else:
            wx.MessageBox('Usuario o contraseña incorrectos', 'Error', wx.OK | wx.ICON_ERROR)

    def verificar_credenciales(self, usuario, contrasena):
        conn = sqlite3.connect('gestion_alquiler_autos.db')
        cursor = conn.cursor()

        # No se utiliza hashing, se compara directamente la contraseña en texto plano
        query = "SELECT * FROM Usuario WHERE nombre=? AND password=?"
        cursor.execute(query, (usuario, contrasena))
        result = cursor.fetchone()

        conn.close()

        return result is not None

    def obtener_rol_usuario(self, usuario):
        conn = sqlite3.connect('gestion_alquiler_autos.db')
        cursor = conn.cursor()

        query = "SELECT tipo FROM Usuario WHERE nombre=?"
        cursor.execute(query, (usuario,))
        result = cursor.fetchone()

        conn.close()

        return result[0] if result else None

    def abrir_ventana_administrador(self):
        ventana_admin = PantallaPrincipalAdministrador(None)
        ventana_admin.Show()
        self.Close()
    def abrir_ventana_cliente(self):
        ventana_cliente = PantallaPrincipalUsuario(None)
        ventana_cliente.Show()
        self.Close()

