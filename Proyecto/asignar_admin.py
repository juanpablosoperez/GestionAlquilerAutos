import wx
import sqlite3

class AsignarAdmin(wx.Frame):

    def __init__(self, parent):
        estilo = wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Asignar Usuario Administrador", pos=wx.DefaultPosition,
                          size=wx.Size(600, 330), style=estilo)

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

        self.m_searchCtrl1 = wx.SearchCtrl(self.m_panel1, wx.ID_ANY, u"Buscar Usuario", wx.DefaultPosition,
                                           wx.Size(200, -1), 0)
        self.m_searchCtrl1.ShowSearchButton(True)
        self.m_searchCtrl1.ShowCancelButton(True)
        fgSizer4.Add(self.m_searchCtrl1, 0, wx.ALL, 5)

        self.m_staticText21 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Buscar por:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)
        self.m_staticText21.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer4.Add(self.m_staticText21, 0, wx.ALL, 5)

        m_choice1Choices = [u"Seleccionar", u"ID", u"Nombre"]
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

        sbSizer1.Add(bSizer8, 0, wx.ALIGN_CENTER, 5)

        self.m_panel1.SetSizer(sbSizer1)
        self.m_panel1.Layout()
        sbSizer1.Fit(self.m_panel1)
        fgSizer5.Add(self.m_panel1, 0, wx.ALL, 5)

        bSizer111.Add(fgSizer5, 1, wx.EXPAND, 5)

        bSizer114 = wx.BoxSizer(wx.VERTICAL)

        sbSizer22 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Usuario"), wx.VERTICAL)

        fgSizer31 = wx.FlexGridSizer(4, 2, 10, 10)
        fgSizer31.SetFlexibleDirection(wx.BOTH)
        fgSizer31.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText23 = wx.StaticText(self, wx.ID_ANY, u"Identificación:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText23.Wrap(-1)
        self.m_staticText23.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer31.Add(self.m_staticText23, 0, wx.ALL, 5)

        self.m_textCtrl18 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl18.SetToolTip(u"Identificación del Usuario")

        fgSizer31.Add(self.m_textCtrl18, 0, wx.ALL, 5)

        self.m_staticText231 = wx.StaticText(self, wx.ID_ANY, u"Nombre:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText231.Wrap(-1)
        self.m_staticText231.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer31.Add(self.m_staticText231, 0, wx.ALL, 5)

        self.m_textCtrl181 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl181.SetToolTip(u"Nombre del Usuario")

        fgSizer31.Add(self.m_textCtrl181, 0, wx.ALL, 5)

        self.m_staticText2311 = wx.StaticText(self, wx.ID_ANY, u"Correo:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2311.Wrap(-1)
        self.m_staticText2311.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))

        fgSizer31.Add(self.m_staticText2311, 0, wx.ALL, 5)

        self.m_textCtrl1811 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl1811.SetToolTip(u"Correo electrónico")

        fgSizer31.Add(self.m_textCtrl1811, 0, wx.ALL, 5)

        self.m_checkBox2 = wx.CheckBox(self, wx.ID_ANY, u"Administrador", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer31.Add(self.m_checkBox2, 0, wx.ALL, 5)

        self.m_checkBox21 = wx.CheckBox(self, wx.ID_ANY, u"Cliente", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer31.Add(self.m_checkBox21, 0, wx.ALL, 5)

        sbSizer22.Add(fgSizer31, 1, wx.EXPAND, 5)

        bSizer114.Add(sbSizer22, 1, wx.EXPAND, 5)

        bSizer111.Add(bSizer114, 0, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button4.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_button4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button4.SetToolTip(u"Cancelar")

        bSizer4.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"Confirmar", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button5.SetFont(wx.Font(10, 74, 90, 90, False, "@Arial Unicode MS"))
        self.m_button5.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_button5.SetToolTip(u"Confirmar")

        bSizer4.Add(self.m_button5, 0, wx.ALL, 5)

        bSizer111.Add(bSizer4, 0, wx.ALIGN_CENTER, 5)

        self.SetSizer(bSizer111)
        self.Layout()
        self.Centre(wx.BOTH)

        # Bind events
        self.m_bpButton2.Bind(wx.EVT_BUTTON, self.buscar_usuario)
        self.m_button4.Bind(wx.EVT_BUTTON, self.cerrar_asign_admin)
        self.m_bpButton3.Bind(wx.EVT_BUTTON, self.refrescar_pantalla)
        self.m_button5.Bind(wx.EVT_BUTTON, self.confirmar_admin)
        self.m_checkBox2.Bind(wx.EVT_CHECKBOX, self.actualizar_tipo_usuario)
        self.m_checkBox21.Bind(wx.EVT_CHECKBOX, self.actualizar_tipo_usuario)

    def __del__(self):
        pass

    def refrescar_pantalla(self, event):
        # Limpiar los TextCtrl (ID, Nombre, Email)
        self.m_textCtrl18.SetValue("")  # Limpiar campo de Identificación
        self.m_textCtrl181.SetValue("")  # Limpiar campo de Nombre
        self.m_textCtrl1811.SetValue("")  # Limpiar campo de Correo

        # Limpiar el SearchCtrl (Campo de búsqueda)
        self.m_searchCtrl1.SetValue("")  # Limpiar el campo de búsqueda

        # Reiniciar el ChoiceBox (Buscar por)
        self.m_choice1.SetSelection(0)  # Seleccionar el valor por defecto "Seleccionar"

        # Desmarcar los CheckBox (Administrador y Cliente)
        self.m_checkBox2.SetValue(False)  # Desmarcar Administrador
        self.m_checkBox21.SetValue(False)  # Desmarcar Cliente

    def buscar_usuario(self, event):
        # Obtener el atributo seleccionado del ChoiceBox
        atributo_seleccionado = self.m_choice1.GetStringSelection()

        # Obtener el texto ingresado en el campo de búsqueda
        texto_busqueda = self.m_searchCtrl1.GetValue()

        # Crear la consulta SQL dinámica basada en el atributo seleccionado
        if atributo_seleccionado == "Seleccionar":
            consulta_sql = "SELECT * FROM Usuario ORDER BY usuario_id"
            valor_busqueda = None
        else:
            # Mapeo del atributo seleccionado a la columna de la base de datos
            if atributo_seleccionado == "ID":
                columna = "usuario_id"
            elif atributo_seleccionado == "Nombre":
                columna = "nombre"
            else:
                wx.MessageBox("Atributo de búsqueda no válido.", "Error", wx.OK | wx.ICON_ERROR)
                return

            consulta_sql = f"SELECT * FROM Usuario WHERE {columna} LIKE ?"
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

            if resultados:
                # Tomar el primer resultado (asumiendo que es único)
                usuario = resultados[0]

                # Asumimos que los campos en la base de datos son:
                # usuario_id, nombre, apellido, email, password, telefono, direccion, tipo
                usuario_id, nombre, apellido, email, password, telefono, direccion, tipo = usuario

                # Cargar la información en los TextCtrl
                self.m_textCtrl18.SetValue(str(usuario_id))  # Identificación
                self.m_textCtrl181.SetValue(nombre)  # Nombre
                self.m_textCtrl1811.SetValue(email)  # Email

                # Manejo del tipo
                if tipo == 'administrador':
                    self.m_checkBox2.SetValue(True)
                    self.m_checkBox21.SetValue(False)
                elif tipo == 'cliente':
                    self.m_checkBox2.SetValue(False)
                    self.m_checkBox21.SetValue(True)
                else:
                    self.m_checkBox2.SetValue(False)
                    self.m_checkBox21.SetValue(False)

            else:
                wx.MessageBox("No se encontraron resultados.", "Información", wx.OK | wx.ICON_INFORMATION)
                # Limpiar los campos si no hay resultados
                self.m_textCtrl18.SetValue("")
                self.m_textCtrl181.SetValue("")
                self.m_textCtrl1811.SetValue("")
                self.m_checkBox2.SetValue(False)
                self.m_checkBox21.SetValue(False)

        except sqlite3.OperationalError as e:
            wx.MessageBox(f"Error en la consulta SQL: {e}", "Error", wx.OK | wx.ICON_ERROR)
        finally:
            conn.close()

    def cerrar_asign_admin(self, event):
        self.Close()

    def confirmar_admin(self, event):
        wx.MessageBox("Usuario confirmado", "Confirmación", wx.OK | wx.ICON_INFORMATION)

    def actualizar_tipo_usuario(self, event):
        # Verifica qué checkbox está marcado
        if self.m_checkBox2.GetValue():
            tipo = 'administrador'
        elif self.m_checkBox21.GetValue():
            tipo = 'cliente'
        else:
            return  # Ningún checkbox está seleccionado, no hacer nada

        # Obtén el ID del usuario actualmente seleccionado
        usuario_id = self.m_textCtrl18.GetValue()

        if not usuario_id:
            wx.MessageBox("Debe buscar un usuario primero.", "Advertencia", wx.OK | wx.ICON_WARNING)
            return

        # Actualiza el tipo en la base de datos
        conn = sqlite3.connect('gestion_alquiler_autos.db')
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE Usuario SET tipo = ? WHERE usuario_id = ?", (tipo, usuario_id))
            conn.commit()
            wx.MessageBox(f"Tipo de usuario actualizado a {tipo}.", "Confirmación", wx.OK | wx.ICON_INFORMATION)
        except sqlite3.OperationalError as e:
            wx.MessageBox(f"Error al actualizar el tipo de usuario: {e}", "Error", wx.OK | wx.ICON_ERROR)
        finally:
            conn.close()


