import wx


def mostrar_mensaje_error(mensaje):
    wx.MessageBox(mensaje, "Error", wx.OK | wx.ICON_ERROR)
