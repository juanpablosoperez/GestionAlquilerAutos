import wx
import wx.adv
import wx.grid
import sqlite3

class Pagos(wx.Frame):
    def __init__(self, parent):
        estilo = wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Gestión de Pagos", pos=wx.DefaultPosition,
                          size=wx.Size(500, 500), style=estilo)  # Aumentar tamaño para mostrar el total

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        icon = wx.Icon(u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/gestion-de-proyectos.png", wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)

        bSizer44 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText156 = wx.StaticText(self, wx.ID_ANY, u"Gestión de Pagos", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText156.Wrap(-1)
        self.m_staticText156.SetFont(wx.Font(12, 74, 90, 92, False, "@Arial Unicode MS"))
        bSizer44.Add(self.m_staticText156, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Static box para filtros
        sbSizer19 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Filtros"), wx.VERTICAL)

        # Botón de filtrar
        self.m_bpButton22 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/filtrar.png", wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        self.m_bpButton22.SetToolTip(u"Filtrar")
        sbSizer19.Add(self.m_bpButton22, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Controles de fecha
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

        bSizer46.Add(fgSizer26, 0, wx.EXPAND, 5)
        sbSizer19.Add(bSizer46, 1, wx.EXPAND, 5)
        bSizer44.Add(sbSizer19, 0, wx.EXPAND, 5)

        # Static box para la lista de pagos
        sbSizer20 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Lista de Pagos"), wx.VERTICAL)

        # Configuración de la grilla
        self.m_grid3 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_grid3.CreateGrid(10, 3)
        self.m_grid3.EnableEditing(False)  # Para que no se puedan editar las celdas
        self.m_grid3.EnableGridLines(True)
        self.m_grid3.SetMargins(5, 5)

        # Configuración de columnas
        self.m_grid3.SetColLabelValue(0, u"ID Pago")
        self.m_grid3.SetColLabelValue(1, u"Fecha")
        self.m_grid3.SetColLabelValue(2, u"Monto")
        self.m_grid3.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        self.m_grid3.SetColLabelSize(40)  # Ajusta el tamaño de la etiqueta de columna (en píxeles)

        # Ajustar el tamaño de las columnas a los títulos
        self.m_grid3.SetLabelBackgroundColour(wx.Colour(192, 192, 192))
        self.m_grid3.SetLabelFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_grid3.SetDefaultCellFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_grid3.SetDefaultCellAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        self.m_grid3.AutoSizeRows()
        self.m_grid3.SetRowLabelSize(20)  # Ocultar etiquetas de filas
        self.m_grid3.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Ajustar las columnas para que ocupen todo el espacio
        self.m_grid3.AutoSizeColumns()

        # Agregar la grilla al sizer
        sbSizer20.Add(self.m_grid3, 1,wx.ALIGN_CENTRE  | wx.ALL, 5)
        bSizer44.Add(sbSizer20, 1, wx.EXPAND | wx.ALL, 5)

        # Contador de totales
        self.m_staticTextTotal = wx.StaticText(self, wx.ID_ANY, u"Total: $0.00", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticTextTotal.Wrap(-1)
        self.m_staticTextTotal.SetFont(wx.Font(10, 74, 90, 92, False, "@Arial Unicode MS"))
        bSizer44.Add(self.m_staticTextTotal, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        # Botón para volver
        bSizer47 = wx.BoxSizer(wx.VERTICAL)
        self.m_button4 = wx.Button(self, wx.ID_ANY, u"Volver", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer47.Add(self.m_button4, 0, wx.ALL, 5)
        bSizer44.Add(bSizer47, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.SetSizer(bSizer44)
        self.Layout()

        self.Centre(wx.BOTH)

        # Conectar eventos
        self.m_bpButton22.Bind(wx.EVT_BUTTON, self.filtrar_pagos_por_fecha)
        self.m_button4.Bind(wx.EVT_BUTTON, self.cerrar_sesion)

        # Cargar pagos al iniciar la ventana
        self.cargar_pagos()

    def cargar_pagos(self):
        # Conectar a la base de datos
        conexion = sqlite3.connect('gestion_alquiler_autos.db')
        cursor = conexion.cursor()

        # Consultar todos los pagos
        consulta = """
        SELECT pago_id, fecha_pago, monto
        FROM Pago
        """
        cursor.execute(consulta)
        pagos = cursor.fetchall()

        # Limpiar la grilla
        self.m_grid3.ClearGrid()
        if self.m_grid3.GetNumberRows() > 0:
            self.m_grid3.DeleteRows(0, self.m_grid3.GetNumberRows())

        # Llenar la grilla con los datos obtenidos
        total = 0
        for fila, pago in enumerate(pagos):
            self.m_grid3.AppendRows(1)
            for columna, valor in enumerate(pago):
                self.m_grid3.SetCellValue(fila, columna, str(valor))
            total += pago[2]  # Sumar el monto a total

        # Mostrar el total
        self.m_staticTextTotal.SetLabel(f"Total: ${total:.2f}")

        # Ajustar columnas
        self.m_grid3.AutoSizeColumns()
        conexion.close()

    def filtrar_pagos_por_fecha(self, event):
        fecha_inicio = self.m_datePicker3.GetValue()
        fecha_fin = self.m_datePicker4.GetValue()

        if not fecha_inicio.IsValid() or not fecha_fin.IsValid():
            wx.MessageBox("Por favor, seleccione un rango de fechas válido", "Error", wx.OK | wx.ICON_ERROR)
            return

        # Conectar a la base de datos
        conexion = sqlite3.connect('gestion_alquiler_autos.db')
        cursor = conexion.cursor()

        # Consultar pagos filtrados
        consulta = """
        SELECT pago_id, fecha_pago, monto
        FROM Pago
        WHERE fecha_pago BETWEEN ? AND ?
        """
        cursor.execute(consulta, (fecha_inicio.FormatISODate(), fecha_fin.FormatISODate()))
        pagos = cursor.fetchall()

        # Limpiar la grilla
        self.m_grid3.ClearGrid()
        if self.m_grid3.GetNumberRows() > 0:
            self.m_grid3.DeleteRows(0, self.m_grid3.GetNumberRows())

        # Llenar la grilla con los datos obtenidos
        total = 0
        for fila, pago in enumerate(pagos):
            self.m_grid3.AppendRows(1)
            for columna, valor in enumerate(pago):
                self.m_grid3.SetCellValue(fila, columna, str(valor))
            total += pago[2]  # Sumar el monto a total

        # Mostrar el total
        self.m_staticTextTotal.SetLabel(f"Total: ${total:.2f}")

        # Ajustar columnas
        self.m_grid3.AutoSizeColumns()
        conexion.close()

    def cerrar_sesion(self, event):
        self.Close()
