import wx
import wx.grid

from mis_reservas import MisReservas
from ver_detalle import VerDetalle


###########################################################################
## Class PantallaPrincipalUsuario
###########################################################################

class PantallaPrincipalUsuario(wx.Frame):

    def __init__(self, parent, user_id):
        self.user_id = user_id
        estilo = wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Pantalla Principal", pos=wx.DefaultPosition,
                          size=wx.Size(700, 500), style=estilo)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        icon = wx.Icon(
            u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/gestion-de-proyectos.png",
            wx.BITMAP_TYPE_PNG)

        self.SetIcon(icon)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText156 = wx.StaticText(self, wx.ID_ANY,
                                             u"Bienvenido al Sistema de Gestión de Alquileres de Autos!",
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText156.Wrap(-1)
        self.m_staticText156.SetFont(wx.Font(12, 74, 90, 92, False, "@Arial Unicode MS"))

        bSizer7.Add(self.m_staticText156, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        fgSizer5 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer5.SetFlexibleDirection(wx.BOTH)
        fgSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.TAB_TRAVERSAL)
        self.m_panel1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel1, wx.ID_ANY, u"Ingresar Búsqueda"), wx.HORIZONTAL)

        fgSizer4 = wx.FlexGridSizer(3, 6, 10, 10)
        fgSizer4.SetFlexibleDirection(wx.BOTH)
        fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText22 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Buscar Vehículo:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        self.m_staticText22.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer4.Add(self.m_staticText22, 0, wx.ALL, 5)

        self.m_searchCtrl1 = wx.SearchCtrl(self.m_panel1, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.Size(200, -1), 0)
        self.m_searchCtrl1.ShowSearchButton(True)
        self.m_searchCtrl1.ShowCancelButton(True)
        fgSizer4.Add(self.m_searchCtrl1, 0, wx.ALL, 5)

        self.m_staticText21 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Ordernar por:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)
        self.m_staticText21.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer4.Add(self.m_staticText21, 0, wx.ALL, 5)

        m_choice1Choices = [u"Seleccionar", u"Marca", u"Modelo", u"Disponibilidad", u"Precio por Día"]
        self.m_choice1 = wx.Choice(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_choice1Choices, 0)
        self.m_choice1.SetSelection(0)
        fgSizer4.Add(self.m_choice1, 0, wx.ALL, 5)

        sbSizer1.Add(fgSizer4, 1, wx.ALIGN_CENTER, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bpButton2 = wx.BitmapButton(self.m_panel1, wx.ID_ANY, wx.Bitmap(u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/lupa.png", wx.BITMAP_TYPE_ANY),
                                           wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        self.m_bpButton2.SetToolTip(u"Buscar")

        bSizer8.Add(self.m_bpButton2, 0, wx.ALL, 5)

        self.m_bpButton3 = wx.BitmapButton(self.m_panel1, wx.ID_ANY, wx.Bitmap(u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/girar.png", wx.BITMAP_TYPE_ANY),
                                           wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        self.m_bpButton3.SetToolTip(u"Actualizar")

        bSizer8.Add(self.m_bpButton3, 0, wx.ALL, 5)

        self.m_bpButton14 = wx.BitmapButton(self.m_panel1, wx.ID_ANY, wx.Bitmap(u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/cita.png", wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        self.m_bpButton14.SetToolTip(u"Mis Reservas")

        bSizer8.Add(self.m_bpButton14, 0, wx.ALL, 5)

        sbSizer1.Add(bSizer8, 0, wx.ALIGN_CENTER, 5)

        self.m_panel1.SetSizer(sbSizer1)
        self.m_panel1.Layout()
        sbSizer1.Fit(self.m_panel1)
        fgSizer5.Add(self.m_panel1, 0, wx.ALL, 5)

        bSizer7.Add(fgSizer5, 0, wx.EXPAND, 5)

        bSizer24 = wx.BoxSizer(wx.VERTICAL)

        sbSizer9 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Resultados"), wx.VERTICAL)

        self.m_grid3 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid3.CreateGrid(12, 5)
        self.m_grid3.EnableEditing(False)
        self.m_grid3.EnableGridLines(True)
        self.m_grid3.EnableDragGridSize(False)
        self.m_grid3.SetMargins(0, 0)

        # Columns
        self.m_grid3.SetColLabelSize(30)
        self.m_grid3.SetColLabelValue(0, u"ID")
        self.m_grid3.SetColLabelValue(1, u"Marca")
        self.m_grid3.SetColLabelValue(2, u"Modelo")
        self.m_grid3.SetColLabelValue(3, u"Precio por Día")
        self.m_grid3.SetColLabelValue(4, u"Disponibilidad")
        self.m_grid3.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)


        # Ajustar tamaño de las columnas según los títulos
        self.m_grid3.AutoSizeColumns()

        # Rows
        self.m_grid3.AutoSizeRows()
        self.m_grid3.EnableDragRowSize(True)
        self.m_grid3.SetRowLabelSize(20)
        self.m_grid3.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.m_grid3.SetLabelBackgroundColour(wx.Colour(192, 192, 192))
        self.m_grid3.SetLabelFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        # Cell Defaults
        self.m_grid3.SetDefaultCellFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_grid3.SetDefaultCellAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        self.m_grid3.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_grid3.Enable(True)

        sbSizer9.Add(self.m_grid3, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer27 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button43 = wx.Button(self, wx.ID_ANY, u"Ver Detalle", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button43.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_button43.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button43.SetToolTip(u"Ver Detalle del Vehículo")

        bSizer27.Add(self.m_button43, 0, wx.ALL, 5)

        sbSizer9.Add(bSizer27, 0, wx.ALIGN_CENTER, 5)

        bSizer24.Add(sbSizer9, 1, wx.EXPAND, 5)

        bSizer7.Add(bSizer24, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer7)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_bpButton2.Bind(wx.EVT_BUTTON, self.buscar_auto)
        self.m_bpButton3.Bind(wx.EVT_BUTTON, self.refrescar_busqueda)
        self.m_bpButton14.Bind(wx.EVT_BUTTON, self.ver_mis_reservas)
        self.m_grid3.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.seleccionar_auto)
        self.m_button43.Bind(wx.EVT_BUTTON, self.ver_detalle)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def buscar_auto(self, event):
        event.Skip()

    def refrescar_busqueda(self, event):
        event.Skip()

    def seleccionar_auto(self, event):
        event.Skip()

    def ver_mis_reservas(self,event):
        mis_reservas = MisReservas(None, user_id=self.user_id)
        mis_reservas.Show()

    def ver_detalle(self, event):
        ver_detalle = VerDetalle(None)
        ver_detalle.Show()
