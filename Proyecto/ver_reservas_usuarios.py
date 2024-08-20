import wx
import wx.grid

###########################################################################
## Class VerReservasUsuarios
###########################################################################

class VerReservasUsuarios(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Reservas de Usuarios", pos=wx.DefaultPosition,
                          size=wx.Size(780, 400), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        icon = wx.Icon(
            u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/gestion-de-proyectos.png",
            wx.BITMAP_TYPE_PNG)

        self.SetIcon(icon)

        bSizer111 = wx.BoxSizer(wx.VERTICAL)

        fgSizer5 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer5.SetFlexibleDirection(wx.BOTH)
        fgSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.TAB_TRAVERSAL)
        self.m_panel1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel1, wx.ID_ANY, u"Ingresar Búsqueda"), wx.HORIZONTAL)

        fgSizer4 = wx.FlexGridSizer(3, 6, 10, 10)
        fgSizer4.SetFlexibleDirection(wx.BOTH)
        fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText22 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Buscar:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        self.m_staticText22.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer4.Add(self.m_staticText22, 0, wx.ALL, 5)

        self.m_searchCtrl1 = wx.SearchCtrl(self.m_panel1, wx.ID_ANY, u"Buscar Reserva", wx.DefaultPosition,
                                           wx.Size(200, -1), 0)
        self.m_searchCtrl1.ShowSearchButton(True)
        self.m_searchCtrl1.ShowCancelButton(True)
        fgSizer4.Add(self.m_searchCtrl1, 0, wx.ALL, 5)

        self.m_staticText21 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Buscar por:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)
        self.m_staticText21.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer4.Add(self.m_staticText21, 0, wx.ALL, 5)

        m_choice1Choices = [u"Seleccionar", u"ID_Reserva", u"ID_Usuario", u"ID_Vehiculo", u"Nombre_Usuario",
                            u"Apellido_Usuario", u"Fecha de Inicio", u"Fecha de Fin", u"Estado", u"Precio_Total"]
        self.m_choice1 = wx.Choice(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_choice1Choices, 0)
        self.m_choice1.SetSelection(0)
        fgSizer4.Add(self.m_choice1, 0, wx.ALL, 5)

        sbSizer1.Add(fgSizer4, 0, wx.ALIGN_CENTER, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bpButton2 = wx.BitmapButton(self.m_panel1, wx.ID_ANY, wx.Bitmap(u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/lupa.png", wx.BITMAP_TYPE_ANY),
                                           wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        self.m_bpButton2.SetToolTip(wx.ToolTip(u"Buscar"))

        bSizer8.Add(self.m_bpButton2, 0, wx.ALL, 5)

        self.m_bpButton3 = wx.BitmapButton(self.m_panel1, wx.ID_ANY, wx.Bitmap(u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/girar.png", wx.BITMAP_TYPE_ANY),
                                           wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        self.m_bpButton3.SetToolTip(wx.ToolTip(u"Actualizar"))

        bSizer8.Add(self.m_bpButton3, 0, wx.ALL, 5)

        sbSizer1.Add(bSizer8, 0, wx.ALIGN_CENTER, 5)

        self.m_panel1.SetSizer(sbSizer1)
        self.m_panel1.Layout()
        sbSizer1.Fit(self.m_panel1)
        fgSizer5.Add(self.m_panel1, 0, wx.ALL, 5)

        bSizer111.Add(fgSizer5, 1, wx.EXPAND, 5)

        bSizer114 = wx.BoxSizer(wx.VERTICAL)

        sbSizer22 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Reservas"), wx.VERTICAL)

        fgSizer31 = wx.FlexGridSizer(1, 1, 0, 0)
        fgSizer31.SetFlexibleDirection(wx.BOTH)
        fgSizer31.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_grid3 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid3.CreateGrid(8, 9)
        self.m_grid3.EnableEditing(False)
        self.m_grid3.EnableGridLines(True)  # Enabling grid lines
        self.m_grid3.EnableDragGridSize(False)
        self.m_grid3.SetMargins(0, 0)

        # Columns
        self.m_grid3.SetColLabelValue(0, u"ID Reserva")
        self.m_grid3.SetColLabelValue(1, u"ID Usuario")
        self.m_grid3.SetColLabelValue(2, u"Nombre")
        self.m_grid3.SetColLabelValue(3, u"Apellido")
        self.m_grid3.SetColLabelValue(4, u"ID Vehículo")
        self.m_grid3.SetColLabelValue(5, u"Fecha de Inicio")
        self.m_grid3.SetColLabelValue(6, u"Fecha de Fin")
        self.m_grid3.SetColLabelValue(7, u"Precio Total")
        self.m_grid3.SetColLabelValue(8, u"Estado")
        self.m_grid3.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Auto-size columns to fit content
        self.m_grid3.AutoSizeColumns()

        # Rows
        self.m_grid3.AutoSizeRows()
        self.m_grid3.EnableDragRowSize(True)
        self.m_grid3.SetRowLabelSize(100)
        self.m_grid3.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.m_grid3.SetLabelBackgroundColour(wx.Colour(192, 192, 192))
        self.m_grid3.SetLabelFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer31.Add(self.m_grid3, 1, wx.EXPAND | wx.ALL, 5)

        sbSizer22.Add(fgSizer31, 1, wx.EXPAND, 5)

        bSizer114.Add(sbSizer22, 1, wx.EXPAND, 5)

        bSizer111.Add(bSizer114, 0, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"Volver", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button4.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_button4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button4.SetToolTip(wx.ToolTip(u"Volver a Pantalla Principal"))

        bSizer4.Add(self.m_button4, 0, wx.ALL, 5)

        bSizer111.Add(bSizer4, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.SetSizer(bSizer111)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_bpButton2.Bind(wx.EVT_BUTTON, self.buscar_auto)
        self.m_bpButton3.Bind(wx.EVT_BUTTON, self.refrescar_busqueda)
        self.m_grid3.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.seleccionar_vehiculo)
        self.m_button4.Bind(wx.EVT_BUTTON, self.cerrar_asign_admin)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def buscar_auto(self, event):
        event.Skip()

    def refrescar_busqueda(self, event):
        event.Skip()

    def seleccionar_vehiculo(self, event):
        event.Skip()

    def cerrar_asign_admin(self, event):
        event.Skip()
