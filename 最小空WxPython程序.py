import wx


class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title="最小空WxPython程序")
        frame.Show()
        return True

app = App()
app.MainLoop()