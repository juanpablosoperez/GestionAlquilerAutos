import wx
import wx.adv



###########################################################################
## Class ReservaVehiculo
###########################################################################

class ReservaVehiculo(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Reservar Vehículo", pos=wx.DefaultPosition,
                          size=wx.Size(400, 250), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer29 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText156 = wx.StaticText(self, wx.ID_ANY, u"Reserva de Vehículo", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText156.Wrap(-1)
        self.m_staticText156.SetFont(wx.Font(12, 74, 90, 92, False, "@Arial Unicode MS"))

        bSizer29.Add(self.m_staticText156, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        sbSizer11 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Detalles de la Reserva"), wx.VERTICAL)

        fgSizer15 = wx.FlexGridSizer(4, 2, 5, 5)
        fgSizer15.SetFlexibleDirection(wx.BOTH)
        fgSizer15.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText58 = wx.StaticText(self, wx.ID_ANY, u"Fecha de Inicio:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText58.Wrap(-1)
        self.m_staticText58.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer15.Add(self.m_staticText58, 0, wx.ALL, 5)

        self.m_datePicker1 = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                               wx.adv.DP_DROPDOWN)
        fgSizer15.Add(self.m_datePicker1, 0, wx.ALL, 5)

        self.m_staticText581 = wx.StaticText(self, wx.ID_ANY, u"Fecha de Fin:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText581.Wrap(-1)
        self.m_staticText581.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer15.Add(self.m_staticText581, 0, wx.ALL, 5)

        self.m_datePicker2 = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                               wx.adv.DP_DROPDOWN)
        fgSizer15.Add(self.m_datePicker2, 0, wx.ALL, 5)

        self.m_staticText5811 = wx.StaticText(self, wx.ID_ANY, u"Precio Total:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5811.Wrap(-1)
        self.m_staticText5811.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer15.Add(self.m_staticText5811, 0, wx.ALL, 5)

        self.m_textCtrl32 = wx.TextCtrl(self, wx.ID_ANY, u"$", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl32.Enable(False)

        fgSizer15.Add(self.m_textCtrl32, 0, wx.ALL, 5)

        sbSizer11.Add(fgSizer15, 0, wx.EXPAND, 5)

        bSizer29.Add(sbSizer11, 0, wx.EXPAND, 5)

        bSizer30 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button4.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_button4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button4.SetToolTip(u"Cancelar")

        bSizer30.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_button41 = wx.Button(self, wx.ID_ANY, u"Confirmar Reserva", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button41.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_button41.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button41.SetToolTip(u"Confirmar Reserva")

        bSizer30.Add(self.m_button41, 0, wx.ALL, 5)

        bSizer29.Add(bSizer30, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.SetSizer(bSizer29)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button4.Bind(wx.EVT_BUTTON, self.cerrar_asign_admin)
        self.m_button41.Bind(wx.EVT_BUTTON, self.confirmar_reserva)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def cerrar_asign_admin(self, event):
        event.Skip()

    def confirmar_reserva(self, event):
        event.Skip()