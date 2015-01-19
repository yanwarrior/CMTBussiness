#!/usr/bin/env python
#Boa:App:BoaApp

import wx
import FrameLogin

modules ={u'FrameAbout': [0, '', u'FrameAbout.py'],
 u'FrameBantuan': [0, '', u'FrameBantuan.py'],
 u'FrameDataArtikel': [0, '', u'FrameDataArtikel.py'],
 u'FrameDataKategori': [0, '', u'FrameDataKategori.py'],
 u'FrameDataPelanggan': [0, '', u'FrameDataPelanggan.py'],
 u'FrameLapMinimum': [0, '', u'FrameLapMinimum.py'],
 u'FrameLapOmzet': [0, '', u'FrameLapOmzet.py'],
 u'FrameLogin': [1, 'Main frame of Application', u'FrameLogin.py'],
 u'FramePengguna': [0, '', u'FramePengguna.py'],
 u'FramePenjualan': [0, '', u'FramePenjualan.py'],
 u'dbconfig': [0, '', u'engine/dbconfig.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = FrameLogin.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
