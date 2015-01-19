#Boa:Frame:Frame1

import wx

from misc import random_key
from models import ModelKategori
from models import ModelArtikel

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTNBATAL, wxID_FRAME1BTNHAPUS, wxID_FRAME1BTNRANDOM, 
 wxID_FRAME1BTNSIMPAN, wxID_FRAME1BTNUBAH, wxID_FRAME1LCKATEGORI, 
 wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1TXTKODEKATEGORI, wxID_FRAME1TXTNAMAKATEGORI, 
] = [wx.NewId() for _init_ctrls in range(12)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(637, 182), size=wx.Size(341, 289),
              style= wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, title=u'Data Kategori')
        self.SetClientSize(wx.Size(341, 289))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(341, 289),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Kode Kategori', name='staticText1', parent=self.panel1,
              pos=wx.Point(16, 24), size=wx.Size(79, 14), style=0)

        self.txtKodeKategori = wx.TextCtrl(id=wxID_FRAME1TXTKODEKATEGORI,
              name=u'txtKodeKategori', parent=self.panel1, pos=wx.Point(16, 40),
              size=wx.Size(216, 24), style=0, value=u'')
        self.txtKodeKategori.SetEditable(False)
        self.txtKodeKategori.Enable(False)

        self.btnRandom = wx.Button(id=wxID_FRAME1BTNRANDOM, label=u'Random',
              name=u'btnRandom', parent=self.panel1, pos=wx.Point(248, 40),
              size=wx.Size(72, 24), style=0)
        self.btnRandom.Bind(wx.EVT_BUTTON, self.OnBtnRandomButton,
              id=wxID_FRAME1BTNRANDOM)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Nama Kategori', name='staticText2', parent=self.panel1,
              pos=wx.Point(16, 72), size=wx.Size(82, 14), style=0)

        self.txtNamaKategori = wx.TextCtrl(id=wxID_FRAME1TXTNAMAKATEGORI,
              name=u'txtNamaKategori', parent=self.panel1, pos=wx.Point(16, 88),
              size=wx.Size(304, 24), style=0, value=u'')

        self.lcKategori = wx.ListCtrl(id=wxID_FRAME1LCKATEGORI,
              name=u'lcKategori', parent=self.panel1, pos=wx.Point(16, 128),
              size=wx.Size(304, 100), style=wx.LC_REPORT)
        self.lcKategori.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnLcKategoriListItemSelected, id=wxID_FRAME1LCKATEGORI)

        self.btnSimpan = wx.Button(id=wxID_FRAME1BTNSIMPAN, label=u'Simpan',
              name=u'btnSimpan', parent=self.panel1, pos=wx.Point(16, 240),
              size=wx.Size(72, 32), style=0)
        self.btnSimpan.Bind(wx.EVT_BUTTON, self.OnBtnSimpanButton,
              id=wxID_FRAME1BTNSIMPAN)

        self.btnHapus = wx.Button(id=wxID_FRAME1BTNHAPUS, label=u'Hapus',
              name=u'btnHapus', parent=self.panel1, pos=wx.Point(168, 240),
              size=wx.Size(72, 32), style=0)
        self.btnHapus.Bind(wx.EVT_BUTTON, self.OnBtnHapusButton,
              id=wxID_FRAME1BTNHAPUS)

        self.btnBatal = wx.Button(id=wxID_FRAME1BTNBATAL, label=u'Batal',
              name=u'btnBatal', parent=self.panel1, pos=wx.Point(248, 240),
              size=wx.Size(72, 32), style=0)
        self.btnBatal.Bind(wx.EVT_BUTTON, self.OnBtnBatalButton,
              id=wxID_FRAME1BTNBATAL)

        self.btnUbah = wx.Button(id=wxID_FRAME1BTNUBAH, label=u'Ubah',
              name=u'btnUbah', parent=self.panel1, pos=wx.Point(96, 240),
              size=wx.Size(64, 32), style=0)
        self.btnUbah.Bind(wx.EVT_BUTTON, self.OnBtnUbahButton,
              id=wxID_FRAME1BTNUBAH)

    def __init__(self, parent):
        self._init_ctrls(parent)
        # Menonaktifkan Button Hapus, Ubah dan Batal
        self.btnHapus.Disable()
        self.btnUbah.Disable()
        self.btnBatal.Disable()
        # Menambahkan kolom header di List Ctrl
        self.__addColumnKategoriToListCtrl()
        # Meload data kategori ke List Ctrl
        self.__loadDataKategoriToListCtrl()


#-------------------------------------------------------------------------------
# BAGIAN BUILD
#-------------------------------------------------------------------------------
    def __addColumnKategoriToListCtrl(self):
        # __addColumnHeaderListCtrl
        """Menambahkan kolom header List Ctrl"""
        self.lcKategori.InsertColumn(
            0, 'Kode Kategori', 
            width=100)
        self.lcKategori.InsertColumn(
            1, 'Kategori', 
            width=180)
        
    def __loadDataKategoriToListCtrl(self):
        """Meload data Kategori di List Ctrl"""
        self.lcKategori.DeleteAllItems()
        data_kategori = ModelKategori()
        data = data_kategori.readKategori()
        if data:
            for i in data:
                jml_baris = self.lcKategori.GetItemCount()
                self.lcKategori.InsertStringItem(jml_baris, i[0])
                self.lcKategori.SetStringItem(
                    jml_baris, 1,
                    i[1])
                jml_baris = jml_baris + 1

    def __bersih(self):
        """Membersihkan elemen pada frame Kategori"""
        self.txtKodeKategori.SetValue("")
        self.txtNamaKategori.SetValue("")
    
    def __validasiSimpan(self):
        """Memvalidasi semua data yang akan di simpan ke database"""
        pesan = ""
        kode_kategori = self.txtKodeKategori.GetValue()
        nama_kategori = self.txtNamaKategori.GetValue()
        
        if not kode_kategori:
            pesan = pesan + "Kode kategori harus diisi !\n"
        
        if not nama_kategori:
            pesan = pesan + "Nama kategori harus diisi !\n"
            
        return pesan


#-------------------------------------------------------------------------------
# BAGIAN EVENT
#-------------------------------------------------------------------------------

    def OnBtnRandomButton(self, event):
        """Event Handling untuk generate key id"""
        rand_key = random_key("KTG",4)
        self.txtKodeKategori.SetValue(rand_key)


    def OnBtnSimpanButton(self, event):
        """Event Handling untung menyimpan data kategori ke database"""
        
        # Memvalidasi sebelum menyimpan
        pesan = self.__validasiSimpan()
        
        # Mengecek hasil validasi
        if not pesan:
            
            # Jika validasi valid maka meneruskan proses selanjutnya
            # Mengambil nilai Kode Kategori dan Nama Kategori
            k_kategori = self.txtKodeKategori.GetValue()
            n_kategori = self.txtNamaKategori.GetValue()
            
            # Menyimpan Kategori ke dalam database
            tambah_kategori = ModelKategori()
            result = tambah_kategori.createKategori(k_kategori, n_kategori)
            
            # Mengecek apakah data kategori berhasil disimpan
            if result:
                
                # Jika penyimpana Kategori berhasil
                # Program akan menampilkan pesan berhasil menyimpan
                pesan = "Penyimpana Berhasil"
                pesan_sukses = wx.MessageDialog(
                    self, pesan,
                    'Pesan Berhasil', wx.OK 
                    )
                pesan_sukses.ShowModal()
                
                # Tambahkan data yang tersimpan ke list ctrl
                # dengan memanggil method self.__loadDataKategoriToListCtrl()
                self.__loadDataKategoriToListCtrl()
                
                # Membersihkan frame
                self.__bersih()
                
            # Jika penyimpanan Kategori gagal
            else:
                
                # Program akan menampilkan pesan kesalahan saat menyimpan
                pesan = "Gagal Menyimpan"
                pesan_error = wx.MessageDialog(
                    self, pesan,
                    'Pesan Kesalahan', wx.ICON_ERROR
                    )
                pesan_error.ShowModal()
        
        # Jika tidak valid      
        else:
            
            # menampilkan pesan kesalahan  
            pesan_dialog = wx.MessageDialog(
                self, pesan,
                'Pesan Peringatan', wx.ICON_WARNING
                )
            pesan_dialog.ShowModal()
            
                 
    def OnLcKategoriListItemSelected(self, event):
        """Event yang terjadi saat List Ctrl Kategori dipilih"""
        
        # Mengambil data Kategori yang di seleksi
        no_baris = event.m_itemIndex
        kode_kategori = self.lcKategori.GetItem(no_baris, 0).GetText()
        nama_kategori = self.lcKategori.GetItem(no_baris, 1).GetText()
        
        # Memindahkan data ke element-element tertentu
        self.txtKodeKategori.SetValue(kode_kategori)
        self.txtNamaKategori.SetValue(nama_kategori)
        
        # Mengaktifkan Button Hapus, Ubah dan Batal
        self.btnUbah.Enable()
        self.btnHapus.Enable()
        self.btnBatal.Enable()
        
        # Menonaktifkan Button Simpan dan Random
        self.btnSimpan.Disable()
        self.btnRandom.Disable()
        

    def OnBtnBatalButton(self, event):
        """Event untuk membatalkan prose Ubah dan Hapus data"""
        
        # Membersihkan semua element
        self.__bersih()
        
        # Menonaktifkan Button Hapus, Ubah dan Batal
        self.btnHapus.Disable()
        self.btnUbah.Disable()
        self.btnBatal.Disable()
        
        # Mengaktifkan Button Random dan Simpan
        self.btnRandom.Enable()
        self.btnSimpan.Enable()
        

    def OnBtnHapusButton(self, event):
        """Event untuk menghapus data Kategori berdasarkan Kode Kategori"""
        
        # Menanyakan kepada user apakah yakin ingin menghapus data
        pesan = wx.MessageDialog(
            self, 'Anda yakin ingin menghapusnya ?',
            'Konfirmasi Hapus', wx.YES_NO
            )
        flag_konfirmasi = False
        hasil = pesan.ShowModal()
        if hasil == wx.ID_YES:
            flag_konfirmasi = True
        
        # Mengambil Kode Kategori
        kode_kategori = self.txtKodeKategori.GetValue()
        
        # Mengecek apakah elemen txtKodeKategori kosong ?
        flag_check = False
        if kode_kategori and flag_konfirmasi:
            flag_check = True
            
        # Menggunakan Method deleteKategori pada Class ModelKategori
        if flag_check:
            
            # Menghapus kategori
            model_kategori = ModelKategori()
            result_delete = model_kategori.deleteKategori(kode_kategori)
            flag_check = False
            
            # Cek berhasil hapus kategori ?
            if result_delete:
                
                # Ubah Kode Kategori di Artikel dengan Default
                model_artikel = ModelArtikel()
                result_update = model_artikel.updateArtikelWhenKategoriDelete(kode_kategori)
                flag_check = False
                
                # Cek hasil update Kode Kategori di Artikel ?
                if result_update:
                    
                    # Set flag_check jika berhasil
                    flag_check = True
                
        # Cek Berhasil Hapus Kategori ?
        if flag_check:
            
            # Tampil pesan Berhasil
            pesan = wx.MessageDialog(
                self, u'Proses Menghapus data Kategori Berhasil',
                'Pesan Sukses', wx.OK
                )
            pesan.ShowModal()
        
        # Cek Gagal hapus Kategori ?
        if not flag_check and flag_konfirmasi == True:
            
            # Tampil pesan Gagal
            pesan = wx.MessageDialog(
                self, 'Proses Menghapus data Kategori Gagal',
                'Pesan Kesalahan', wx.ICON_ERROR
                )
            pesan.ShowModal()
        
        # Muat ulang data Kategori di List Ctrl
        self.__loadDataKategoriToListCtrl()
        
        # Bersihkan element frame Kategori
        self.__bersih()


    def OnBtnUbahButton(self, event):
        """Event untuk mengubah data Kategori"""
        
        # Dapatkan kode dan nama Kategori
        kode_kategori = self.txtKodeKategori.GetValue()
        nama_kategori = self.txtNamaKategori.GetValue()
        
        # Proses ubah data Kategori
        model_kategori = ModelKategori()
        result_model_kategori = model_kategori.updateKategori(kode_kategori, nama_kategori)
        
        # Cek apakah perubahan berhasil ?
        if result_model_kategori:
            
            # Tampil pesan sukses
            pesan = wx.MessageDialog(
                self, 'Berhasil Mengupdate Kategori',
                'Pesan Sukses', wx.OK
                )
            pesan.ShowModal()
        
        # Jika perubahan gagal
        else:
            
            # Tampilkan pesan Kesalahan
            pesan = wx.MessageDialog(
                self, 'Gagal Mengupdate Kategori',
                'Pesan Kesalahan', wx.ICON_ERROR
                )
            pesan.ShowModal()
        
