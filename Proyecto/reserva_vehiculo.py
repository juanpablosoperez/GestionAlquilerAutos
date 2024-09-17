import wx
import wx.adv
from datetime import datetime
import sqlite3
from enviar_email import enviar_correo_confirmacion_pago


class ReservaVehiculo(wx.Frame):
    # codigo para la interfaz
    def __init__(self, parent, precio_por_dia, usuario_id, vehiculo_id, email):
        estilo = wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Reservar Vehículo", pos=wx.DefaultPosition,
                          size=wx.Size(400, 250), style=estilo)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        icon = wx.Icon(
            u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/gestion-de-proyectos.png",
            wx.BITMAP_TYPE_PNG)

        self.SetIcon(icon)

        self.precio_por_dia = precio_por_dia  # Guardar el precio por día
        self.usuario_id = usuario_id  # Guardar el ID del usuario
        self.vehiculo_id = vehiculo_id  # Guardar el ID del vehiculo
        self.email = email

        bSizer29 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText156 = wx.StaticText(self, wx.ID_ANY, u"Reserva de Vehículo", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText156.Wrap(-1)
        self.m_staticText156.SetFont(wx.Font(12, 74, 90, 92, False, "@Arial Unicode MS"))

        bSizer29.Add(self.m_staticText156, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        sbSizer11 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Detalles de la Reserva"), wx.VERTICAL)

        fgSizer15 = wx.FlexGridSizer(4, 2, 5, 5)
        fgSizer15.SetFlexibleDirection(wx.BOTH)
        fgSizer15.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText58 = wx.StaticText(self, wx.ID_ANY, u"Fecha de Inicio:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText58.Wrap(-1)
        self.m_staticText58.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer15.Add(self.m_staticText58, 0, wx.ALL, 5)

        self.m_datePicker1 = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                   wx.DefaultSize,
                                                   wx.adv.DP_DROPDOWN)
        fgSizer15.Add(self.m_datePicker1, 0, wx.ALL, 5)

        self.m_staticText581 = wx.StaticText(self, wx.ID_ANY, u"Fecha de Fin:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText581.Wrap(-1)
        self.m_staticText581.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer15.Add(self.m_staticText581, 0, wx.ALL, 5)

        self.m_datePicker2 = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                   wx.DefaultSize,
                                                   wx.adv.DP_DROPDOWN)
        fgSizer15.Add(self.m_datePicker2, 0, wx.ALL, 5)

        self.m_staticText5811 = wx.StaticText(self, wx.ID_ANY, u"Precio Total:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5811.Wrap(-1)
        self.m_staticText5811.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer15.Add(self.m_staticText5811, 0, wx.ALL, 5)

        self.m_textCtrl32 = wx.TextCtrl(self, wx.ID_ANY, u"$", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl32.Enable(False)

        fgSizer15.Add(self.m_textCtrl32, 0, wx.ALL, 5)

        sbSizer11.Add(fgSizer15, 0, wx.EXPAND, 5)

        bSizer29.Add(sbSizer11, 0, wx.EXPAND, 5)

        bSizer30 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button4.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_button4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button4.SetToolTip(u"Cancelar")

        bSizer30.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_button41 = wx.Button(self, wx.ID_ANY, u"Confirmar Reserva", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button41.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_button41.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button41.SetToolTip(u"Confirmar Reserva")

        bSizer30.Add(self.m_button41, 0, wx.ALL, 5)

        bSizer29.Add(bSizer30, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.SetSizer(bSizer29)
        self.Layout()

        self.Centre(wx.BOTH)

        # Eventos
        self.m_button4.Bind(wx.EVT_BUTTON, self.cerrar_sesion)
        self.m_button41.Bind(wx.EVT_BUTTON, self.confirmar_reserva)
        self.m_datePicker1.Bind(wx.adv.EVT_DATE_CHANGED, self.calcular_precio)
        self.m_datePicker2.Bind(wx.adv.EVT_DATE_CHANGED, self.calcular_precio)

    def __del__(self):
        pass

    def cerrar_sesion(self, event):
        self.Close()

    def confirmar_reserva(self, event):
        email = self.email
        fecha_inicio = self.m_datePicker1.GetValue()
        fecha_fin = self.m_datePicker2.GetValue()

        if fecha_inicio.IsValid() and fecha_fin.IsValid():
            delta = fecha_fin.Subtract(fecha_inicio)
            num_dias = delta.GetDays()

            if num_dias < 0:
                wx.MessageBox("La fecha de fin debe ser después de la fecha de inicio.", "Error", wx.OK | wx.ICON_ERROR)
                return

            monto_total = num_dias * self.precio_por_dia

            try:
                conn = sqlite3.connect('gestion_alquiler_autos.db')
                cursor = conn.cursor()

                # Insertar en la tabla Reserva con el estado 'Completada'
                cursor.execute(''' 
                    INSERT INTO Reserva (usuario_id, vehiculo_id, fecha_inicio, fecha_fin, precio_total, estado)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                self.usuario_id, self.vehiculo_id, fecha_inicio.FormatISODate(), fecha_fin.FormatISODate(), monto_total,
                'Completada'))

                reserva_id = cursor.lastrowid  # Obtener el ID de la reserva recién insertada

                # Insertar en la tabla Pago
                cursor.execute(''' 
                    INSERT INTO Pago (reserva_id, monto, fecha_pago)
                    VALUES (?, ?, ?)
                ''', (reserva_id, monto_total, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

                conn.commit()
                enviar_correo_confirmacion_pago(email)
                wx.MessageBox("Reserva confirmada exitosamente.", "Éxito", wx.OK | wx.ICON_INFORMATION)
                self.Close()
            except sqlite3.Error as e:
                wx.MessageBox(f"Error al confirmar la reserva: {e}", "Error", wx.OK | wx.ICON_ERROR)
            finally:
                conn.close()

        else:
            wx.MessageBox("Las fechas de inicio y fin son inválidas.", "Error", wx.OK | wx.ICON_ERROR)

    def calcular_precio(self, event):
        fecha_inicio = self.m_datePicker1.GetValue()
        fecha_fin = self.m_datePicker2.GetValue()

        if fecha_inicio.IsValid() and fecha_fin.IsValid():
            delta = fecha_fin.Subtract(fecha_inicio)
            num_dias = delta.GetDays()

            if num_dias < 0:
                wx.MessageBox("La fecha de fin debe ser después de la fecha de inicio.", "Error", wx.OK | wx.ICON_ERROR)
                self.m_textCtrl32.SetValue("$")
                return

            monto_total = num_dias * self.precio_por_dia
            self.m_textCtrl32.SetValue(f"${monto_total:.2f}")
        else:
            self.m_textCtrl32.SetValue("$")


