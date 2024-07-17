import wx
from login import LoginFrame
from database import inicializar_admin


class MainApp(wx.App):
    def OnInit(self):
        inicializar_admin()
        login_frame = LoginFrame(None, title="Inicio de Sesión")
        login_frame.Show()
        return True


if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()
