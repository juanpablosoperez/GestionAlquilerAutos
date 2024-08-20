import wx

###########################################################################
## Class FormularioRegistro
###########################################################################

class FormularioRegistro(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Formulario de Registro", pos=wx.DefaultPosition,
                          size=wx.Size(350, 480), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        icon = wx.Icon(
            u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/gestion-de-proyectos.png",
            wx.BITMAP_TYPE_PNG)

        self.SetIcon(icon)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText156 = wx.StaticText(self, wx.ID_ANY, u"Registro de Usuario", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText156.Wrap(-1)
        self.m_staticText156.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        bSizer3.Add(self.m_staticText156, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_bitmap1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/agregar-usuario.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.Size(60, 60), 0)
        bSizer3.Add(self.m_bitmap1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        sbSizer16 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Datos Personales"), wx.VERTICAL)

        fgSizer1 = wx.FlexGridSizer(7, 2, 5, 5)  # Adjusted rows to fit all fields
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"Nombre:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        self.m_staticText5.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

        fgSizer1.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl1.SetMaxLength(100)
        self.m_textCtrl1.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.m_textCtrl1.SetToolTip(u"Nombre")

        fgSizer1.Add(self.m_textCtrl1, 0, wx.ALL, 5)

        self.m_staticText51 = wx.StaticText(self, wx.ID_ANY, u"Apellido:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)
        self.m_staticText51.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

        fgSizer1.Add(self.m_staticText51, 0, wx.ALL, 5)

        self.m_textCtrl11 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl11.SetMaxLength(100)
        self.m_textCtrl11.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.m_textCtrl11.SetToolTip(u"Apellido")

        fgSizer1.Add(self.m_textCtrl11, 0, wx.ALL, 5)

        self.m_staticText511 = wx.StaticText(self, wx.ID_ANY, u"Email:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText511.Wrap(-1)
        self.m_staticText511.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

        fgSizer1.Add(self.m_staticText511, 0, wx.ALL, 5)

        self.m_textCtrl111 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl111.SetMaxLength(100)
        self.m_textCtrl111.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.m_textCtrl111.SetToolTip(u"Correo electrónico")

        fgSizer1.Add(self.m_textCtrl111, 0, wx.ALL, 5)

        self.m_staticText5111 = wx.StaticText(self, wx.ID_ANY, u"Contraseña:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5111.Wrap(-1)
        self.m_staticText5111.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

        fgSizer1.Add(self.m_staticText5111, 0, wx.ALL, 5)

        self.m_textCtrl1111 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
        self.m_textCtrl1111.SetMaxLength(100)
        self.m_textCtrl1111.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.m_textCtrl1111.SetToolTip(u"Contraseña")

        fgSizer1.Add(self.m_textCtrl1111, 0, wx.ALL, 5)

        self.m_staticText51111 = wx.StaticText(self, wx.ID_ANY, u"Teléfono:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51111.Wrap(-1)
        self.m_staticText51111.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

        fgSizer1.Add(self.m_staticText51111, 0, wx.ALL, 5)

        self.m_textCtrl1112 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl1112.SetMaxLength(100)
        self.m_textCtrl1112.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.m_textCtrl1112.SetToolTip(u"Teléfono")

        fgSizer1.Add(self.m_textCtrl1112, 0, wx.ALL, 5)

        self.m_staticText511111 = wx.StaticText(self, wx.ID_ANY, u"Dirección:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText511111.Wrap(-1)
        self.m_staticText511111.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

        fgSizer1.Add(self.m_staticText511111, 0, wx.ALL, 5)

        self.m_textCtrl11121 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl11121.SetMaxLength(100)
        self.m_textCtrl11121.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.m_textCtrl11121.SetToolTip(u"Dirección de Domicilio")

        fgSizer1.Add(self.m_textCtrl11121, 0, wx.ALL, 5)

        self.m_staticText18 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText18.Wrap(-1)
        fgSizer1.Add(self.m_staticText18, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        sbSizer16.Add(fgSizer1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer3.Add(sbSizer16, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button4.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.m_button4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button4.SetToolTip(u"Cancelar")

        bSizer4.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"Registrarse", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button5.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.m_button5.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button5.SetToolTip(u"Registrarse")

        bSizer4.Add(self.m_button5, 0, wx.ALL, 5)

        bSizer3.Add(bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button4.Bind(wx.EVT_BUTTON, self.cerrar_sesion)
        self.m_button5.Bind(wx.EVT_BUTTON, self.registrar_usuario)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def cerrar_sesion(self, event):
        self.Close()

    def registrar_usuario(self, event):
        # Implement registration logic here
        wx.MessageBox("Usuario registrado con éxito.", "Información", wx.OK | wx.ICON_INFORMATION)
