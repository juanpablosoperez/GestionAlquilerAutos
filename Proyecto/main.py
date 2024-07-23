import wx
from database import inicializar_admin
from inicio_sesion import IniciodeSesion
from formulario_registro import FormulariodeRegistro


class MainApp(wx.App):
    def OnInit(self):
        inicializar_admin()
        login_frame = IniciodeSesion(None)
        formulario_registro_frame = FormulariodeRegistro(None)
        login_frame.Show()
        formulario_registro_frame.Show()
        return True


if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()
