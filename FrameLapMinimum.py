#Boa:Frame:Frame1
import time

import wx

from models import ModelArtikel
from misc import excelArtikelMinimum
from misc import excel_omzet
from misc import chart_omzet



def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTNCETAK, wxID_FRAME1LCLAPMIN, wxID_FRAME1PANEL1, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, wxID_FRAME1TXTPENCARIAN, 
] = [wx.NewId() for _init_ctrls in range(7)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(338, 180), size=wx.Size(833, 445),
              style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, title=u'Laporan Minimum')
        self.SetClientSize(wx.Size(833, 445))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(833, 445),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Data Laporan Minimum', name='staticText1',
              parent=self.panel1, pos=wx.Point(24, 96), size=wx.Size(126, 14),
              style=0)

        self.lcLapMin = wx.ListCtrl(id=wxID_FRAME1LCLAPMIN, name=u'lcLapMin',
              parent=self.panel1, pos=wx.Point(24, 120), size=wx.Size(784, 256),
              style=wx.LC_REPORT)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Pencarian', name='staticText2', parent=self.panel1,
              pos=wx.Point(24, 40), size=wx.Size(54, 14), style=0)

        self.txtPencarian = wx.TextCtrl(id=wxID_FRAME1TXTPENCARIAN,
              name=u'txtPencarian', parent=self.panel1, pos=wx.Point(32, 56),
              size=wx.Size(792, 24), style=wx.TE_PROCESS_ENTER, value=u'')
        self.txtPencarian.Bind(wx.EVT_TEXT_ENTER, self.OnTxtPencarianTextEnter,
              id=wxID_FRAME1TXTPENCARIAN)
        self.txtPencarian.Bind(wx.EVT_KEY_UP, self.OnTxtPencarianKeyUp)

        self.btnCetak = wx.Button(id=wxID_FRAME1BTNCETAK, label=u'Cetak',
              name=u'btnCetak', parent=self.panel1, pos=wx.Point(24, 392),
              size=wx.Size(85, 34), style=0)
        self.btnCetak.Bind(wx.EVT_BUTTON, self.OnBtnCetakButton,
              id=wxID_FRAME1BTNCETAK)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.__createColumnListCtrl()
        self.__loadDataArtikelMinimum()

#-------------------------------------------------------------------------------
# BAGIAN BUILD
#-------------------------------------------------------------------------------
    
    def __loadDataArtikelMinimum(self):
        '''load data artikel yang jumlahnya minimum'''
        model_artikel = ModelArtikel()
        data_artikel = model_artikel.readArtikelStokMin()
        if data_artikel:
            for data in data_artikel:
                jml_baris = self.lcLapMin.GetItemCount()
                # insert kode artikel
                self.lcLapMin.InsertStringItem(jml_baris,data[0])
                # insert kategori
                self.lcLapMin.SetStringItem(jml_baris, 1, data[1])
                # insert nama artikel
                self.lcLapMin.SetStringItem(jml_baris, 2, data[2])
                # insert harga
                self.lcLapMin.SetStringItem(jml_baris, 3, str(data[3]))
                # insert stok
                self.lcLapMin.SetStringItem(jml_baris, 4, str(data[4]))
                # insert stok minimum
                self.lcLapMin.SetStringItem(jml_baris, 5, str(data[5]))
                jml_baris = jml_baris + 1
                
                
    
    def __createColumnListCtrl(self):
        '''Membuat kolom list ctrl'''
        self.lcLapMin.InsertColumn(
            0, 'Kode Artikel',
            width=80)
        self.lcLapMin.InsertColumn(
            1, 'Kategori',
            width=120)
        self.lcLapMin.InsertColumn(
            2, 'Artikel',
            width=200)
        self.lcLapMin.InsertColumn(
            3, 'Harga',
            width=130)
        self.lcLapMin.InsertColumn(
            4, 'Stok',
            width=80)
        self.lcLapMin.InsertColumn(
            5, 'Stok Minimum',
            width=100)
    
    def __pencarianArtikelStokMin(self, pencarian):
        """Melakukan Pencarian Artikel di bawah stok minimum"""
        # Memanggil methode pencarian artikel
        # dengan parameter text pencarian
        model_artikel = ModelArtikel()
        hasil_cari = model_artikel.searchArtikelStokMin(pencarian)
        if hasil_cari:
            self.lcLapMin.DeleteAllItems()
            for data in hasil_cari:
                jml_baris = self.lcLapMin.GetItemCount()
                # insert kode artikel
                self.lcLapMin.InsertStringItem(jml_baris,data[0])
                # insert kategori
                self.lcLapMin.SetStringItem(jml_baris, 1, data[1])
                # insert nama artikel
                self.lcLapMin.SetStringItem(jml_baris, 2, data[2])
                # insert harga
                self.lcLapMin.SetStringItem(jml_baris, 3, str(data[3]))
                # insert stok
                self.lcLapMin.SetStringItem(jml_baris, 4, str(data[4]))
                # insert stok minimum
                self.lcLapMin.SetStringItem(jml_baris, 5, str(data[5]))
                jml_baris = jml_baris + 1
                
    def __dirDialog(self):
        """Mendapatkan direktori"""
        dialog = wx.DirDialog(self, "Choose a directory:",style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            return dialog.GetPath()
        else:
            return False
        dialog.Destroy()
#-------------------------------------------------------------------------------
# BAGIAN EVENT
#-------------------------------------------------------------------------------
    '''event load artikel saat frame baru pertama kali dibuka'''
    '''seleksi data artikel dan keluarkan isinya dalam dialog box'''
    '''export data artikel yang memiliki nilai stok di bawah minimum'''

    def OnTxtPencarianTextEnter(self, event):
        """Event untuk melakukan pencarian artikel di bawah stok minimum"""
        # Mendapatkan text pencarian
        pencarian = self.txtPencarian.GetValue()
        self.__pencarianArtikelStokMin(pencarian)

    def OnTxtPencarianKeyUp(self, event):
        """Event untuk melakukan pencarian (mengembalikan) pencarian"""
        pencarian = self.txtPencarian.GetValue()
        self.__pencarianArtikelStokMin(pencarian)

    def OnBtnCetakButton(self, event):
        """Event mencetak list ctrl data artikel dibawah stok minimum"""
        # Mengambil direktori tempat simpan file excel
        direktori = self.__dirDialog()
        if direktori:
            jml_baris = self.lcLapMin.GetItemCount()
            data_artikel = []
            for data in range(jml_baris):
                kode_artikel = self.lcLapMin.GetItem(data,0).GetText()
                kategori = self.lcLapMin.GetItem(data, 1).GetText()
                artikel = self.lcLapMin.GetItem(data, 2).GetText()
                harga = self.lcLapMin.GetItem(data, 3).GetText()
                stok = self.lcLapMin.GetItem(data, 4).GetText()
                stok_min = self.lcLapMin.GetItem(data, 5).GetText()
                data_artikel.append([
                    kode_artikel, kategori,
                    artikel, harga,
                    stok, stok_min])
            
            filename = direktori + "/LAPORAN MINIMUM "+str(time.strftime("%d-%m-%Y %H%M%S")) + ".xls"
            sheet_name = str(time.strftime("%d%m%Y-%H%M%S"))
            excel = excelArtikelMinimum(filename, sheet_name, data_artikel)
            
            if excel:
                pesan = wx.MessageDialog(
                    self, "Berhasil Export Data Laporan Minimum",
                    'Pesan Sukses', wx.OK
                    )
                pesan.ShowModal()
            else:
                pesan = wx.MessageDialog(
                    self, "Gagal Export Data Laporan Minimum",
                    'Pesan Kesalahan', wx.ICON_ERROR
                    )
                pesan.ShowModal()
            
        else:
            pass
        
