import wx
import  sqlite3


class ModificarVehiculo(wx.Frame):
    # codigo para la interfaz
    def __init__(self, parent, datos_vehiculo):
        estilo = wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Modificar Vehículo", pos=wx.DefaultPosition,
                          size=wx.Size(300, 380), style=estilo)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        icon = wx.Icon(
            u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/gestion-de-proyectos.png",
            wx.BITMAP_TYPE_PNG)

        self.SetIcon(icon)

        bSizer82 = wx.BoxSizer(wx.VERTICAL)

        self.m_bitmap14 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/documento.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer82.Add(self.m_bitmap14, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Ajustamos el FlexGridSizer para que maneje dinámicamente las filas
        fgSizer9 = wx.FlexGridSizer(0, 2, 0, 0)  # 0 filas, 2 columnas, el número de filas será calculado automáticamente
        fgSizer9.SetFlexibleDirection(wx.BOTH)
        fgSizer9.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText23 = wx.StaticText(self, wx.ID_ANY, u"Marca:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText23.Wrap(-1)
        self.m_staticText23.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer9.Add(self.m_staticText23, 0, wx.ALL, 5)

        self.m_textCtrl18 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl18.SetToolTip(u"Marca del Vehículo")  # Reemplazo de SetToolTipString

        fgSizer9.Add(self.m_textCtrl18, 0, wx.ALL, 5)

        self.m_staticText24 = wx.StaticText(self, wx.ID_ANY, u"Modelo:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText24.Wrap(-1)
        self.m_staticText24.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer9.Add(self.m_staticText24, 0, wx.ALL, 5)

        self.m_textCtrl19 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl19.SetToolTip(u"Modelo del Vehículo")  # Reemplazo de SetToolTipString

        fgSizer9.Add(self.m_textCtrl19, 0, wx.ALL, 5)

        self.m_staticText241 = wx.StaticText(self, wx.ID_ANY, u"Año:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText241.Wrap(-1)
        self.m_staticText241.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer9.Add(self.m_staticText241, 0, wx.ALL, 5)

        self.m_textCtrl26 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl26.SetToolTip(u"Año de Fabricación")  # Reemplazo de SetToolTipString

        fgSizer9.Add(self.m_textCtrl26, 0, wx.ALL, 5)

        self.m_staticText242 = wx.StaticText(self, wx.ID_ANY, u"Precio por Día:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText242.Wrap(-1)
        self.m_staticText242.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer9.Add(self.m_staticText242, 0, wx.ALL, 5)

        self.m_textCtrl192 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl192.SetToolTip(u"Precio por día")  # Reemplazo de SetToolTipString

        fgSizer9.Add(self.m_textCtrl192, 0, wx.ALL, 5)

        self.m_staticText243 = wx.StaticText(self, wx.ID_ANY, u"Disponibilidad:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText243.Wrap(-1)
        self.m_staticText243.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer9.Add(self.m_staticText243, 0, wx.ALL, 5)

        m_choice2Choices = [ u"Disponible", u"No disponible"]
        self.m_choice2 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0)
        self.m_choice2.SetSelection(0)
        fgSizer9.Add(self.m_choice2, 0, wx.ALL, 5)

        self.m_staticText244 = wx.StaticText(self, wx.ID_ANY, u"Matrícula:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText244.Wrap(-1)
        self.m_staticText244.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer9.Add(self.m_staticText244, 0, wx.ALL, 5)

        self.m_textCtrl193 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl193.SetToolTip(u"Matrícula del Vehículo")  # Reemplazo de SetToolTipString

        fgSizer9.Add(self.m_textCtrl193, 0, wx.ALL, 5)

        self.m_staticText245 = wx.StaticText(self, wx.ID_ANY, u"Color:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText245.Wrap(-1)
        self.m_staticText245.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer9.Add(self.m_staticText245, 0, wx.ALL, 5)

        self.m_textCtrl194 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl194.SetToolTip(u"Color del Vehículo")  # Reemplazo de SetToolTipString

        fgSizer9.Add(self.m_textCtrl194, 0, wx.ALL, 5)

        bSizer82.Add(fgSizer9, 1, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button4.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_button4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button4.SetToolTip(u"Cancelar")  # Reemplazo de SetToolTipString

        bSizer4.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"Modificar", wx.Point(-1, -1), wx.DefaultSize, 0)
        self.m_button5.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_button5.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button5.SetToolTip(u"Modificar")  # Reemplazo de SetToolTipString

        bSizer4.Add(self.m_button5, 0, wx.ALL, 5)

        bSizer82.Add(bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer82)
        self.Layout()

        self.Centre(wx.BOTH)

        # eventos
        self.m_button4.Bind(wx.EVT_BUTTON, self.cerrar_sesion)
        self.m_button5.Bind(wx.EVT_BUTTON, self.agregar_auto)

        self.Bind(wx.EVT_BUTTON, self.agregar_auto, id=self.m_button5.GetId())

        # Guardar el ID del vehículo para futuras actualizaciones
        self.id_vehiculo = datos_vehiculo[0]

        # Inicializar los campos con los datos del vehículo
        self.inicializar_campos(datos_vehiculo)

        # Inicializar campos con datos del vehículo
        self.inicializar_campos(datos_vehiculo)

    def __del__(self):
        pass

    def inicializar_campos(self, datos_vehiculo):
        # Asumimos que datos_vehiculo es una tupla con los datos del vehículo
        self.m_textCtrl18.SetValue(datos_vehiculo[1])  # Marca
        self.m_textCtrl19.SetValue(datos_vehiculo[2])  # Modelo
        self.m_textCtrl26.SetValue(str(datos_vehiculo[3]))  # Año
        self.m_textCtrl192.SetValue(str(datos_vehiculo[4]))  # Precio por Día
        self.m_choice2.SetSelection(1 if datos_vehiculo[5] == "Disponible" else 2)  # Disponibilidad
        self.m_textCtrl193.SetValue(datos_vehiculo[6])  # Matrícula
        self.m_textCtrl194.SetValue(datos_vehiculo[7])  # Color

    def cerrar_sesion(self, event):
        self.Close()

    def agregar_auto(self, event):
        # Obtener los datos modificados
        marca = self.m_textCtrl18.GetValue()
        modelo = self.m_textCtrl19.GetValue()
        anio = self.m_textCtrl26.GetValue()
        precio_por_dia = self.m_textCtrl192.GetValue()
        disponibilidad = 1 if self.m_choice2.GetSelection() == 1 else 0
        matricula = self.m_textCtrl193.GetValue()
        color = self.m_textCtrl194.GetValue()

        # Validar los datos
        if not (marca and modelo and anio and precio_por_dia and matricula and color):
            wx.MessageBox("Por favor, complete todos los campos.", "Error", wx.OK | wx.ICON_ERROR)
            return

        # Actualizar los datos en la base de datos
        conn = sqlite3.connect('gestion_alquiler_autos.db')
        cursor = conn.cursor()

        try:
            consulta_sql = """UPDATE Vehiculo
                              SET marca = ?,
                                  modelo = ?,
                                  anio = ?,
                                  precio_por_dia = ?,
                                  disponibilidad = ?,
                                  matricula = ?,
                                  color = ?
                              WHERE vehiculo_id = ?"""
            valores = (marca, modelo, anio, precio_por_dia, disponibilidad, matricula, color, self.id_vehiculo)
            cursor.execute(consulta_sql, valores)
            conn.commit()

            wx.MessageBox("Vehículo actualizado correctamente.", "Éxito", wx.OK | wx.ICON_INFORMATION)
            self.Close()
        except sqlite3.Error as e:
            wx.MessageBox(f"Error al actualizar el vehículo: {e}", "Error", wx.OK | wx.ICON_ERROR)
        finally:
            conn.close()
