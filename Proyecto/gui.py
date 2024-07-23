import wx

###########################################################################
## Class IniciodeSesion
###########################################################################

class IniciodeSesion(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Inicio de Sesión", pos=wx.DefaultPosition,
                          size=wx.Size(300, 320), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_bpButton2 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/auto.png", wx.BITMAP_TYPE_ANY),
                                           wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        bSizer1.Add(self.m_bpButton2, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"Usuario", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        self.m_staticText5.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        bSizer1.Add(self.m_staticText5, 0, wx.ALIGN_CENTER | wx.ALIGN_TOP, 5)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.Point(-1, -1), wx.DefaultSize, 0)
        self.m_textCtrl1.SetMaxLength(100)
        self.m_textCtrl1.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_textCtrl1.SetToolTip("Nombre de Usuario")

        bSizer1.Add(self.m_textCtrl1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"Contraseña", wx.DefaultPosition, wx.DefaultSize, 0,
                                            u"usuario")
        self.m_staticText11.Wrap(-1)
        self.m_staticText11.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_staticText11.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))

        bSizer1.Add(self.m_staticText11, 0, wx.ALIGN_CENTER | wx.ALIGN_TOP, 5)

        self.m_textCtrl11 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.Point(-1, -1), wx.DefaultSize, 0)
        self.m_textCtrl11.SetMaxLength(100)
        self.m_textCtrl11.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_textCtrl11.SetToolTip("Contraseña")

        bSizer1.Add(self.m_textCtrl11, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_staticText111 = wx.StaticText(self, wx.ID_ANY, u"No tienes cuenta?", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText111.Wrap(-1)
        self.m_staticText111.SetFont(wx.Font(8, 74, 90, 90, False, "@Arial Unicode MS"))

        bSizer1.Add(self.m_staticText111, 0, wx.ALIGN_CENTER | wx.ALL | wx.LEFT, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"Registrarse", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button2.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_button2.SetToolTip("Registrarse")

        bSizer1.Add(self.m_button2, 0, wx.ALIGN_CENTER | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0,
                                            u"usuario")
        self.m_staticText12.Wrap(-1)
        self.m_staticText12.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_staticText12.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))

        bSizer1.Add(self.m_staticText12, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT)
        self.m_button11.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_button11.SetToolTip("Cancelar")

        bSizer4.Add(self.m_button11, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"Iniciar Sesión", wx.DefaultPosition, wx.DefaultSize,
                                   wx.BU_EXACTFIT)
        self.m_button1.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_button1.SetToolTip("Iniciar Sesión")

        bSizer4.Add(self.m_button1, 0, wx.ALL, 5)

        bSizer1.Add(bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button2.Bind(wx.EVT_BUTTON, self.registrar_usuario)
        self.m_button11.Bind(wx.EVT_BUTTON, self.cerrar_sesion)
        self.m_button1.Bind(wx.EVT_BUTTON, self.iniciar_sesion)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def registrar_usuario(self, event):
        event.Skip()

    def cerrar_sesion(self, event):
        event.Skip()

    def iniciar_sesion(self, event):
        event.Skip()

