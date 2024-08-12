import wx
from database import inicializar_admin
from inicio_sesion import InicioSesion
from formulario_registro import FormularioRegistro
from pantalla_principal_admin import PantallaPrincipalAdministrador
from pantalla_crud_admin import RegistroAlquiler


class MainApp(wx.App):
    def OnInit(self):
        inicializar_admin()
        login_frame = InicioSesion(None)
        formulario_registro_frame = FormularioRegistro(None)
        pantalla_principal_admin_frame = PantallaPrincipalAdministrador(None)
        pantalla_crud_admin_frame = RegistroAlquiler(None)
        #login_frame.Show()
        #formulario_registro_frame.Show()
        #pantalla_principal_admin_frame.Show()
        pantalla_crud_admin_frame.Show()
        return True


if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()
