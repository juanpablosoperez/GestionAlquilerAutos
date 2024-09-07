import wx
import wx.grid
from agregar_vehiculo import AgregarVehiculo
from modificar_vehiculo import ModificarVehiculo
import sqlite3


###########################################################################
## Class RegistroAlquiler
###########################################################################

class RegistroAlquiler(wx.Frame):

    def __init__(self, parent):
        estilo = wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"CRUD - GESTIÓN DE VEHÍCULOS",
                          pos=wx.DefaultPosition, size=wx.Size(700, 600),
                          style=estilo)

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

        m_choice1Choices = [u"Seleccionar", u"marca", u"modelo",u"precio_por_dia",
                            u"disponibilidad", u"matricula", u"color"]

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

        self.m_button43.Bind(wx.EVT_BUTTON, self.on_modificar_click)

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
        self.m_grid2.SetColLabelValue(8, u"Tipo")
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
        self.m_grid2.SetRowLabelSize(20)
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
        # Asociar eventos
        self.m_grid2.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.on_grid_select)
        self.m_button44.Bind(wx.EVT_BUTTON, self.on_eliminar_click)

    def __del__(self):
        pass

        # Virtual event handlers, overide them in your derived class

    def buscar_auto(self, event):
        # Obtener el atributo seleccionado del ChoiceBox
        atributo_seleccionado = self.m_choice1.GetStringSelection()

        # Obtener el texto ingresado en el campo de búsqueda
        texto_busqueda = self.m_searchCtrl1.GetValue()

        # Crear la consulta SQL dinámica basada en el atributo seleccionado
        if atributo_seleccionado == "Seleccionar":
            # Mostrar todos los registros ordenados por ID descendente si no se selecciona ningún atributo
            consulta_sql = "SELECT * FROM Vehiculo ORDER BY vehiculo_id"
            valor_busqueda = None
        else:
            consulta_sql = f"SELECT * FROM Vehiculo WHERE {atributo_seleccionado} LIKE ?"
            valor_busqueda = f"%{texto_busqueda}%"

        # Conectar a la base de datos y ejecutar la consulta
        conn = sqlite3.connect('gestion_alquiler_autos.db')
        cursor = conn.cursor()
        try:
            print(f"Ejecutando consulta SQL: {consulta_sql} con valor de búsqueda: {valor_busqueda}")  # Depuración
            if valor_busqueda:
                cursor.execute(consulta_sql, (valor_busqueda,))
            else:
                cursor.execute(consulta_sql)
            resultados = cursor.fetchall()
            print(f"Resultados obtenidos: {resultados}")  # Depuración
        except sqlite3.OperationalError as e:
            wx.MessageBox(f"Error en la consulta SQL: {e}", "Error", wx.OK | wx.ICON_ERROR)
            resultados = []
        conn.close()

        # Limpiar el grid antes de mostrar los nuevos resultados
        self.m_grid2.ClearGrid()

        # Verificar si hay resultados y ajustar el tamaño de la grilla si es necesario
        if resultados:
            num_filas = len(resultados)
            num_columnas = len(resultados[0])  # Suponiendo que todas las filas tienen el mismo número de columnas

            # Ajustar el número de filas en la grilla
            if num_filas > self.m_grid2.GetNumberRows():
                self.m_grid2.AppendRows(num_filas - self.m_grid2.GetNumberRows())

            # Ajustar el número de columnas en la grilla
            if num_columnas > self.m_grid2.GetNumberCols():
                self.m_grid2.AppendCols(num_columnas - self.m_grid2.GetNumberCols())

            # Cargar los resultados en el grid
            for i, fila in enumerate(resultados):
                for j, valor in enumerate(fila):
                    # Convertir el valor del campo "disponibilidad"
                    if j == 5:  # Suponiendo que la columna "disponibilidad" es la sexta (índice 5)
                        valor = 'Disponible' if valor == 1 else 'No disponible'
                    self.m_grid2.SetCellValue(i, j, str(valor))
        else:
            wx.MessageBox("No se encontraron resultados.", "Información", wx.OK | wx.ICON_INFORMATION)

    def refrescar_busqueda(self, event):
        # Limpiar solo las filas del grid, manteniendo los títulos de las columnas
        num_rows = self.m_grid2.GetNumberRows()
        if num_rows > 0:
            self.m_grid2.DeleteRows(0, num_rows)

        # Limpiar el campo de búsqueda
        self.m_searchCtrl1.SetValue("")

        # Restablecer el ChoiceBox a la opción predeterminada
        self.m_choice1.SetSelection(0)  # Asumiendo que la primera opción es la predeterminada

    def agregar_auto(self, event):
        agregar_auto = AgregarVehiculo(None)
        agregar_auto.Show()


    def eliminar_auto(self, id_vehiculo):
        # Conectar a la base de datos
        conn = sqlite3.connect('gestion_alquiler_autos.db')
        cursor = conn.cursor()

        try:
            # Ejecutar la consulta DELETE
            cursor.execute("DELETE FROM Vehiculo WHERE vehiculo_id = ?", (id_vehiculo,))
            conn.commit()
            # Mostrar un mensaje de éxito
            wx.MessageBox("El registro ha sido eliminado con éxito.", "Éxito", wx.OK | wx.ICON_INFORMATION)
            # Refrescar el grid
            self.refrescar_busqueda(None)
        except sqlite3.Error as e:
            # Mostrar un mensaje de error
            wx.MessageBox(f"Error al eliminar el registro: {e}", "Error", wx.OK | wx.ICON_ERROR)
        finally:
            conn.close()

    def on_eliminar_click(self, event):
        if hasattr(self, 'id_vehiculo_seleccionado'):
            id_vehiculo = self.id_vehiculo_seleccionado

            # Crear el cuadro de diálogo de confirmación
            mensaje = f"¿Estás seguro de que deseas eliminar el vehículo con ID {id_vehiculo}?"
            dialogo_confirmacion = wx.MessageDialog(self, mensaje, "Confirmar Eliminación",
                                                    wx.YES_NO | wx.ICON_QUESTION)

            # Mostrar el cuadro de diálogo y obtener la respuesta del usuario
            respuesta = dialogo_confirmacion.ShowModal()

            # Si el usuario selecciona "Sí", proceder con la eliminación
            if respuesta == wx.ID_YES:
                self.eliminar_auto(id_vehiculo)
            else:
                wx.MessageBox("Eliminación cancelada.", "Información", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox("No hay un registro seleccionado para eliminar.", "Error", wx.OK | wx.ICON_ERROR)

    def salir_crud(self, event):
        self.Close()

    def on_grid_select(self, event):
        # Obtener la fila seleccionada
        fila_seleccionada = event.GetRow()

        # Obtener el valor del ID (suponiendo que es la primera columna)
        id_vehiculo = self.m_grid2.GetCellValue(fila_seleccionada, 0)

        # Guardar el ID para usarlo en la función eliminar_auto
        self.id_vehiculo_seleccionado = id_vehiculo

    def modificar_auto(self, event):
        # Obtener el índice de la fila seleccionada en la grilla
        fila_seleccionada = self.m_grid2.GetSelectedRows()

        if not fila_seleccionada:
            wx.MessageBox("Por favor, seleccione un vehículo para modificar.", "Error", wx.OK | wx.ICON_ERROR)
            return

        # Obtener los datos del vehículo seleccionado
        fila = fila_seleccionada[0]
        datos_vehiculo = [self.m_grid2.GetCellValue(fila, col) for col in range(self.m_grid2.GetNumberCols())]

        # Crear la ventana de modificación pasando los datos del vehículo
        modificar_auto = ModificarVehiculo(None, datos_vehiculo)
        modificar_auto.Show()

    def on_modificar_click(self, event):
        # Obtener el vehículo seleccionado en la grilla
        datos_vehiculo = self.obtener_datos_vehiculo_seleccionado()

        if datos_vehiculo:
            # Crear y mostrar la ventana de modificar, pasando datos_vehiculo
            ventana_modificar = ModificarVehiculo(self, datos_vehiculo)
            ventana_modificar.Show()

    def obtener_datos_vehiculo_seleccionado(self):
        # Obtener el índice de la fila seleccionada
        fila_seleccionada = self.m_grid2.GetGridCursorRow()

        if fila_seleccionada == -1:
            wx.MessageBox("Por favor, seleccione un vehículo en la grilla.", "Error", wx.OK | wx.ICON_ERROR)
            return None

        # Obtener los datos de la fila seleccionada
        id_vehiculo = self.m_grid2.GetCellValue(fila_seleccionada, 0)
        marca = self.m_grid2.GetCellValue(fila_seleccionada, 1)
        modelo = self.m_grid2.GetCellValue(fila_seleccionada, 2)
        año = self.m_grid2.GetCellValue(fila_seleccionada, 3)
        precio_por_dia = self.m_grid2.GetCellValue(fila_seleccionada, 4)
        disponibilidad = self.m_grid2.GetCellValue(fila_seleccionada, 5)
        matricula = self.m_grid2.GetCellValue(fila_seleccionada, 6)
        color = self.m_grid2.GetCellValue(fila_seleccionada, 7)

        # Convertir disponibilidad a formato legible si es necesario
        disponibilidad = "Disponible" if disponibilidad == "1" else "No disponible"

        # Retornar los datos como una tupla
        return (int(id_vehiculo), marca, modelo, año, precio_por_dia, disponibilidad, matricula, color)
