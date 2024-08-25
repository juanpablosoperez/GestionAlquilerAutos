import wx
from inicio_sesion import InicioSesion

class MainApp(wx.App):
    def OnInit(self):
        login_frame = InicioSesion(None)

        login_frame.Show()
        return True


if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()
