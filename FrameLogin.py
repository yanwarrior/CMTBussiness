#Boa:Frame:Frame1

import wx
import MySQLdb

import FrameUtama


database = MySQLdb.connect(
        'localhost', 'root',
        'junox', 'penjualan')               # Create Connection   
                       
cursor = database.cursor()                  # Create Cursor Object 

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTNLOGIN, wxID_FRAME1PANEL1, wxID_FRAME1PNGGAMBAR, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, wxID_FRAME1TXTKATASANDI, 
 wxID_FRAME1TXTKODEPENGGUNA, 
] = [wx.NewId() for _init_ctrls in range(8)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(739, 304), size=wx.Size(277, 268),
              style=  wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, title=u'Login eLocker')
        self.SetClientSize(wx.Size(277, 268))
        self.Center(wx.BOTH)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(277, 268),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Kode Pengguna', name='staticText1', parent=self.panel1,
              pos=wx.Point(32, 96), size=wx.Size(87, 14), style=0)

        self.txtKodePengguna = wx.TextCtrl(id=wxID_FRAME1TXTKODEPENGGUNA,
              name=u'txtKodePengguna', parent=self.panel1, pos=wx.Point(32,
              112), size=wx.Size(216, 24), style=0, value=u'')
        self.txtKodePengguna.Bind(wx.EVT_TEXT, self.OnTxtKodePenggunaText,
              id=wxID_FRAME1TXTKODEPENGGUNA)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Kata Sandi', name='staticText2', parent=self.panel1,
              pos=wx.Point(32, 144), size=wx.Size(57, 14), style=0)

        self.txtKataSandi = wx.TextCtrl(id=wxID_FRAME1TXTKATASANDI,
              name=u'txtKataSandi', parent=self.panel1, pos=wx.Point(32, 160),
              size=wx.Size(216, 24), style=wx.TE_PASSWORD, value=u'')

        self.btnLogin = wx.Button(id=wxID_FRAME1BTNLOGIN, label=u'Login',
              name=u'btnLogin', parent=self.panel1, pos=wx.Point(32, 208),
              size=wx.Size(85, 34), style=0)
        self.btnLogin.Bind(wx.EVT_BUTTON, self.OnClickLogin,
              id=wxID_FRAME1BTNLOGIN)

        self.pngGambar = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_FRAME1PNGGAMBAR, name=u'pngGambar', parent=self.panel1,
              pos=wx.Point(104, 24), size=wx.Size(64, 64), style=0)
        self.pngGambar.SetLabel(u'')

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        # set focus to self.txtKodePengguna
        self.txtKodePengguna.SetFocus()
        
        # set image gambar tampilan depan
        gambar  = 'img/login.png'
        img     = wx.Image(gambar, wx.BITMAP_TYPE_ANY)
        self.pngGambar.SetBitmap(wx.BitmapFromImage(img))
        

    def OnClickLogin(self, event):
        """event klik tombol self.btnLogin untuk proses login"""
        username = self.txtKodePengguna.GetValue()
        password = self.txtKataSandi.GetValue()
        # Memeriksa username dan password pengguna yang login
        sql = """SELECT * 
                 FROM Pengguna 
                 WHERE email = '%s'
                 AND kata_sandi = '%s'""" % (username, password)
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            if not result:
                message = "Maaf, Login gagal ! coba kembali..."
                pop_up = wx.MessageDialog(
                        self, message, 
                        "Notifikasi", wx.ICON_ERROR)
                pop_up.ShowModal()
            else:
                message = "Login Berhasil"
                pop_up = wx.MessageDialog(
                        self, message, 
                        "Notifikasi", wx.OK) 
                sql = """
                    UPDATE 
                """  
                pop_up.ShowModal()
                # Call Frame utama
                frame_utama = FrameUtama.create(None)
                frame_utama.Show(True)
                # destroy this frame login
                self.Destroy()
        except:
            message = "Terjadi kesalahan saat Login, hubungi Developer."
            pop_up = wx.MessageDialog(self, message, 
                                      "Notifikasi", wx.ICON_WARNING)
            pop_up.ShowModal()
       
            

    def OnTxtKodePenggunaText(self, event):
        # event mengubah huruf menjadi besar (uppercase)
        pass
        ''''
        event.Skip()
        selection   = self.txtKodePengguna.GetSelection()
        value       = self.txtKodePengguna.GetValue().upper()
        self.txtKodePengguna.ChangeValue(value)
        self.txtKodePengguna.SetSelection(*selection)
		'''
