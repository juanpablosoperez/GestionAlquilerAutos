import wx
import wx.adv
import wx.grid

class Pagos(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Gestión de Pagos", pos=wx.DefaultPosition,
                          size=wx.Size(650, 540), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # Reemplaza SetSizeHintsSz con SetSizeHints
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        icon = wx.Icon(
            u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/gestion-de-proyectos.png",
            wx.BITMAP_TYPE_PNG)

        self.SetIcon(icon)

        bSizer44 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText156 = wx.StaticText(self, wx.ID_ANY, u"Gestión de Pagos", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText156.Wrap(-1)
        self.m_staticText156.SetFont(wx.Font(12, 74, 90, 92, False, "@Arial Unicode MS"))

        bSizer44.Add(self.m_staticText156, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        sbSizer19 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Filtros"), wx.VERTICAL)

        self.m_bpButton22 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/filtrar.png", wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        self.m_bpButton22.SetToolTip(u"Filtrar")

        sbSizer19.Add(self.m_bpButton22, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer46 = wx.BoxSizer(wx.VERTICAL)

        fgSizer26 = wx.FlexGridSizer(3, 2, 5, 5)
        fgSizer26.SetFlexibleDirection(wx.BOTH)
        fgSizer26.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText58 = wx.StaticText(self, wx.ID_ANY, u"Fecha de Inicio:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText58.Wrap(-1)
        self.m_staticText58.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer26.Add(self.m_staticText58, 0, wx.ALL, 5)

        self.m_datePicker3 = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                               wx.adv.DP_DROPDOWN)
        fgSizer26.Add(self.m_datePicker3, 0, wx.ALL, 5)

        self.m_staticText581 = wx.StaticText(self, wx.ID_ANY, u"Fecha de Fin:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText581.Wrap(-1)
        self.m_staticText581.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer26.Add(self.m_staticText581, 0, wx.ALL, 5)

        self.m_datePicker4 = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                               wx.adv.DP_DROPDOWN)
        fgSizer26.Add(self.m_datePicker4, 0, wx.ALL, 5)

        self.m_staticText582 = wx.StaticText(self, wx.ID_ANY, u"Monto Total:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText582.Wrap(-1)
        self.m_staticText582.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer26.Add(self.m_staticText582, 0, wx.ALL, 5)

        self.m_textCtrl32 = wx.TextCtrl(self, wx.ID_ANY, u"$", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl32.Enable(False)

        fgSizer26.Add(self.m_textCtrl32, 0, wx.ALL, 5)

        bSizer46.Add(fgSizer26, 0, wx.EXPAND, 5)

        sbSizer19.Add(bSizer46, 1, wx.EXPAND, 5)

        bSizer44.Add(sbSizer19, 0, wx.EXPAND, 5)

        sbSizer20 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Lista de Pagos"), wx.VERTICAL)

        self.m_grid3 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid3.CreateGrid(8, 6)
        self.m_grid3.EnableEditing(False)
        self.m_grid3.EnableGridLines(True)
        self.m_grid3.EnableDragGridSize(False)
        self.m_grid3.SetMargins(0, 0)

        # Columns
        self.m_grid3.SetColLabelValue(0, u"ID Pago")
        self.m_grid3.SetColLabelValue(1, u"Fecha")
        self.m_grid3.SetColLabelValue(2, u"Monto")
        self.m_grid3.SetColLabelValue(3, u"ID Usuario")
        self.m_grid3.SetColLabelValue(4, u"Nombre")
        self.m_grid3.SetColLabelValue(5, u"Apellido")
        self.m_grid3.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Ajustar el tamaño de las columnas a los títulos
        self.m_grid3.AutoSizeColumns()

        # Rows
        self.m_grid3.AutoSizeRows()
        self.m_grid3.EnableDragRowSize(True)
        self.m_grid3.SetRowLabelSize(80)
        self.m_grid3.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.m_grid3.SetLabelBackgroundColour(wx.Colour(192, 192, 192))
        self.m_grid3.SetLabelFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        # Cell Defaults
        self.m_grid3.SetDefaultCellFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_grid3.SetDefaultCellAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        self.m_grid3.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        sbSizer20.Add(self.m_grid3, 0, wx.ALL, 5)

        bSizer44.Add(sbSizer20, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer47 = wx.BoxSizer(wx.VERTICAL)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"Volver", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button4.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_button4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button4.SetToolTip(u"Volver a Pantalla Principal")

        bSizer47.Add(self.m_button4, 0, wx.ALL, 5)

        bSizer44.Add(bSizer47, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.SetSizer(bSizer44)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_bpButton22.Bind(wx.EVT_BUTTON, self.filtrar_pagos_por_fecha)
        self.m_grid3.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.seleccionar_vehiculo)
        self.m_button4.Bind(wx.EVT_BUTTON, self.cerrar_asign_admin)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def filtrar_pagos_por_fecha(self, event):
        event.Skip()

    def seleccionar_vehiculo(self, event):
        event.Skip()

    def cerrar_asign_admin(self, event):
        event.Skip()






