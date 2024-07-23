import wx

###########################################################################
## Class Inicio de Sesión
###########################################################################

class IniciodeSesion(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Inicio de Sesión", pos=wx.DefaultPosition,
                          size=wx.Size(300, 330), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

        # Main Vertical Sizer
        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        # Image
        self.m_bpButton2 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(
            u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/auto.png",
            wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        bSizer1.Add(self.m_bpButton2, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Username Label
        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"Usuario", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        self.m_staticText5.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))

        bSizer1.Add(self.m_staticText5, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Username TextCtrl
        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl1.SetMaxLength(100)
        self.m_textCtrl1.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))
        self.m_textCtrl1.SetToolTip("Nombre de Usuario")

        bSizer1.Add(self.m_textCtrl1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Password Label
        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"Contraseña", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        self.m_staticText11.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))

        bSizer1.Add(self.m_staticText11, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Password TextCtrl
        self.m_textCtrl11 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
        self.m_textCtrl11.SetMaxLength(100)
        self.m_textCtrl11.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))
        self.m_textCtrl11.SetToolTip("Contraseña")

        bSizer1.Add(self.m_textCtrl11, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # No Account Label
        self.m_staticText111 = wx.StaticText(self, wx.ID_ANY, u"No tienes cuenta?", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText111.Wrap(-1)
        self.m_staticText111.SetFont(wx.Font(8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))

        bSizer1.Add(self.m_staticText111, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Register Button
        self.m_button2 = wx.Button(self, wx.ID_ANY, u"Registrarse", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button2.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))
        self.m_button2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button2.SetToolTip("Registrarse")

        bSizer1.Add(self.m_button2, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Sizer for Cancel and Login Buttons
        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT)
        self.m_button11.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))
        self.m_button11.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button11.SetToolTip("Cancelar")

        bSizer4.Add(self.m_button11, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"Iniciar Sesión", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT)
        self.m_button1.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))
        self.m_button1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button1.SetToolTip("Iniciar Sesión")

        bSizer4.Add(self.m_button1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer1.Add(bSizer4, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button2.Bind(wx.EVT_BUTTON, self.formularioderegistro)
        self.m_button11.Bind(wx.EVT_BUTTON, self.cerrar_sesion)
        self.m_button1.Bind(wx.EVT_BUTTON, self.iniciar_sesion)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def formularioderegistro(self, event):
        event.Skip()

    def cerrar_sesion(self, event):
        event.Skip()

    def iniciar_sesion(self, event):
        event.Skip()

