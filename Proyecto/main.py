import wx
from database import inicializar_admin
from inicio_sesion import InicioSesion
from formulario_registro import FormularioRegistro
from pantalla_principal_admin import PantallaPrincipalAdministrador
from pantalla_crud_admin import RegistroAlquiler
from agregar_vehiculo import AgregarVehiculo
from modificar_vehiculo import ModificarVehiculo
from asignar_admin import AsignarAdmin
from pagos import Pagos
from ver_reservas_usuarios import VerReservasUsuarios

class MainApp(wx.App):
    def OnInit(self):
        inicializar_admin()
        login_frame = InicioSesion(None)
        formulario_registro_frame = FormularioRegistro(None)
        pantalla_principal_admin_frame = PantallaPrincipalAdministrador(None)
        pantalla_crud_admin_frame = RegistroAlquiler(None)
        pantalla_agregar_vehiculo = AgregarVehiculo(None)
        pantalla_modificar_vehiculo = ModificarVehiculo(None)
        pantalla_asignar_admin = AsignarAdmin(None)
        pantalla_pagos = Pagos(None)
        pantalla_ver_reservas_usuarios = VerReservasUsuarios(None)

        #login_frame.Show()
        #formulario_registro_frame.Show()
        #pantalla_principal_admin_frame.Show()
        #pantalla_crud_admin_frame.Show()
        #pantalla_agregar_vehiculo.Show()
        #pantalla_modificar_vehiculo.Show()
        #pantalla_asignar_admin.Show()
        #pantalla_pagos.Show()
        pantalla_ver_reservas_usuarios.Show()

        return True


if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()
