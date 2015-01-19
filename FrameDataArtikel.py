#Boa:Frame:Frame1

import wx
import wx.lib.buttons
import MySQLdb

from models import ModelArtikel
from models import ModelKategori
from models import ModelStokUkuran
from misc import random_key

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTNBATAL, wxID_FRAME1BTNHAPUS, wxID_FRAME1BTNRANDOM, 
 wxID_FRAME1BTNREFRESH, wxID_FRAME1BTNSIMPAN, wxID_FRAME1BTNUBAH, 
 wxID_FRAME1CMBKODEKATEGORI, wxID_FRAME1LBLKATEGORI, wxID_FRAME1LCDATAARTIKEL, 
 wxID_FRAME1PANEL1, wxID_FRAME1SPINL32, wxID_FRAME1SPINM30, 
 wxID_FRAME1SPINS28, wxID_FRAME1SPINXL34, wxID_FRAME1SPINXXL36, 
 wxID_FRAME1SPINXXXL38, wxID_FRAME1SPIN_MIN, wxID_FRAME1STATICBOX1, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT10, wxID_FRAME1STATICTEXT11, 
 wxID_FRAME1STATICTEXT12, wxID_FRAME1STATICTEXT13, wxID_FRAME1STATICTEXT14, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, 
 wxID_FRAME1STATICTEXT5, wxID_FRAME1STATICTEXT6, wxID_FRAME1STATICTEXT7, 
 wxID_FRAME1STATICTEXT8, wxID_FRAME1STATICTEXT9, wxID_FRAME1TXTKODEARTIKEL, 
 wxID_FRAME1TXTPENCARIAN, wxID_FRAME1TXTTOTALSTOK, wxID_FRAME1TXT_HARGA_JUAL, 
 wxID_FRAME1TXT_HARGA_MODAL, wxID_FRAME1TXT_NAMA_ARTIKEL, 
] = [wx.NewId() for _init_ctrls in range(39)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(286, 137), size=wx.Size(1078, 605),
              style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, title=u'Data Artikel - Produk')
        self.SetClientSize(wx.Size(1078, 605))
        self.Center(wx.BOTH)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(1078, 605),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Kode Artikel', name='staticText1', parent=self.panel1,
              pos=wx.Point(24, 24), size=wx.Size(69, 14), style=0)

        self.txtKodeArtikel = wx.TextCtrl(id=wxID_FRAME1TXTKODEARTIKEL,
              name=u'txtKodeArtikel', parent=self.panel1, pos=wx.Point(24, 40),
              size=wx.Size(168, 24), style=0, value=u'')

        self.btnRandom = wx.Button(id=wxID_FRAME1BTNRANDOM, label=u'Random',
              name=u'btnRandom', parent=self.panel1, pos=wx.Point(200, 38),
              size=wx.Size(64, 26), style=0)
        self.btnRandom.Bind(wx.EVT_BUTTON, self.OnBtnRandomButton,
              id=wxID_FRAME1BTNRANDOM)

        self.cmbKodeKategori = wx.ComboBox(choices=['Pilih Kode Kategori...'],
              id=wxID_FRAME1CMBKODEKATEGORI, name=u'cmbKodeKategori',
              parent=self.panel1, pos=wx.Point(24, 136), size=wx.Size(240, 27),
              style=0, value=u'')
        self.cmbKodeKategori.SetLabel(u'')
        self.cmbKodeKategori.Bind(wx.EVT_COMBOBOX,
              self.OnCmbKodeKategoriCombobox, id=wxID_FRAME1CMBKODEKATEGORI)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Kode Kategori : ', name='staticText2', parent=self.panel1,
              pos=wx.Point(24, 120), size=wx.Size(88, 14), style=0)

        self.lblKategori = wx.StaticText(id=wxID_FRAME1LBLKATEGORI, label=u'',
              name=u'lblKategori', parent=self.panel1, pos=wx.Point(112, 120),
              size=wx.Size(54, 14), style=0)
        self.lblKategori.SetBackgroundColour(wx.Colour(62, 149, 224))

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Stok Ukuran ', name='staticBox1', parent=self.panel1,
              pos=wx.Point(24, 176), size=wx.Size(240, 248), style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'S / 28', name='staticText4', parent=self.panel1,
              pos=wx.Point(48, 200), size=wx.Size(32, 14), style=0)

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'M / 30', name='staticText5', parent=self.panel1,
              pos=wx.Point(48, 240), size=wx.Size(36, 14), style=0)

        self.spinS28 = wx.SpinCtrl(id=wxID_FRAME1SPINS28, initial=0, max=100,
              min=0, name=u'spinS28', parent=self.panel1, pos=wx.Point(48, 216),
              size=wx.Size(72, 24), style=wx.SP_ARROW_KEYS)
        self.spinS28.Bind(wx.EVT_SPIN, self.OnSpinS28Spin,
              id=wxID_FRAME1SPINS28)

        self.spinM30 = wx.SpinCtrl(id=wxID_FRAME1SPINM30, initial=0, max=100,
              min=0, name=u'spinM30', parent=self.panel1, pos=wx.Point(48, 256),
              size=wx.Size(72, 24), style=wx.SP_ARROW_KEYS)

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label=u'L  / 32', name='staticText6', parent=self.panel1,
              pos=wx.Point(48, 280), size=wx.Size(35, 14), style=0)

        self.spinL32 = wx.SpinCtrl(id=wxID_FRAME1SPINL32, initial=0, max=100,
              min=0, name=u'spinL32', parent=self.panel1, pos=wx.Point(48, 296),
              size=wx.Size(72, 24), style=wx.SP_ARROW_KEYS)

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label=u'XL / 34', name='staticText7', parent=self.panel1,
              pos=wx.Point(144, 200), size=wx.Size(39, 14), style=0)

        self.spinXL34 = wx.SpinCtrl(id=wxID_FRAME1SPINXL34, initial=0, max=100,
              min=0, name=u'spinXL34', parent=self.panel1, pos=wx.Point(144,
              216), size=wx.Size(80, 24), style=wx.SP_ARROW_KEYS)

        self.staticText8 = wx.StaticText(id=wxID_FRAME1STATICTEXT8,
              label=u'XXL / 36', name='staticText8', parent=self.panel1,
              pos=wx.Point(144, 240), size=wx.Size(46, 14), style=0)

        self.spinXXL36 = wx.SpinCtrl(id=wxID_FRAME1SPINXXL36, initial=0,
              max=100, min=0, name=u'spinXXL36', parent=self.panel1,
              pos=wx.Point(144, 256), size=wx.Size(80, 24),
              style=wx.SP_ARROW_KEYS)

        self.staticText9 = wx.StaticText(id=wxID_FRAME1STATICTEXT9,
              label=u'XXXL / 38', name='staticText9', parent=self.panel1,
              pos=wx.Point(144, 280), size=wx.Size(53, 14), style=0)

        self.spinXXXL38 = wx.SpinCtrl(id=wxID_FRAME1SPINXXXL38, initial=0,
              max=100, min=0, name=u'spinXXXL38', parent=self.panel1,
              pos=wx.Point(144, 296), size=wx.Size(80, 24),
              style=wx.SP_ARROW_KEYS)

        self.staticText10 = wx.StaticText(id=wxID_FRAME1STATICTEXT10,
              label=u'Stok Ukuran : ', name='staticText10', parent=self.panel1,
              pos=wx.Point(48, 336), size=wx.Size(76, 14), style=0)

        self.staticText11 = wx.StaticText(id=wxID_FRAME1STATICTEXT11,
              label=u'Pencarian', name='staticText11', parent=self.panel1,
              pos=wx.Point(304, 24), size=wx.Size(54, 14), style=0)

        self.txtPencarian = wx.TextCtrl(id=wxID_FRAME1TXTPENCARIAN,
              name=u'txtPencarian', parent=self.panel1, pos=wx.Point(304, 40),
              size=wx.Size(728, 24), style=wx.TE_PROCESS_ENTER, value=u'')
        self.txtPencarian.Bind(wx.EVT_TEXT_ENTER, self.OnTxtPencarianTextEnter,
              id=wxID_FRAME1TXTPENCARIAN)
        self.txtPencarian.Bind(wx.EVT_KEY_UP, self.OnTxtPencarianKeyUp)

        self.lcDataArtikel = wx.ListCtrl(id=wxID_FRAME1LCDATAARTIKEL,
              name=u'lcDataArtikel', parent=self.panel1, pos=wx.Point(304, 80),
              size=wx.Size(728, 496), style=wx.LC_REPORT)
        self.lcDataArtikel.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnLcDataArtikelListItemSelected,
              id=wxID_FRAME1LCDATAARTIKEL)

        self.btnSimpan = wx.Button(id=wxID_FRAME1BTNSIMPAN, label=u'Simpan',
              name=u'btnSimpan', parent=self.panel1, pos=wx.Point(24, 536),
              size=wx.Size(60, 40), style=0)
        self.btnSimpan.Bind(wx.EVT_BUTTON, self.OnBtnSimpanButton,
              id=wxID_FRAME1BTNSIMPAN)

        self.btnHapus = wx.Button(id=wxID_FRAME1BTNHAPUS, label=u'Hapus',
              name=u'btnHapus', parent=self.panel1, pos=wx.Point(152, 536),
              size=wx.Size(50, 40), style=0)
        self.btnHapus.Bind(wx.EVT_BUTTON, self.OnBtnHapusButton,
              id=wxID_FRAME1BTNHAPUS)

        self.btnBatal = wx.Button(id=wxID_FRAME1BTNBATAL, label=u'Batal',
              name=u'btnBatal', parent=self.panel1, pos=wx.Point(208, 536),
              size=wx.Size(56, 40), style=0)
        self.btnBatal.Bind(wx.EVT_BUTTON, self.OnBtnBatalButton,
              id=wxID_FRAME1BTNBATAL)

        self.btnRefresh = wx.lib.buttons.GenBitmapButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1BTNREFRESH, name=u'btnRefresh', parent=self.panel1,
              pos=wx.Point(200, 328), size=wx.Size(24, 24),
              style=wx.TRANSPARENT_WINDOW | wx.NO_BORDER | wx.NO_3D)
        self.btnRefresh.SetBitmapDisabled(wx.Bitmap(u'img/refresh.png',
              wx.BITMAP_TYPE_PNG))
        self.btnRefresh.SetBitmapFocus(wx.Bitmap(u'img/refresh.png',
              wx.BITMAP_TYPE_PNG))
        self.btnRefresh.SetBitmapSelected(wx.Bitmap(u'img/refresh.png',
              wx.BITMAP_TYPE_PNG))
        self.btnRefresh.SetToolTipString(u'refresh')
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.OnBtnRefreshButton,
              id=wxID_FRAME1BTNREFRESH)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Harga Modal', name='staticText3', parent=self.panel1,
              pos=wx.Point(24, 432), size=wx.Size(68, 14), style=0)

        self.txt_harga_modal = wx.TextCtrl(id=wxID_FRAME1TXT_HARGA_MODAL,
              name=u'txt_harga_modal', parent=self.panel1, pos=wx.Point(24,
              448), size=wx.Size(240, 24), style=0, value=u'')
        self.txt_harga_modal.Bind(wx.EVT_CHAR, self.OnTxt_harga_modalChar)

        self.staticText12 = wx.StaticText(id=wxID_FRAME1STATICTEXT12,
              label=u'Harga Jual', name='staticText12', parent=self.panel1,
              pos=wx.Point(24, 480), size=wx.Size(57, 14), style=0)

        self.txt_harga_jual = wx.TextCtrl(id=wxID_FRAME1TXT_HARGA_JUAL,
              name=u'txt_harga_jual', parent=self.panel1, pos=wx.Point(24, 496),
              size=wx.Size(240, 24), style=0, value=u'')
        self.txt_harga_jual.Bind(wx.EVT_CHAR, self.OnTxt_harga_jualChar)

        self.staticText13 = wx.StaticText(id=wxID_FRAME1STATICTEXT13,
              label=u'Nama Artikel', name='staticText13', parent=self.panel1,
              pos=wx.Point(24, 72), size=wx.Size(71, 14), style=0)

        self.txt_nama_artikel = wx.TextCtrl(id=wxID_FRAME1TXT_NAMA_ARTIKEL,
              name=u'txt_nama_artikel', parent=self.panel1, pos=wx.Point(24,
              88), size=wx.Size(240, 24), style=0, value=u'')

        self.staticText14 = wx.StaticText(id=wxID_FRAME1STATICTEXT14,
              label=u'Stok Minimum Artikel : ', name='staticText14',
              parent=self.panel1, pos=wx.Point(48, 368), size=wx.Size(126, 14),
              style=0)

        self.spin_min = wx.SpinCtrl(id=wxID_FRAME1SPIN_MIN, initial=0, max=100,
              min=0, name=u'spin_min', parent=self.panel1, pos=wx.Point(176,
              360), size=wx.Size(48, 24), style=wx.SP_ARROW_KEYS)

        self.txtTotalStok = wx.TextCtrl(id=wxID_FRAME1TXTTOTALSTOK,
              name=u'txtTotalStok', parent=self.panel1, pos=wx.Point(144, 328),
              size=wx.Size(48, 24), style=0, value=u'0')

        self.btnUbah = wx.Button(id=wxID_FRAME1BTNUBAH, label=u'Ubah',
              name=u'btnUbah', parent=self.panel1, pos=wx.Point(88, 536),
              size=wx.Size(56, 40), style=0)
        self.btnUbah.Bind(wx.EVT_BUTTON, self.OnBtnUbahButton,
              id=wxID_FRAME1BTNUBAH)

    def __init__(self, parent):
        self._init_ctrls(parent)
        # Mendisable beberapa Button
        self.txtKodeArtikel.Disable()
        self.btnHapus.Disable()
        self.btnBatal.Disable()
        self.btnUbah.Disable()
        # Menambahkan column lcDataArtikel ListCtrl
        self.__addColumnArtikelToListCtrl()
        # Meload data Artikel ke List Ctrl
        self.__loadDataArtikelToListCtrl()
        # Meload data Kategori ke Combo Box
        self.__loadDataKategoriToComboBox()
    
    
#-------------------------------------------------------------------------------
# BAGIAN BUILD
#-------------------------------------------------------------------------------

    def __loadDataKategoriToComboBox(self):
        """Meload data Kategori ke Combo Box"""
        self.cmbKodeKategori.SetStringSelection("Pilih Kode Kategori...")
        model_kategori = ModelKategori()
        results = model_kategori.readKategori()
        for kode_kategori in results:
            self.cmbKodeKategori.Append(str(kode_kategori[0]))
    
    def __addColumnArtikelToListCtrl(self): 
        """Menambahkan kolom header List Ctrl"""
        self.lcDataArtikel.InsertColumn(
            0, 'Kode', 
            width=70)
        self.lcDataArtikel.InsertColumn(
            1, 'Kategori', 
            width=70)
        self.lcDataArtikel.InsertColumn(
            2, 'Stok', 
            wx.LIST_FORMAT_CENTRE, width=40
            )              
        self.lcDataArtikel.InsertColumn(
            3, 'Artikel', 
            wx.LIST_FORMAT_LEFT, width=230
            )               
        self.lcDataArtikel.InsertColumn(
            4, 'Harga',
            wx.LIST_FORMAT_RIGHT, width=200
            )  
        self.lcDataArtikel.InsertColumn(
            5, 'Stok Minimum',
            wx.LIST_FORMAT_CENTRE, width=130)   
    
    def __loadDataArtikelToListCtrl(self):
        """Meload data Artikel ke List Ctrl"""
        self.lcDataArtikel.DeleteAllItems()
        model_artikel = ModelArtikel()
        results = model_artikel.readArtikel()
            
        for artikel in results:
            jml_baris = self.lcDataArtikel.GetItemCount()
            self.lcDataArtikel.InsertStringItem(jml_baris, str(artikel[0]))
            self.lcDataArtikel.SetStringItem(jml_baris, 1, str(artikel[1]))
            self.lcDataArtikel.SetStringItem(jml_baris, 2, str(artikel[2]))
            self.lcDataArtikel.SetStringItem(jml_baris, 3, str(artikel[3]))
            self.lcDataArtikel.SetStringItem(jml_baris, 4, str(artikel[4]))
            self.lcDataArtikel.SetStringItem(jml_baris, 5, str(artikel[5]))
            
            if jml_baris % 2:
                self.lcDataArtikel.SetItemBackgroundColour(jml_baris, "#D7DEE6")
            elif int(artikel[2]) <= int(artikel[5]):
                self.lcDataArtikel.SetItemBackgroundColour(jml_baris, "#FFB870")
            else:
                self.lcDataArtikel.SetItemBackgroundColour(jml_baris, "#66CCFF")
            
            jml_baris = jml_baris + 1
    
    def __getDataUkuran(self):
        """Mendapatkan data Ukuran"""
        ukuran = self.spinS28.GetValue() + self.spinM30.GetValue() + \
        self.spinL32.GetValue() + self.spinXL34.GetValue() + \
        self.spinXXL36.GetValue() + self.spinXXXL38.GetValue()
        self.txtTotalStok.SetValue(str(ukuran))
                
    def __bersih(self):
        """Membersihkan element pada frame Artikel"""
        self.txtKodeArtikel.SetValue("")
        self.txt_nama_artikel.SetValue("")
        self.cmbKodeKategori.SetStringSelection("Pilih Kode Kategori...")
        self.spinL32.SetValue(0)
        self.spinM30.SetValue(0)
        self.spinS28.SetValue(0)
        self.spinXL34.SetValue(0)
        self.spinXXL36.SetValue(0)
        self.spinXXXL38.SetValue(0)
        self.spin_min.SetValue(0)
        self.txtTotalStok.SetValue("0")
        self.txt_harga_jual.SetValue("")
        self.txt_harga_modal.SetValue("")
    
    def __validasiSimpan(self):
        """Memvalidasi sebelum menyimpan Artikel ke database"""
        pesan = ""
        # check nama artikel
        if not self.txt_nama_artikel.GetValue():
            pesan = pesan + "\tNama Artikel harus diisi !\n"
        # check kode artikel
        if not self.txtKodeArtikel.GetValue():
            pesan = pesan + "\tKode Artikel harus diisi !\n"
        # check kode kategori
        if not self.cmbKodeKategori.GetStringSelection():
            pesan = pesan + "\tKode Kategori harus di pilih !\n"
        if self.cmbKodeKategori.GetStringSelection() == "Pilih Kode Kategori..." or\
         self.cmbKodeKategori.GetValue() == "Pilih Kode Kategori...":
            pesan = pesan + "\tKode Kategori tidak valid\n"
        # check jumlah total stok
        if not self.txtTotalStok.GetValue() and \
            len(self.txtTotalStok.GetValue()) == '0':
            pesan = pesan + "\tTotal Stok harus diisi !\n"
        # check harga modal
        if not self.txt_harga_modal.GetValue():
            pesan = pesan + "\tHarga Modal harus diisi !\n"
        # check harga jual
        if not self.txt_harga_jual.GetValue():
            pesan = pesan + "\tHarga Jual harus diisi !\n"
        # check stok minimum
        if not str(self.spin_min.GetValue()) and \
            str(self.spin_min.GetValue()) == '0':
            pesan = pesan + "\tStok Minimum Harus diisi !\n"
        
        return pesan
    

#-------------------------------------------------------------------------------
# BAGIAN EVENT
#-------------------------------------------------------------------------------
    def OnSpinS28Spin(self, event):
        """Event spin Ukuran S 28"""
        self.__getDataUkuran()
    
    def OnBtnRandomButton(self, event):
        """Event menggenerate kode Artikel"""
        key_random = random_key("ART",4)
        self.txtKodeArtikel.SetValue(key_random)
    
    def onSeleksiLcDataArtikel(self, event):
        """Event menyeleksi data Artikel di List Ctrl"""
    
    def OnTxt_harga_modalChar(self, event):
        """Only numeric"""
        keycode = event.GetKeyCode()
        if keycode < 255:
            # valid ASCII
            if chr(keycode).isdigit() or keycode == 8:
                # Valid alphanumeric character
                event.Skip()
    
    def OnTxt_harga_jualChar(self, event):
        """Only numeric"""
        keycode = event.GetKeyCode()
        if keycode < 255:
            # valid ASCII
            if chr(keycode).isdigit() or keycode == 8:
                # Valid alphanumeric character
                event.Skip()
    
    def OnBtnRefreshButton(self, event):
        """Event merefresh data ukuran"""
        self.__getDataUkuran()
    
    def OnBtnBatalButton(self, event):
        """Event membersihkan data Artikel di layar"""
        self.__bersih()
        self.btnHapus.Disable()
        self.btnUbah.Disable()
        self.btnSimpan.Enable()
        self.btnRandom.Enable()
        self.btnBatal.Disable()

    def OnBtnHapusButton(self, event):
        """Event menghapus data Artikel"""
        # Mengecek dan Mendapatkan Kode Artikel
        kode_artikel = ""
        if self.txtKodeArtikel.GetValue():
            kode_artikel = self.txtKodeArtikel.GetValue()
        else:
            # Menampilkan notifikasi Kode Artikel kosong
            pesan = wx.MessageDialog(
                self, 'Untuk melakukan proses ini, Kode Artikel tidak boleh kosong !',
                'Pesan Peringatan', wx.ICON_WARNING
                )
            pesan.ShowModal()
        
        pesan = wx.MessageDialog(
            self, "Anda yakin ingin menghapus Artikel ini ?",
            "Konfirmasi Pengguna", wx.YES_NO
            )
        hasil_pesan = pesan.ShowModal()
        
        if hasil_pesan == wx.ID_YES:
            try:
                # Menghapus Artikel
                model_artikel = ModelArtikel()
                result_artikel = model_artikel.deleteArtikel(kode_artikel)
                model_stok_ukuran = ModelStokUkuran()
                
                # Menghapus Stok Ukuran berdasarkan kode artikel
                result_stok_ukuran = model_stok_ukuran.deleteStokUkuran(kode_artikel)
                
                if result_artikel and result_stok_ukuran:
                    pesan = wx.MessageDialog(
                        self, 'Artikel berhasil dihapus',
                        'Pesan Berhasil', wx.OK
                    )
                    pesan.ShowModal()
                    
                    # Reload data List Ctrl
                    self.__loadDataArtikelToListCtrl()
                    self.__bersih()
                    self.btnBatal.Disable()
                    self.btnHapus.Disable()
                    self.btnUbah.Disable()
                    self.btnSimpan.Enable()
                    self.btnRandom.Enable()
                    
                else:
                    # Gagal menghapus Artikel
                    pesan = wx.MessageDialog(
                        self, 'Artikel tidak berhasil dihapus',
                        'Pesan Kesalahan', wx.ICON_ERROR
                        )
                    pesan.ShowModal()
            except:
                # Kesalahan menghapus Artikel
                pesan = wx.MessageDialog(
                    self, 'Terjadi kesalahan saat menghapus Artikel',
                    'Pesan Kesalahan', wx.ICON_ERROR
                    )
                pesan.ShowModal()
        

    def OnBtnUbahButton(self, event):
        """Event mengubah data Artikel"""
        # Memvalidasi
        validasi = self.__validasiSimpan()
        if validasi:
            pesan = wx.MessageDialog(
                self, validasi,
                'Pesan Kesalahan', wx.ICON_ERROR
                )
            pesan.ShowModal()
        else:
            
            # Mendapatkan Kode Artikel
            kode_artikel = self.txtKodeArtikel.GetValue()
            # Mendapatkan data-data perubahan untuk Artikel
            kode_kategori = self.cmbKodeKategori.GetStringSelection()
            nama_artikel = self.txt_nama_artikel.GetValue()
            harga_modal = self.txt_harga_modal.GetValue()
            harga_jual = self.txt_harga_jual.GetValue()
            stok_minimum = str(self.spin_min.GetValue())
            
            # Mendapatkan data-data perubahan untuk Stok Ukuran
            s28 = self.spinS28.GetValue()
            m30 = self.spinM30.GetValue()
            l32 = self.spinL32.GetValue()
            xl34 = self.spinXL34.GetValue()
            xxl36 = self.spinXXL36.GetValue()
            xxxl38 = self.spinXXXL38.GetValue()
            total_stok = s28 + m30 + l32 + xl34 + xxl36 + xxxl38
            
            # Mengubah data Artikel
            model_artikel = ModelArtikel()
            hasil_model_artikel = model_artikel.updateArtikel(
                kode_artikel, kode_kategori,
                nama_artikel, harga_modal,
                harga_jual, stok_minimum
                )
            
            # Mengubah data Stok Ukuran
            model_stok_ukuran = ModelStokUkuran()
            hasil_model_stok_ukuran = model_stok_ukuran.updateStokUkuran(
                kode_artikel, str(s28),
                str(m30), str(l32),
                str(xl34), str(xxl36),
                str(xxxl38), str(total_stok)
                )
            
            # Pemeriksaan hasil pengubahan
            if model_artikel and model_stok_ukuran:
                pesan = wx.MessageDialog(
                    self, 'Perubahan berhasil dilakukan !',
                    'Pesan Perubahan', wx.ICON_INFORMATION
                    )
                pesan.ShowModal()
            else:
                pesan = wx.MessageDialog(
                    self, 'Perubahan tidak berhasil dilakukan !',
                    'Pesan Kesalahan', wx.ICON_ERROR
                    )
                pesan.ShowModal()
            
            self.__loadDataArtikelToListCtrl()
            self.__bersih()
        
    
    def OnCmbKodeKategoriCombobox(self, event):
        """Event memilih Kode Kategori"""
        kode_kategori = self.cmbKodeKategori.GetStringSelection()
        model_kategori = ModelKategori()
        result = model_kategori.readNamaKategori(kode_kategori)
        if result:
            self.lblKategori.SetLabel(result[0])
        else:
            self.lblKategori.SetLabel("")
        
    def OnBtnSimpanButton(self, event):
        """Event Menyimpan data Artikel"""
        pesan_error = self.__validasiSimpan()
        
        if pesan_error:
            pesan = wx.MessageDialog(
                self, pesan_error,
                'Pesan Peringatan', wx.ICON_WARNING
                )
            pesan.ShowModal()
        else:
            kode_artikel = self.txtKodeArtikel.GetValue()
            kode_kategori = self.cmbKodeKategori.GetStringSelection()
            nama_artikel = self.txt_nama_artikel.GetValue()
            harga_modal = int(self.txt_harga_modal.GetValue())
            harga_jual = int(self.txt_harga_jual.GetValue())
            stok_minimum = self.spin_min.GetValue()
            
            s = self.spinS28.GetValue()
            m = self.spinM30.GetValue()
            l = self.spinL32.GetValue()
            xl = self.spinXL34.GetValue()
            xxl = self.spinXXL36.GetValue()
            xxxl = self.spinXXXL38.GetValue()
            total_stok = s + m + l + xl + xxl + xxxl
            
            
            # Create data Artikel
            data_artikel = (
                kode_artikel, kode_kategori, nama_artikel, 
                str(harga_modal), str(harga_jual), str(stok_minimum)
                )
            model_artikel = ModelArtikel()
            result_artikel = model_artikel.createArtikel(data_artikel)
            if result_artikel:
                # Create data Stok Ukuran
                data_stok_ukuran = (
                    kode_artikel, str(s), str(m), 
                    str(l), str(xl), str(xxl), 
                    str(xxxl), str(total_stok))
                model_stok_ukuran = ModelStokUkuran()
                result_stok_ukuran = model_stok_ukuran.createStokUkuran(data_stok_ukuran)
                if result_stok_ukuran:
                    # Membersihkan Element
                    self.__bersih()
                    # Mengisi kembalo data Artikel ke List Ctrl
                    self.__loadDataArtikelToListCtrl()
                    # Menampilkan pesan berhasil
                    pesan = wx.MessageDialog(
                        self, 'Penyimpanan Artikel berhasil !',
                        'Pesan Berhasil', wx.OK
                        ) 
                    pesan.ShowModal()
                else:
                    pesan = wx.MessageDialog(
                        self, 'Terjadi kesalahan saat menyimpan Artikel !',
                        'Pesan Kesalahan', wx.ICON_ERROR
                        )
                    pesan.ShowModal()
            else:
                pesan = wx.MessageDialog(
                    self, 'Terjadi kesalahan saat menyimpan Artikel !',
                    'Pesan Kesalahan', wx.ICON_ERROR
                    )
                pesan.ShowModal()

    def OnLcDataArtikelListItemSelected(self, event):
        """Event menyeleksi List Item Artikel"""
        # Button disabled
        self.btnSimpan.Disable()
        self.btnRandom.Disable()
        # Button active
        self.btnHapus.Enable()
        self.btnUbah.Enable()
        self.btnBatal.Enable()
        # Mengambil semua data Artikel dari List Ctrl
        no_baris = event.m_itemIndex
        self.NumCol = self.lcDataArtikel.GetColumnCount()
        kode_artikel = self.lcDataArtikel.GetItem(no_baris, 0).GetText()
        self.txtKodeArtikel.SetValue(kode_artikel)
        # Mengambil semua data-data yang diperlukan dari database
        model_artikel = ModelArtikel()
        result = model_artikel.readArtikelFromKodeArtikel(kode_artikel)
        # Menempatkan semua data-data ke element tertentu
        self.txt_nama_artikel.SetValue(result[0])
        self.cmbKodeKategori.SetStringSelection(result[1])
        self.lblKategori.SetLabel(result[2])
        self.spinS28.SetValue(int(result[3]))
        self.spinM30.SetValue(int(result[4]))
        self.spinL32.SetValue(int(result[5]))
        self.spinXL34.SetValue(int(result[6]))
        self.spinXXL36.SetValue(int(result[7]))
        self.spinXXXL38.SetValue(int(result[8]))
        self.txtTotalStok.SetValue(str(result[9]))
        self.spin_min.SetValue(int(result[10]))
        self.txt_harga_modal.SetValue(str(result[11]))
        self.txt_harga_jual.SetValue(str(result[12]))

    def OnTxtPencarianTextEnter(self, event):
        """Event mencari data Artikel berdasarkan Nama Artikelnya"""
        self.lcDataArtikel.DeleteAllItems()
        # Mengambil text pencarian
        text_pencarian = self.txtPencarian.GetValue()
        # Mengambil data Artikel berdasarkan Nama Artikelnya
        model_artikel = ModelArtikel()
        results = model_artikel.searchArtikel(text_pencarian)
        for result in results:
            jml_baris = self.lcDataArtikel.GetItemCount()
            self.lcDataArtikel.InsertStringItem(jml_baris, str(result[0]))
            self.lcDataArtikel.SetStringItem(
                jml_baris, 1,
                str(result[1]))
            self.lcDataArtikel.SetStringItem(
                jml_baris, 2,
                str(result[2]))
            self.lcDataArtikel.SetStringItem(
                jml_baris, 3,
                str(result[3]))
            self.lcDataArtikel.SetStringItem(
                jml_baris, 4,
                str(result[4]))
            self.lcDataArtikel.SetStringItem(
                jml_baris, 5,
                str(result[5]))
            if jml_baris % 2:
                self.lcDataArtikel.SetItemBackgroundColour(jml_baris, "#D7DEE6")
            elif int(result[2]) <= int(result[5]):
                self.lcDataArtikel.SetItemBackgroundColour(jml_baris, "#FFB870")
            else:
                self.lcDataArtikel.SetItemBackgroundColour(jml_baris, "#66CCFF")
            jml_baris = jml_baris + 1

    def OnTxtPencarianKeyUp(self, event):
        """Event untuk mengembalikan data semula setelah pencarian"""
        data = len(self.txtPencarian.GetValue())
        if data <= 0:
            self.__loadDataArtikelToListCtrl()
        else:
            pass
        


    
        
        
