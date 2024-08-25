import wx
from pantalla_crud_admin import RegistroAlquiler
from pagos import Pagos
from asignar_admin import AsignarAdmin
from ver_reservas_usuarios import VerReservasUsuarios


###########################################################################
## Class PantallaPrincipalAdministrador
###########################################################################

class PantallaPrincipalAdministrador(wx.Frame):

    def __init__(self, parent):
        estilo = wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Pantalla Principal Administrador", pos=wx.DefaultPosition,
                          size=wx.Size(760, 500), style=estilo)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        icon = wx.Icon(
            u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/gestion-de-proyectos.png",
            wx.BITMAP_TYPE_PNG)

        self.SetIcon(icon)

        bSizer123 = wx.BoxSizer(wx.VERTICAL)

        self.m_toolBar2 = wx.ToolBar(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL)
        self.m_toolBar2.SetToolBitmapSize(wx.Size(24, 24))
        self.m_toolBar2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))

        # Define a default image path for testing purposes
        image_path = u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/"

        # List of buttons and their respective tooltips
        buttons = [
            (image_path + 'gestion-de-base-de-datos.png', u"Gestión de Autos", self.pantalla_crud_admin),
            (image_path + 'ingresos.png', u"Pagos", self.pantalla_pagos_admin),
            (image_path + 'reserva.png', u"Reservas", self.pantalla_reservas_admin),
            (image_path + 'administrador.png', u"Asignar Usuario Administrador", self.asignar_admin)
        ]

        for img_path, tooltip, handler in buttons:
            bmp = wx.Bitmap(img_path, wx.BITMAP_TYPE_ANY)
            if bmp.IsOk():
                button = wx.BitmapButton(self.m_toolBar2, wx.ID_ANY, bmp, wx.DefaultPosition, wx.DefaultSize,
                                         wx.BU_AUTODRAW)
                button.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
                button.SetToolTip(tooltip)
                self.m_toolBar2.AddControl(button)

                # Bind the button to the event handler
                button.Bind(wx.EVT_BUTTON, handler)
            else:
                print(f"Error loading image: {img_path}")

        # Static text controls
        self.m_staticText156 = wx.StaticText(self.m_toolBar2, wx.ID_ANY,
                                             u"Bienvenido al Sistema de Gestión de Alquileres de Autos!")
        self.m_staticText156.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Unicode MS"))
        self.m_toolBar2.AddControl(self.m_staticText156)

        # Static bitmap control for the "beneficios.png" image
        bmp_path = 'beneficios.png'
        bmp = wx.Bitmap(image_path + bmp_path, wx.BITMAP_TYPE_ANY)
        if bmp.IsOk():
            self.m_bitmap43 = wx.StaticBitmap(self.m_toolBar2, wx.ID_ANY, bmp, wx.DefaultPosition, wx.DefaultSize)
            self.m_toolBar2.AddControl(self.m_bitmap43)
        else:
            print(f"Error loading image: {image_path + bmp_path}")

        # Add empty space to push the bitmap to the right
        self.m_toolBar2.AddStretchableSpace()

        # Realize the toolbar
        self.m_toolBar2.Realize()

        # Add the toolbar to the sizer without alignment flags
        bSizer123.Add(self.m_toolBar2, 0, wx.EXPAND, 5)

        bSizer133 = wx.BoxSizer(wx.VERTICAL)

        self.m_bitmap40 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(
            u"C:/Users/JUAMPI/Documents/Desarrollo de Software/2DO AÑO D. SOFTWARE/Programacion I/Gestion de Alquiler Autos/iconos/NAZ_b7923fadf1194885a4af9248b94f48db.jpg",
            wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer133.Add(self.m_bitmap40, 0, 0, 5)

        bSizer123.Add(bSizer133, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer123)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        if hasattr(self, 'm_bpButton12'):
            self.Bind(wx.EVT_BUTTON, self.asignar_admin, self.m_bpButton12)
        else:
            print("m_bpButton12 is not defined")

    def __del__(self):
        pass


    # Virtual event handlers, overide them in your derived class
    def pantalla_crud_admin(self, event):
        crud_admin = RegistroAlquiler(None)
        crud_admin.Show()


    def pantalla_pagos_admin(self, event):
        pagos_admin = Pagos(None)
        pagos_admin.Show()


    def pantalla_reservas_admin(self, event):
        reservas_admin = VerReservasUsuarios(None)
        reservas_admin.Show()

    def asignar_admin(self, event):
        asignar_admin = AsignarAdmin(None)
        asignar_admin.Show()