import wx
from reserva_vehiculo import ReservaVehiculo

###########################################################################
## Class VerDetalle
###########################################################################

class VerDetalle(wx.Frame):

    def __init__(self, parent, marca, modelo, anio, precio_por_dia, disponibilidad, matricula, color, tipo):
        estilo = wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Detalle del Vehículo", pos=wx.DefaultPosition,
                          size=wx.Size(400, 440), style=estilo)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        icon = wx.Icon(
            u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/gestion-de-proyectos.png",
            wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)

        bSizer28 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText54 = wx.StaticText(self, wx.ID_ANY, u"Detalle del Vehículo", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText54.Wrap(-1)
        self.m_staticText54.SetFont(wx.Font(14, 74, 90, 92, False, "@Arial Unicode MS"))

        bSizer28.Add(self.m_staticText54, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        sbSizer11 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Información General"), wx.VERTICAL)

        fgSizer11 = wx.FlexGridSizer(8, 2, 5, 5)
        fgSizer11.SetFlexibleDirection(wx.BOTH)
        fgSizer11.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # Marca
        self.m_staticText55 = wx.StaticText(self, wx.ID_ANY, u"Marca:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText55.Wrap(-1)
        self.m_staticText55.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        fgSizer11.Add(self.m_staticText55, 0, wx.ALL, 5)

        self.m_textCtrl24 = wx.TextCtrl(self, wx.ID_ANY, marca, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl24.Enable(False)
        fgSizer11.Add(self.m_textCtrl24, 0, wx.ALL, 5)

        # Modelo
        self.m_staticText551 = wx.StaticText(self, wx.ID_ANY, u"Modelo:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText551.Wrap(-1)
        self.m_staticText551.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        fgSizer11.Add(self.m_staticText551, 0, wx.ALL, 5)

        self.m_textCtrl241 = wx.TextCtrl(self, wx.ID_ANY, modelo, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl241.Enable(False)
        fgSizer11.Add(self.m_textCtrl241, 0, wx.ALL, 5)

        # Año
        self.m_staticText5511 = wx.StaticText(self, wx.ID_ANY, u"Año:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5511.Wrap(-1)
        self.m_staticText5511.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        fgSizer11.Add(self.m_staticText5511, 0, wx.ALL, 5)

        self.m_textCtrl2411 = wx.TextCtrl(self, wx.ID_ANY, str(anio), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl2411.Enable(False)
        fgSizer11.Add(self.m_textCtrl2411, 0, wx.ALL, 5)

        # Precio por Día
        self.m_staticText55111 = wx.StaticText(self, wx.ID_ANY, u"Precio por Día:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText55111.Wrap(-1)
        self.m_staticText55111.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        fgSizer11.Add(self.m_staticText55111, 0, wx.ALL, 5)

        self.m_textCtrl24111 = wx.TextCtrl(self, wx.ID_ANY, precio_por_dia, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl24111.Enable(False)
        fgSizer11.Add(self.m_textCtrl24111, 0, wx.ALL, 5)

        # Disponibilidad
        self.m_staticText551111 = wx.StaticText(self, wx.ID_ANY, u"Disponibilidad:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText551111.Wrap(-1)
        self.m_staticText551111.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        fgSizer11.Add(self.m_staticText551111, 0, wx.ALL, 5)

        self.m_textCtrl241111 = wx.TextCtrl(self, wx.ID_ANY, disponibilidad, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl241111.Enable(False)
        fgSizer11.Add(self.m_textCtrl241111, 0, wx.ALL, 5)

        # Matrícula
        self.m_staticText5511111 = wx.StaticText(self, wx.ID_ANY, u"Matrícula:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5511111.Wrap(-1)
        self.m_staticText5511111.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        fgSizer11.Add(self.m_staticText5511111, 0, wx.ALL, 5)

        self.m_textCtrl2411111 = wx.TextCtrl(self, wx.ID_ANY, matricula, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl2411111.Enable(False)
        fgSizer11.Add(self.m_textCtrl2411111, 0, wx.ALL, 5)

        # Color
        self.m_staticText55111111 = wx.StaticText(self, wx.ID_ANY, u"Color:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText55111111.Wrap(-1)
        self.m_staticText55111111.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        fgSizer11.Add(self.m_staticText55111111, 0, wx.ALL, 5)

        self.m_textCtrl24111111 = wx.TextCtrl(self, wx.ID_ANY, color, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl24111111.Enable(False)
        fgSizer11.Add(self.m_textCtrl24111111, 0, wx.ALL, 5)

        # Tipo
        self.m_staticText551111111 = wx.StaticText(self, wx.ID_ANY, u"Tipo:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText551111111.Wrap(-1)
        self.m_staticText551111111.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        fgSizer11.Add(self.m_staticText551111111, 0, wx.ALL, 5)

        self.m_textCtrl241111111 = wx.TextCtrl(self, wx.ID_ANY, tipo, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl241111111.Enable(False)
        fgSizer11.Add(self.m_textCtrl241111111, 0, wx.ALL, 5)

        sbSizer11.Add(fgSizer11, 0, wx.ALIGN_CENTER, 5)

        bSizer28.Add(sbSizer11, 0, wx.EXPAND, 5)

        bSizer30 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button43 = wx.Button(self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button43.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_button43.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button43.SetToolTip(u"Cancelar")

        bSizer30.Add(self.m_button43, 0, wx.ALL, 5)

        self.m_button431 = wx.Button(self, wx.ID_ANY, u"Reservar Vehículo", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button431.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_button431.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button431.SetToolTip(u"Reservar Vehículo")

        bSizer30.Add(self.m_button431, 0, wx.ALL, 5)

        bSizer28.Add(bSizer30, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        self.SetSizer(bSizer28)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button43.Bind(wx.EVT_BUTTON, self.cancelar)
        self.m_button431.Bind(wx.EVT_BUTTON, self.reservar)

    def cancelar(self, event):
        self.Close()

    def reservar(self, event):
        reserva_vehiculo = ReservaVehiculo(None)
        reserva_vehiculo.Show()

