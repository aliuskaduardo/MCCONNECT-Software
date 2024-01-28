# display a graph image in a Scrolled Windows

import wx

class MyScrolledWindow(wx.Frame): # for networks
    def __init__(self, parent, id, title, sFig):
        wx.Frame.__init__(self, parent, id, title, size=(710, 760))
        sw = wx.ScrolledWindow(self)
        bmp = wx.Image(sFig,wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(sw, -1, bmp)
        wx.StaticText(sw, -1, '* You can find PNG pictures, DOT files and the plotting executables inside \"dot\" folder', (5, 680))
        sw.SetScrollbars(20, 20, 55, 40)

class MyScrolledWindow2(wx.Frame): # for centralities / TIs
    def __init__(self, parent, id, title, sFig):
        wx.Frame.__init__(self, parent, id, title, size=(690, 530))
        sw = wx.ScrolledWindow(self)
        bmp = wx.Image(sFig,wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(sw, -1, bmp)
        wx.StaticText(sw, -1, '* You can find PNG pictures, DOT files and the plotting executables inside \"dot\" folder', (5, 680))
        #sw.SetScrollbars(20, 20, 55, 40)
        
