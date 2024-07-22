import wx
from database import inicializar_admin
from gui import IniciodeSesion


class MainApp(wx.App):
    def OnInit(self):
        inicializar_admin()
        login_frame = IniciodeSesion(None)
        login_frame.Show()
        return True


if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()
