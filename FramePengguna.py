#Boa:Frame:Frame1

import wx

from models import ModelPengguna

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTNBATAL, wxID_FRAME1BTNUBAH, wxID_FRAME1PANEL1, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, wxID_FRAME1TXTKODEID, 
 wxID_FRAME1TXTKODEPENGGUNA, wxID_FRAME1TXTUSERNAME, 
] = [wx.NewId() for _init_ctrls in range(9)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(582, 164), size=wx.Size(263, 282),
              style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, title=u'Pengguna')
        self.SetClientSize(wx.Size(263, 282))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(263, 282),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Username', name='staticText1', parent=self.panel1,
              pos=wx.Point(24, 112), size=wx.Size(152, 16), style=0)

        self.txtUsername = wx.TextCtrl(id=wxID_FRAME1TXTUSERNAME,
              name=u'txtUsername', parent=self.panel1, pos=wx.Point(24, 128),
              size=wx.Size(208, 24), style=0, value=u'')

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Password', name='staticText2', parent=self.panel1,
              pos=wx.Point(24, 160), size=wx.Size(88, 16), style=0)

        self.txtKodePengguna = wx.TextCtrl(id=wxID_FRAME1TXTKODEPENGGUNA,
              name=u'txtKodePengguna', parent=self.panel1, pos=wx.Point(24,
              176), size=wx.Size(208, 24), style=0, value=u'')

        self.btnUbah = wx.Button(id=wxID_FRAME1BTNUBAH, label=u'Ubah',
              name=u'btnUbah', parent=self.panel1, pos=wx.Point(104, 208),
              size=wx.Size(64, 32), style=0)
        self.btnUbah.Bind(wx.EVT_BUTTON, self.OnBtnUbahButton,
              id=wxID_FRAME1BTNUBAH)

        self.btnBatal = wx.Button(id=wxID_FRAME1BTNBATAL, label=u'Batal',
              name=u'btnBatal', parent=self.panel1, pos=wx.Point(176, 208),
              size=wx.Size(56, 34), style=0)

        self.txtKodeId = wx.TextCtrl(id=wxID_FRAME1TXTKODEID, name=u'txtKodeId',
              parent=self.panel1, pos=wx.Point(24, 64), size=wx.Size(208, 34),
              style=0, value=u'')
        self.txtKodeId.SetEditable(True)
        self.txtKodeId.Enable(False)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.__loadDataPengguna()
        
    def __loadDataPengguna(self):
        """Load data pengguna pertama kali"""
        # Mendapatkan username dan password pengguna
        model_pengguna = ModelPengguna()
        data_pengguna = model_pengguna.readPengguna()
        # Tampilkan ke layar frame
        self.txtKodeId.SetValue(str(data_pengguna[0]))
        self.txtKodePengguna.SetValue(str(data_pengguna[2]))
        self.txtUsername.SetValue(str(data_pengguna[1]))

    def OnBtnUbahButton(self, event):
        """mengubah data pengguna"""
        model_pengguna = ModelPengguna()
        email = self.txtUsername.GetValue()
        password = self.txtKodePengguna.GetValue()
        kode_pengguna = self.txtKodeId.GetValue()
        hasil_update = model_pengguna.updatePengguna(email, password, kode_pengguna)
        if hasil_update:
            pesan = wx.MessageDialog(
                self, 'Pengubahan data pengguna berhasil',
                'Pesan Sukses', wx.OK
                )
            pesan.ShowModal()
        else:
            pesan = wx.MessageDialog(
                self, 'Pengubahan data pengguna gagal dilakukan',
                'Pesan Kesalahan', wx.ICON_ERROR
                )
            pesan.ShowModal()
            
