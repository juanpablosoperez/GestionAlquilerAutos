import wx
import wx.grid
import sqlite3
###########################################################################
## Class MisReservas
###########################################################################

class MisReservas(wx.Frame):

    def __init__(self, parent, user_id):
        self.user_id = user_id
        estilo = wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Mis Reservas", pos=wx.DefaultPosition,
                          size=wx.Size(605, 400), style=estilo)

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

        m_choice1Choices = [u"Seleccionar", u"Estado"]
        self.m_choice1 = wx.Choice(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_choice1Choices, 0)
        self.m_choice1.SetSelection(0)
        fgSizer4.Add(self.m_choice1, 0, wx.ALL, 5)

        sbSizer1.Add(fgSizer4, 0, wx.ALIGN_CENTER, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bpButton2 = wx.BitmapButton(self.m_panel1, wx.ID_ANY, wx.Bitmap(
            u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/lupa.png",
            wx.BITMAP_TYPE_ANY),
                                           wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        self.m_bpButton2.SetToolTip(u"Buscar")

        self.m_bpButton2.SetToolTip(u"Buscar")

        bSizer8.Add(self.m_bpButton2, 0, wx.ALL, 5)

        self.m_bpButton3 = wx.BitmapButton(self.m_panel1, wx.ID_ANY, wx.Bitmap(
            u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/girar.png",
            wx.BITMAP_TYPE_ANY),
                                           wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        self.m_bpButton3.SetToolTip(u"Actualizar")

        self.m_bpButton3.SetToolTip(u"Actualizar")

        bSizer8.Add(self.m_bpButton3, 0, wx.ALL, 5)

        sbSizer1.Add(bSizer8, 0, wx.ALIGN_CENTER, 5)

        self.m_panel1.SetSizer(sbSizer1)
        self.m_panel1.Layout()
        sbSizer1.Fit(self.m_panel1)
        fgSizer5.Add(self.m_panel1, 0, wx.ALL, 5)

        bSizer111.Add(fgSizer5, 1, wx.EXPAND, 5)

        bSizer114 = wx.BoxSizer(wx.VERTICAL)

        sbSizer22 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Reservas"), wx.VERTICAL)

        fgSizer31 = wx.FlexGridSizer(4, 2, 10, 10)
        fgSizer31.SetFlexibleDirection(wx.BOTH)
        fgSizer31.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_grid_panel = wx.Panel(self, wx.ID_ANY)
        self.m_grid3 = wx.grid.Grid(self.m_grid_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid3.CreateGrid(8, 5)
        self.m_grid3.EnableEditing(False)
        self.m_grid3.EnableGridLines(True)
        self.m_grid3.EnableDragGridSize(False)
        self.m_grid3.SetMargins(5, 5)

        # Columns
        self.m_grid3.SetColLabelValue(0, u"ID Reserva")
        self.m_grid3.SetColLabelValue(1, u"Fecha de Inicio")
        self.m_grid3.SetColLabelValue(2, u"Fecha de Fin")
        self.m_grid3.SetColLabelValue(3, u"Precio Total")
        self.m_grid3.SetColLabelValue(4, u"Estado")
        self.m_grid3.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Ajuste de tamaño de columnas
        for col in range(self.m_grid3.GetNumberCols()):
            self.m_grid3.AutoSizeColumn(col)

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

        grid_sizer = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer.Add(self.m_grid3, 1,wx.ALIGN_CENTRE | wx.ALL, 5)
        self.m_grid_panel.SetSizer(grid_sizer)

        fgSizer31.Add(self.m_grid_panel, 1, wx.EXPAND, 5)

        sbSizer22.Add(fgSizer31, 1,wx.ALIGN_CENTRE  | wx.ALL, 5)

        bSizer114.Add(sbSizer22, 1, wx.EXPAND, 5)

        bSizer111.Add(bSizer114, 0, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"Volver", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button4.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_button4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button4.SetToolTip(u"Volver a Pantalla Principal")

        bSizer4.Add(self.m_button4, 0, wx.ALL, 5)

        bSizer111.Add(bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer111)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.m_bpButton2.Bind(wx.EVT_BUTTON, self.buscar_reserva)
        self.m_bpButton3.Bind(wx.EVT_BUTTON, self.refrescar_busqueda)
        self.m_button4.Bind(wx.EVT_BUTTON, self.cerrar_sesion)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def buscar_reserva(self, event):
        # Obtener el término de búsqueda y el filtro
        search_term = self.m_searchCtrl1.GetValue()
        filtro = self.m_choice1.GetStringSelection()

        # Conexión a la base de datos (SQLite en este caso)
        conn = sqlite3.connect('gestion_alquiler_autos.db')  # Ajusta el nombre de tu base de datos
        cursor = conn.cursor()

        # Query base
        query = "SELECT reserva_id, fecha_inicio, fecha_fin, precio_total, estado FROM Reserva WHERE usuario_id = ?"
        params = [self.user_id]

        # Agregar filtros según el filtro seleccionado
        if filtro == "Fecha de Inicio" and search_term:
            query += " AND fecha_inicio LIKE ?"
            params.append(f'%{search_term}%')
        elif filtro == "Fecha de Fin" and search_term:
            query += " AND fecha_fin LIKE ?"
            params.append(f'%{search_term}%')
        elif filtro == "Estado" and search_term:
            query += " AND estado LIKE ?"
            params.append(f'%{search_term}%')

        # Ejecutar la consulta
        cursor.execute(query, params)
        resultados = cursor.fetchall()

        # Limpiar la grilla
        self.m_grid3.ClearGrid()

        # Redimensionar la grilla según los resultados
        if len(resultados) > self.m_grid3.GetNumberRows():
            self.m_grid3.AppendRows(len(resultados) - self.m_grid3.GetNumberRows())
        elif len(resultados) < self.m_grid3.GetNumberRows():
            self.m_grid3.DeleteRows(0, self.m_grid3.GetNumberRows() - len(resultados))

        # Insertar resultados en la grilla
        for row, reserva in enumerate(resultados):
            for col, value in enumerate(reserva):
                self.m_grid3.SetCellValue(row, col, str(value))

        # Ajustar tamaño de la columna "Estado"
        self.m_grid3.AutoSizeColumn(4)

    def refrescar_busqueda(self, event):
        # Limpiar la grilla
        self.m_grid3.ClearGrid()

        # Restablecer el número de filas a 8 (o el número inicial deseado)
        self.m_grid3.DeleteRows(0, self.m_grid3.GetNumberRows(), True)
        self.m_grid3.AppendRows(8)

        # Limpiar el campo de búsqueda
        self.m_searchCtrl1.SetValue("")

        # Restablecer la selección del Choice
        self.m_choice1.SetSelection(0)

        # Forzar la actualización de la grilla
        self.m_grid3.ForceRefresh()

    def cerrar_sesion(self, event):
        self.Close()
