import wx
import sqlite3


class AgregarVehiculo(wx.Frame):
    # codigo para la interfaz
    def __init__(self, parent):
        estilo = wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Agregar Vehículo", pos=wx.DefaultPosition,
                          size=wx.Size(300, 380), style=estilo)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        icon = wx.Icon(
            u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/gestion-de-proyectos.png",
            wx.BITMAP_TYPE_PNG)

        self.SetIcon(icon)

        bSizer82 = wx.BoxSizer(wx.VERTICAL)

        self.m_bitmap15 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/expediente.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer82.Add(self.m_bitmap15, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        fgSizer9 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer9.SetFlexibleDirection(wx.BOTH)
        fgSizer9.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText23 = wx.StaticText(self, wx.ID_ANY, u"Marca:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText23.Wrap(-1)
        self.m_staticText23.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer9.Add(self.m_staticText23, 0, wx.ALL, 5)

        self.m_textCtrl18 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl18.SetToolTip(u"Marca del Vehículo")

        fgSizer9.Add(self.m_textCtrl18, 0, wx.ALL, 5)

        self.m_staticText24 = wx.StaticText(self, wx.ID_ANY, u"Modelo:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText24.Wrap(-1)
        self.m_staticText24.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer9.Add(self.m_staticText24, 0, wx.ALL, 5)

        self.m_textCtrl19 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl19.SetToolTip(u"Modelo del Vehículo")

        fgSizer9.Add(self.m_textCtrl19, 0, wx.ALL, 5)

        self.m_staticText241 = wx.StaticText(self, wx.ID_ANY, u"Año:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText241.Wrap(-1)
        self.m_staticText241.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer9.Add(self.m_staticText241, 0, wx.ALL, 5)

        self.m_textCtrl26 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl26.SetToolTip(u"Año de Fabricación")

        fgSizer9.Add(self.m_textCtrl26, 0, wx.ALL, 5)

        self.m_staticText242 = wx.StaticText(self, wx.ID_ANY, u"Precio por Día:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText242.Wrap(-1)
        self.m_staticText242.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer9.Add(self.m_staticText242, 0, wx.ALL, 5)

        self.m_textCtrl192 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl192.SetToolTip(u"Precio por día")

        fgSizer9.Add(self.m_textCtrl192, 0, wx.ALL, 5)

        self.m_staticText243 = wx.StaticText(self, wx.ID_ANY, u"Disponibilidad:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText243.Wrap(-1)
        self.m_staticText243.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer9.Add(self.m_staticText243, 0, wx.ALL, 5)

        m_choice2Choices = [u"Seleccionar", u"Disponible", u"No disponible"]
        self.m_choice2 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0)
        self.m_choice2.SetSelection(0)
        fgSizer9.Add(self.m_choice2, 0, wx.ALL, 5)

        self.m_staticText244 = wx.StaticText(self, wx.ID_ANY, u"Matrícula:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText244.Wrap(-1)
        self.m_staticText244.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer9.Add(self.m_staticText244, 0, wx.ALL, 5)

        self.m_textCtrl193 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl193.SetToolTip(u"Matrícula del Vehículo")

        fgSizer9.Add(self.m_textCtrl193, 0, wx.ALL, 5)

        self.m_staticText245 = wx.StaticText(self, wx.ID_ANY, u"Color:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText245.Wrap(-1)
        self.m_staticText245.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer9.Add(self.m_staticText245, 0, wx.ALL, 5)

        self.m_textCtrl194 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl194.SetToolTip(u"Color del Vehículo")

        fgSizer9.Add(self.m_textCtrl194, 0, wx.ALL, 5)

        bSizer82.Add(fgSizer9, 1, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button4.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_button4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button4.SetToolTip(u"Cancelar")

        bSizer4.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"Agregar", wx.Point(-1, -1), wx.DefaultSize, 0)
        self.m_button5.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_button5.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button5.SetToolTip(u"Agregar Vehículo")

        bSizer4.Add(self.m_button5, 0, wx.ALL, 5)

        bSizer82.Add(bSizer4, 0, wx.ALIGN_CENTER, 5)

        self.SetSizer(bSizer82)
        self.Layout()

        self.Centre(wx.BOTH)

        # Eventos
        self.m_button4.Bind(wx.EVT_BUTTON, self.cancelar)
        self.m_button5.Bind(wx.EVT_BUTTON, self.agregar)

    def __del__(self):
        pass

    def cancelar(self, event):
        self.Close()

    def agregar(self, event):
        # Obtener los datos del nuevo vehículo desde los controles de la interfaz
        marca = self.m_textCtrl18.GetValue()
        modelo = self.m_textCtrl19.GetValue()
        anio = int(self.m_textCtrl26.GetValue())
        precio_por_dia = float(self.m_textCtrl192.GetValue())
        disponibilidad = 1 if self.m_choice2.GetSelection() == 1 else 0
        matricula = self.m_textCtrl193.GetValue()
        color = self.m_textCtrl194.GetValue()

        conn = sqlite3.connect('gestion_alquiler_autos.db')
        cursor = conn.cursor()

        try:
            # Obtener el último ID utilizado en la tabla
            cursor.execute("SELECT MAX(vehiculo_id) FROM Vehiculo")
            ultimo_id = cursor.fetchone()[0]
            nuevo_id = (ultimo_id + 1) if ultimo_id is not None else 1

            # Insertar el nuevo registro
            consulta_sql = """
                INSERT INTO Vehiculo (vehiculo_id, marca, modelo, anio, precio_por_dia, disponibilidad, matricula, color)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(consulta_sql, (nuevo_id, marca, modelo, anio, precio_por_dia, disponibilidad, matricula, color))

            # Confirmar los cambios
            conn.commit()

            wx.MessageBox('Vehículo agregado con éxito.', 'Información', wx.OK | wx.ICON_INFORMATION)

        except sqlite3.Error as e:
            wx.MessageBox(f"Error al agregar el vehículo: {e}", "Error", wx.OK | wx.ICON_ERROR)

        finally:
            conn.close()
            self.Close()