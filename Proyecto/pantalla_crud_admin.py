import wx
import wx.grid


###########################################################################
## Class RegistroAlquiler
###########################################################################

class RegistroAlquiler(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"CRUD - GESTIÓN DE VEHÍCULOS",
                          pos=wx.DefaultPosition, size=wx.Size(755, 600),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        icon = wx.Icon(
            u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/gestion-de-proyectos.png",
            wx.BITMAP_TYPE_PNG)

        self.SetIcon(icon)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

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
        self.m_staticText22.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))

        fgSizer4.Add(self.m_staticText22, 0, wx.ALL, 5)

        self.m_searchCtrl1 = wx.SearchCtrl(self.m_panel1, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.Size(200, -1), 0)
        self.m_searchCtrl1.ShowSearchButton(True)
        self.m_searchCtrl1.ShowCancelButton(True)
        fgSizer4.Add(self.m_searchCtrl1, 0, wx.ALL, 5)

        self.m_staticText21 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Ordenar por:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)
        self.m_staticText21.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))

        fgSizer4.Add(self.m_staticText21, 0, wx.ALL, 5)

        m_choice1Choices = [u"Seleccionar", u"ID", u"Marca", u"Modelo", u"Disponibilidad", u"Precio por Día"]
        self.m_choice1 = wx.Choice(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_choice1Choices, 0)
        self.m_choice1.SetSelection(0)
        fgSizer4.Add(self.m_choice1, 0, wx.ALL, 5)

        sbSizer1.Add(fgSizer4, 1, wx.ALIGN_CENTER, 5)

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

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bitmap2 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/coche.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.m_bitmap2, 0, wx.ALL, 5)

        self.m_bitmap3 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/coche1.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.m_bitmap3, 0, wx.ALL, 5)

        self.m_bitmap4 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/coche2.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.m_bitmap4, 0, wx.ALL, 5)

        self.m_bitmap5 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/coche3.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.m_bitmap5, 0, wx.ALL, 5)

        fgSizer5.Add(bSizer10, 0, wx.EXPAND | wx.ALL, 5)

        bSizer7.Add(fgSizer5, 0, wx.EXPAND, 5)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))
        self.m_panel2.SetMinSize(wx.Size(1024, 100))

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel2, wx.ID_ANY, u"Operaciones"), wx.VERTICAL)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button42 = wx.Button(self.m_panel2, wx.ID_ANY, u"Agregar", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button42.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))
        self.m_button42.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button42.SetToolTip(wx.ToolTip(u"Agregar"))

        bSizer9.Add(self.m_button42, 0, wx.ALL, 5)

        self.m_button43 = wx.Button(self.m_panel2, wx.ID_ANY, u"Modificar", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button43.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))
        self.m_button43.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button43.SetToolTip(wx.ToolTip(u"Modificar"))

        bSizer9.Add(self.m_button43, 0, wx.ALL, 5)

        self.m_button44 = wx.Button(self.m_panel2, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button44.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))
        self.m_button44.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button44.SetToolTip(wx.ToolTip(u"Eliminar"))

        bSizer9.Add(self.m_button44, 0, wx.ALL, 5)

        self.m_button45 = wx.Button(self.m_panel2, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button45.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))
        self.m_button45.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button45.SetToolTip(wx.ToolTip(u"Salir"))

        bSizer9.Add(self.m_button45, 0, wx.ALL, 5)

        bSizer9.AddSpacer(10)

        sbSizer2.Add(bSizer9, 0,  wx.ALL | wx.ALIGN_CENTER, 5)

        self.m_panel2.SetSizer(sbSizer2)
        self.m_panel2.Layout()
        sbSizer2.Fit(self.m_panel2)
        bSizer7.Add(self.m_panel2, 0, wx.ALL, 5)

        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel3.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))

        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel3, wx.ID_ANY, u"Detalle"), wx.VERTICAL)

        self.m_grid2 = wx.grid.Grid(self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid2.CreateGrid(12, 8)
        self.m_grid2.EnableEditing(True)
        self.m_grid2.EnableGridLines(False)
        self.m_grid2.EnableDragGridSize(False)
        self.m_grid2.SetMargins(5, 5)

        # Columns
        self.m_grid2.EnableDragColMove(False)
        self.m_grid2.EnableDragColSize(False)
        self.m_grid2.SetColLabelSize(30)
        self.m_grid2.SetColLabelValue(0, u"ID")
        self.m_grid2.SetColLabelValue(1, u"Marca")
        self.m_grid2.SetColLabelValue(2, u"Modelo")
        self.m_grid2.SetColLabelValue(3, u"Año")
        self.m_grid2.SetColLabelValue(4, u"Precio por día")
        self.m_grid2.SetColLabelValue(5, u"Disponibilidad")
        self.m_grid2.SetColLabelValue(6, u"Matrícula")
        self.m_grid2.SetColLabelValue(7, u"Color")
        self.m_grid2.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid2.SetRowSize(0, 16)
        self.m_grid2.SetRowSize(1, 16)
        self.m_grid2.SetRowSize(2, 16)
        self.m_grid2.SetRowSize(3, 16)
        self.m_grid2.SetRowSize(4, 16)
        self.m_grid2.SetRowSize(5, 16)
        self.m_grid2.SetRowSize(6, 16)
        self.m_grid2.SetRowSize(7, 17)
        self.m_grid2.SetRowSize(8, 16)
        self.m_grid2.AutoSizeRows()
        self.m_grid2.EnableDragRowSize(True)
        self.m_grid2.SetRowLabelSize(80)
        self.m_grid2.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.m_grid2.SetDefaultCellAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        sbSizer3.Add(self.m_grid2, 0, wx.ALL, 5)

        self.m_panel3.SetSizer(sbSizer3)
        self.m_panel3.Layout()
        sbSizer3.Fit(self.m_panel3)
        bSizer7.Add(self.m_panel3, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer7)
        self.Layout()

        self.Centre(wx.BOTH)
        # Connect Events
        self.m_bpButton2.Bind(wx.EVT_BUTTON, self.buscar_auto)
        self.m_bpButton3.Bind(wx.EVT_BUTTON, self.refrescar_busqueda)
        self.m_button42.Bind(wx.EVT_BUTTON, self.agregar_auto)
        self.m_button43.Bind(wx.EVT_BUTTON, self.modificar_auto)
        self.m_button44.Bind(wx.EVT_BUTTON, self.eliminar_auto)
        self.m_button45.Bind(wx.EVT_BUTTON, self.salir_crud)

    def __del__(self):
        pass

        # Virtual event handlers, overide them in your derived class

    def buscar_auto(self, event):
        event.Skip()

    def refrescar_busqueda(self, event):
        event.Skip()

    def agregar_auto(self, event):
        event.Skip()

    def modificar_auto(self, event):
        event.Skip()

    def eliminar_auto(self, event):
        event.Skip()

    def salir_crud(self, event):
        event.Skip()
