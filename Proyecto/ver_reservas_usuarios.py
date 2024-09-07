import wx
import wx.grid
import sqlite3
###########################################################################
## Class VerReservasUsuarios
###########################################################################

class VerReservasUsuarios(wx.Frame):

    def __init__(self, parent):
        estilo = wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Reservas de Usuarios", pos=wx.DefaultPosition,
                          size=wx.Size(600, 400), style=estilo)

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

        m_choice1Choices = [u"Seleccionar", u"ID_Reserva", u"Nombre_Usuario",
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
        self.m_grid3.CreateGrid(8, 8)
        self.m_grid3.EnableEditing(False)
        self.m_grid3.EnableGridLines(True)  # Enabling grid lines
        self.m_grid3.EnableDragGridSize(False)
        self.m_grid3.SetMargins(0, 0)

        self.m_grid3.SetColLabelValue(0, u"ID Reserva")
        self.m_grid3.SetColLabelValue(1, u"ID Usuario")
        self.m_grid3.SetColLabelValue(2, u"Nombre")
        self.m_grid3.SetColLabelValue(3, u"Apellido")
        self.m_grid3.SetColLabelValue(4, u"Fecha de Inicio")
        self.m_grid3.SetColLabelValue(5, u"Fecha de Fin")
        self.m_grid3.SetColLabelValue(6, u"Precio Total")
        self.m_grid3.SetColLabelValue(7, u"Estado")

        self.m_grid3.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Auto-size columns to fit content
        self.m_grid3.AutoSizeColumns()

        # Rows
        self.m_grid3.AutoSizeRows()
        self.m_grid3.EnableDragRowSize(True)
        self.m_grid3.SetRowLabelSize(20)
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
        self.m_bpButton2.Bind(wx.EVT_BUTTON, self.buscar_reserva)
        self.m_bpButton3.Bind(wx.EVT_BUTTON, self.refrescar_busqueda)
        self.m_grid3.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.seleccionar_reserva)
        self.m_button4.Bind(wx.EVT_BUTTON, self.cerrar_asign_admin)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def buscar_reserva(self, event):
        # Diccionario con consultas para las diferentes tablas y campos
        consultas = {
            "ID_Reserva": (
                "SELECT r.reserva_id, u.usuario_id, u.nombre, u.apellido, r.fecha_inicio, r.fecha_fin, r.precio_total, r.estado "
                "FROM Reserva r JOIN Usuario u ON r.usuario_id = u.usuario_id "
                "WHERE r.reserva_id LIKE ?"
            ),
            "ID_Usuario": (
                "SELECT r.reserva_id, u.usuario_id, u.nombre, u.apellido, r.fecha_inicio, r.fecha_fin, r.precio_total, r.estado "
                "FROM Reserva r JOIN Usuario u ON r.usuario_id = u.usuario_id "
                "WHERE u.usuario_id LIKE ?"
            ),
            "Nombre_Usuario": (
                "SELECT r.reserva_id, u.usuario_id, u.nombre, u.apellido, r.fecha_inicio, r.fecha_fin, r.precio_total, r.estado "
                "FROM Reserva r JOIN Usuario u ON r.usuario_id = u.usuario_id "
                "WHERE u.nombre LIKE ?"
            ),
            "Apellido_Usuario": (
                "SELECT r.reserva_id, u.usuario_id, u.nombre, u.apellido, r.fecha_inicio, r.fecha_fin, r.precio_total, r.estado "
                "FROM Reserva r JOIN Usuario u ON r.usuario_id = u.usuario_id "
                "WHERE u.apellido LIKE ?"
            ),
            "Fecha de Inicio": (
                "SELECT r.reserva_id, u.usuario_id, u.nombre, u.apellido, r.fecha_inicio, r.fecha_fin, r.precio_total, r.estado "
                "FROM Reserva r JOIN Usuario u ON r.usuario_id = u.usuario_id "
                "WHERE r.fecha_inicio LIKE ?"
            ),
            "Fecha de Fin": (
                "SELECT r.reserva_id, u.usuario_id, u.nombre, u.apellido, r.fecha_inicio, r.fecha_fin, r.precio_total, r.estado "
                "FROM Reserva r JOIN Usuario u ON r.usuario_id = u.usuario_id "
                "WHERE r.fecha_fin LIKE ?"
            ),
            "Estado": (
                "SELECT r.reserva_id, u.usuario_id, u.nombre, u.apellido, r.fecha_inicio, r.fecha_fin, r.precio_total, r.estado "
                "FROM Reserva r JOIN Usuario u ON r.usuario_id = u.usuario_id "
                "WHERE r.estado LIKE ?"
            ),
            "Precio_Total": (
                "SELECT r.reserva_id, u.usuario_id, u.nombre, u.apellido, r.fecha_inicio, r.fecha_fin, r.precio_total, r.estado "
                "FROM Reserva r JOIN Usuario u ON r.usuario_id = u.usuario_id "
                "WHERE r.precio_total LIKE ?"
            )
        }

        # Obtener el campo seleccionado en el ChoiceBox
        campo_busqueda = self.m_choice1.GetStringSelection()

        # Obtener el valor ingresado en el campo de búsqueda
        valor_busqueda = self.m_searchCtrl1.GetValue()

        # Conectar a la base de datos
        try:
            conn = sqlite3.connect('gestion_alquiler_autos.db')
            cursor = conn.cursor()

            # Si no se selecciona ningún campo o se selecciona "Seleccionar", mostrar todos los registros
            if campo_busqueda == "Seleccionar" or valor_busqueda == "":
                consulta = (
                    "SELECT r.reserva_id, u.usuario_id, u.nombre, u.apellido, r.fecha_inicio, r.fecha_fin, r.precio_total, r.estado "
                    "FROM Reserva r JOIN Usuario u ON r.usuario_id = u.usuario_id "
                    "ORDER BY r.reserva_id"
                )
                cursor.execute(consulta)
            else:
                # Verificar que el campo seleccionado tenga una consulta válida
                if campo_busqueda not in consultas:
                    wx.MessageBox("Por favor, seleccione un campo válido para la búsqueda.", "Error", wx.ICON_ERROR)
                    return

                # Obtener la consulta SQL del diccionario según el campo de búsqueda
                consulta = consultas[campo_busqueda]

                # Ejecutar la consulta con el valor ingresado
                cursor.execute(consulta, ('%' + valor_busqueda + '%',))

            # Obtener resultados
            resultados = cursor.fetchall()

        # Mostrar los resultados en la grilla
            self.mostrar_resultados_en_grilla(resultados)

            # Cerrar la conexión
            cursor.close()
            conn.close()

        except Exception as e:
            wx.MessageBox(f"Error al realizar la búsqueda: {e}", "Error", wx.ICON_ERROR)


    def refrescar_busqueda(self, event):
        # Limpiar el campo de búsqueda
        self.m_searchCtrl1.SetValue("")

        # Restablecer el ChoiceBox al valor por defecto ("Seleccionar")
        self.m_choice1.SetSelection(0)

        # Limpiar la grilla
        self.limpiar_grilla()

    def limpiar_grilla(self):
        # Recorrer todas las celdas de la grilla y limpiarlas
        num_filas = self.m_grid3.GetNumberRows()
        num_columnas = self.m_grid3.GetNumberCols()

        for fila in range(num_filas):
            for columna in range(num_columnas):
                self.m_grid3.SetCellValue(fila, columna, "")

        # Opcional: Auto-ajustar el tamaño de las columnas y filas
        self.m_grid3.AutoSizeColumns()
        self.m_grid3.AutoSizeRows()

    def mostrar_resultados_en_grilla(self, resultados):
        # Limpiar la grilla antes de insertar nuevos datos
        self.m_grid3.ClearGrid()

        # Si hay más filas en los resultados que en la grilla, agregar filas
        if len(resultados) > self.m_grid3.GetNumberRows():
            self.m_grid3.AppendRows(len(resultados) - self.m_grid3.GetNumberRows())

        # Mostrar los datos en la grilla
        for fila, reserva in enumerate(resultados):
            for columna, dato in enumerate(reserva):
                self.m_grid3.SetCellValue(fila, columna, str(dato))

        # Ajustar el tamaño de las columnas y las filas
        self.m_grid3.AutoSizeColumns()
        self.m_grid3.AutoSizeRows()

    def cerrar_asign_admin(self, event):
        self.Close()

    def seleccionar_reserva(self,event):
        pass
