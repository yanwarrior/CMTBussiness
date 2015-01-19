#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1TESTERVERSION, 
] = [wx.NewId() for _init_ctrls in range(5)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(580, 269), size=wx.Size(308, 243),
              style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, title=u'About CMT')
        self.SetClientSize(wx.Size(308, 243))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(308, 243),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'CMT Alpha Tester', name='staticText1', parent=self.panel1,
              pos=wx.Point(89, 65), size=wx.Size(130, 18), style=0)
        self.staticText1.Center(wx.HORIZONTAL)
        self.staticText1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.staticText1.SetForegroundColour(wx.Colour(180, 71, 71))

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Clothing Management Tools', name='staticText2',
              parent=self.panel1, pos=wx.Point(76, 88), size=wx.Size(156, 13),
              style=0)
        self.staticText2.Center(wx.HORIZONTAL)
        self.staticText2.SetFont(wx.Font(10, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Sans'))

        self.TesterVersion = wx.StaticText(id=wxID_FRAME1TESTERVERSION,
              label=u'Tester Version', name=u'TesterVersion',
              parent=self.panel1, pos=wx.Point(119, 112), size=wx.Size(69, 12),
              style=0)
        self.TesterVersion.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.TesterVersion.Enable(True)
        self.TesterVersion.Center(wx.HORIZONTAL)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        '''
        # Ambil Logo
        file_path = "img/bisnis.png"
        img = wx.Image(file_path, wx.BITMAP_TYPE_ANY)
        self.logo.SetBitmap(wx.BitmapFromImage(img))
        '''
