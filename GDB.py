#Global Battle Database, written in WxPython
import wx
def GDB():
    app = wx.App()
    win = wx.Frame(None, title = "Global Battle Database", size = (1280, 720))

    l1 = wx.Button(win, label = "Country Name", pos = (0, 0), size = (200,150))

    l2 = wx.Button(win, label = "Country2 Name", pos = (0, 150), size = (200,150))

    l3 = wx.Button(win, label = "Country2 Name", pos = (0, 300), size = (200,150))

    viewself = wx.Button(win, label = "View My Database", pos = (0, 600), size = (640,120))

    exitbutton = wx.Button(win, label = "Exit", pos = (640, 600), size = (640,120))

    l4 = wx.Button(win, label = "Country2 Name", pos = (0, 450), size = (200,150))

    wl1 = wx.Button(win, label = '''Own: XXXXXXX^
    Weapons: M-1, T-1, NorthStar
    Population: 500000000
    ''', pos = (200, 0), size = (1080, 150))

    wl2 = wx.Button(win, label = '''Own: XXXXXXX^
    Weapons: M-1, T-1, NorthStar
    Population: 500000000
    ''', pos = (200, 150), size = (1080, 150))

    wl3 = wx.Button(win, label = '''Own: XXXXXXX^
    Weapons: M-1, T-1, NorthStar
    Population: 500000000
    ''', pos = (200, 300), size = (1080, 150))

    wl4 = wx.Button(win, label = '''Own: XXXXXXX^
    Weapons: M-1, T-1, NorthStar
    Population: 500000000
    ''', pos = (200, 450), size = (1080, 150))
    win.Show()
    app.MainLoop()
