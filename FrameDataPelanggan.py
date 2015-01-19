#Boa:Frame:Frame1

import wx
import wx.richtext

from misc import random_key
from models import ModelPelanggan

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTNBATAL, wxID_FRAME1BTNHAPUS, wxID_FRAME1BTNRANDOM, 
 wxID_FRAME1BTNSIMPAN, wxID_FRAME1BTNUBAH, wxID_FRAME1LCPELANGGAN, 
 wxID_FRAME1PANEL1, wxID_FRAME1RBPRIA, wxID_FRAME1RBWANITA, 
 wxID_FRAME1RICHTEXTCTRL1, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5, 
 wxID_FRAME1STATICTEXT6, wxID_FRAME1STATICTEXT7, wxID_FRAME1TXTEMAIL, 
 wxID_FRAME1TXTKODEPELANGGAN, wxID_FRAME1TXTNAMAPELANGGAN, 
 wxID_FRAME1TXTNOMERHANDPHONE, wxID_FRAME1TXTPENCARIAN, 
] = [wx.NewId() for _init_ctrls in range(23)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(478, 71), size=wx.Size(824, 452),
              style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, title=u'Data Pelanggan')
        self.SetClientSize(wx.Size(824, 452))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(824, 452),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Kode Pelanggan', name='staticText1', parent=self.panel1,
              pos=wx.Point(24, 24), size=wx.Size(89, 14), style=0)

        self.txtKodePelanggan = wx.TextCtrl(id=wxID_FRAME1TXTKODEPELANGGAN,
              name=u'txtKodePelanggan', parent=self.panel1, pos=wx.Point(24,
              40), size=wx.Size(208, 24), style=0, value=u'')
        self.txtKodePelanggan.SetEditable(False)
        self.txtKodePelanggan.Enable(False)

        self.btnRandom = wx.Button(id=wxID_FRAME1BTNRANDOM, label=u'Random',
              name=u'btnRandom', parent=self.panel1, pos=wx.Point(240, 40),
              size=wx.Size(69, 24), style=0)
        self.btnRandom.Bind(wx.EVT_BUTTON, self.OnBtnRandomButton,
              id=wxID_FRAME1BTNRANDOM)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Nama Pelanggan', name='staticText2', parent=self.panel1,
              pos=wx.Point(24, 72), size=wx.Size(92, 14), style=0)

        self.txtNamaPelanggan = wx.TextCtrl(id=wxID_FRAME1TXTNAMAPELANGGAN,
              name=u'txtNamaPelanggan', parent=self.panel1, pos=wx.Point(24,
              88), size=wx.Size(280, 24), style=0, value=u'')

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Email ', name='staticText3', parent=self.panel1,
              pos=wx.Point(24, 120), size=wx.Size(33, 14), style=0)

        self.txtEmail = wx.TextCtrl(id=wxID_FRAME1TXTEMAIL, name=u'txtEmail',
              parent=self.panel1, pos=wx.Point(24, 136), size=wx.Size(280, 24),
              style=0, value=u'')

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'Jenis Kelamin', name='staticText4', parent=self.panel1,
              pos=wx.Point(24, 168), size=wx.Size(75, 14), style=0)

        self.rbPria = wx.RadioButton(id=wxID_FRAME1RBPRIA, label=u'Pria',
              name=u'rbPria', parent=self.panel1, pos=wx.Point(24, 184),
              size=wx.Size(96, 24), style=0)
        self.rbPria.SetValue(True)

        self.rbWanita = wx.RadioButton(id=wxID_FRAME1RBWANITA, label=u'Wanita',
              name=u'rbWanita', parent=self.panel1, pos=wx.Point(88, 184),
              size=wx.Size(80, 22), style=0)
        self.rbWanita.SetValue(True)

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'Nomor Handphone', name='staticText5', parent=self.panel1,
              pos=wx.Point(24, 216), size=wx.Size(105, 14), style=0)

        self.txtNomerHandphone = wx.TextCtrl(id=wxID_FRAME1TXTNOMERHANDPHONE,
              name=u'txtNomerHandphone', parent=self.panel1, pos=wx.Point(24,
              232), size=wx.Size(280, 24), style=0, value=u'')

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label=u'Alamat', name='staticText6', parent=self.panel1,
              pos=wx.Point(24, 264), size=wx.Size(39, 14), style=0)

        self.richTextCtrl1 = wx.richtext.RichTextCtrl(id=wxID_FRAME1RICHTEXTCTRL1,
              parent=self.panel1, pos=wx.Point(24, 280), size=wx.Size(280, 100),
              style=wx.richtext.RE_MULTILINE, value=u'')
        self.richTextCtrl1.SetLabel(u'')

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label=u'Pencarian', name='staticText7', parent=self.panel1,
              pos=wx.Point(344, 24), size=wx.Size(54, 14), style=0)

        self.txtPencarian = wx.TextCtrl(id=wxID_FRAME1TXTPENCARIAN,
              name=u'txtPencarian', parent=self.panel1, pos=wx.Point(344, 40),
              size=wx.Size(456, 24), style=wx.TE_PROCESS_ENTER, value=u'')
        self.txtPencarian.Bind(wx.EVT_TEXT_ENTER, self.OnTxtPencarianTextEnter,
              id=wxID_FRAME1TXTPENCARIAN)
        self.txtPencarian.Bind(wx.EVT_KEY_UP, self.OnTxtPencarianKeyUp)

        self.lcPelanggan = wx.ListCtrl(id=wxID_FRAME1LCPELANGGAN,
              name=u'lcPelanggan', parent=self.panel1, pos=wx.Point(344, 80),
              size=wx.Size(456, 344), style=wx.LC_REPORT)
        self.lcPelanggan.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnLcPelangganListItemSelected, id=wxID_FRAME1LCPELANGGAN)

        self.btnSimpan = wx.Button(id=wxID_FRAME1BTNSIMPAN, label=u'Simpan',
              name=u'btnSimpan', parent=self.panel1, pos=wx.Point(24, 392),
              size=wx.Size(64, 34), style=0)
        self.btnSimpan.Bind(wx.EVT_BUTTON, self.OnBtnSimpanButton,
              id=wxID_FRAME1BTNSIMPAN)

        self.btnHapus = wx.Button(id=wxID_FRAME1BTNHAPUS, label=u'Hapus',
              name=u'btnHapus', parent=self.panel1, pos=wx.Point(176, 392),
              size=wx.Size(56, 34), style=0)
        self.btnHapus.Bind(wx.EVT_BUTTON, self.OnBtnHapusButton,
              id=wxID_FRAME1BTNHAPUS)

        self.btnBatal = wx.Button(id=wxID_FRAME1BTNBATAL, label=u'Batal',
              name=u'btnBatal', parent=self.panel1, pos=wx.Point(240, 392),
              size=wx.Size(64, 34), style=0)
        self.btnBatal.Bind(wx.EVT_BUTTON, self.OnBtnBatalButton,
              id=wxID_FRAME1BTNBATAL)

        self.btnUbah = wx.Button(id=wxID_FRAME1BTNUBAH, label=u'Ubah',
              name=u'btnUbah', parent=self.panel1, pos=wx.Point(96, 392),
              size=wx.Size(72, 36), style=0)
        self.btnUbah.Bind(wx.EVT_BUTTON, self.OnBtnUbahButton,
              id=wxID_FRAME1BTNUBAH)

    def __init__(self, parent):
        self._init_ctrls(parent)
        # Mematikan tombol
        self.btnBatal.Disable()
        self.btnHapus.Disable()
        self.btnUbah.Disable()
        # Menghidupkan tomsbol
        self.btnRandom.Enable()
        self.btnSimpan.Enable()
        # Set default radio button
        self.rbPria.SetValue(True)
        # Membuat column header
        self.__addColumnPelangganToListCtrl()
        
        # load data kategori ke List Ctrl
        self.__loadDataPelangganToListCtrl()


#-------------------------------------------------------------------------------
# BAGIAN BUILD
#-------------------------------------------------------------------------------
    def __addColumnPelangganToListCtrl(self):
        """Menambahkan kolom header List Ctrl"""
        self.lcPelanggan.InsertColumn(
            0, 'Kode', 
            width=100)
        self.lcPelanggan.InsertColumn(
            1, 'Nama Pelanggan', 
            width=180)
        self.lcPelanggan.InsertColumn(
            2, 'Email',
            width=200)
        self.lcPelanggan.InsertColumn(
            3, 'Jenis Kelamin',
            width=130)
        self.lcPelanggan.InsertColumn(
            4, 'HP',
            width=170)
        self.lcPelanggan.InsertColumn(
            5, 'Alamat',
            width=350)
        
    def __loadDataPelangganToListCtrl(self):
        """Meload data Pelanggan ke List Ctrl"""
        self.lcPelanggan.DeleteAllItems()
        # Ambil data Pelanggan dari tabel Pelanggan
        data_pelanggan = ModelPelanggan()
        data = data_pelanggan.readPelanggan()
        # Cek berhasil mengambil data Pelanggan ?
        if data:
            # Proses memasukan data-data Pelanggan jika
            # data Pelanggan sudah berhasil didapatkan dari database
            for i in data:
                ## mendapatkan jumlah baris
                jml_baris = self.lcPelanggan.GetItemCount()
                ## memasukan kode pelanggan pada kolom ke 0
                self.lcPelanggan.InsertStringItem(jml_baris, i[0])
                ## memasukan nama pelanggan pada kolom ke 1
                self.lcPelanggan.SetStringItem(
                    jml_baris, 1,
                    i[1])
                ## memasukan email pelanggan pada kolom ke 2
                self.lcPelanggan.SetStringItem(
                    jml_baris, 2,
                    i[2])
                ## memasukan jenis_kelamin pelanggan pada kolom ke 3
                self.lcPelanggan.SetStringItem(
                    jml_baris, 3,
                    i[3])
                ## memasukan nomer hp pelanggan pada kolom ke 4
                self.lcPelanggan.SetStringItem(
                    jml_baris, 4,
                    i[4])
                ## memasukan alamat pelanggan pada kolom ke 5
                self.lcPelanggan.SetStringItem(
                    jml_baris, 5,
                    i[5])
                ## menaikan jumlah baris yang ada
                jml_baris = jml_baris + 1
        
    def __bersih(self):
        """Membersihkan element pada frame Pelanggan"""
        self.txtKodePelanggan.SetValue("")
        self.txtNamaPelanggan.SetValue("")
        self.txtEmail.SetValue("")
        self.txtNomerHandphone.SetValue("")
        self.rbPria.SetValue(True)
        self.richTextCtrl1.SetValue("")
        
    def __validasiSimpan(self):
        """Memvalidasi sebelum menyimpan Artikel ke database"""
        # Mendapatkan kode, nama dan email pelanggan
        kode_pelanggan = self.txtKodePelanggan.GetValue()
        nama_pelanggan = self.txtNamaPelanggan.GetValue()
        email = self.txtEmail.GetValue()
        # mengecek pemilihan radio button jenis kelamin
        # untuk mendapatkan nilai jenis kelamin
        if self.rbPria.GetValue():
            jenis_kelamin = "Pria"
        else:
            jenis_kelamin = "Wanita"
        # mendapatkan nomer hp pelanggan
        hp = self.txtNomerHandphone.GetValue()
        # mendapatkan alamat pelanggan
        alamat = self.richTextCtrl1.GetValue()
        # inisialisasi pesan error
        pesan = ""
        
        # jika kode pelanggan belum diisi
        if not kode_pelanggan:
            pesan = pesan + "Kode Pelanggan Harus diisi\n"
        
        # jika nama pelanggan belum diisi
        if not nama_pelanggan:
            pesan = pesan + "Nama Pelanggan harus diisi\n"
            
        # jika email pelanggan belum diisi    
        if not email:
            pesan = pesan + "Email Pelanggan harus diisi\n"
        
        # jika jenis kelamin pelanggan belum dipilih
        if not jenis_kelamin:
            pesan = pesan + "Jenis kelamin Pelanggan harus diisi\n"
        
        # jika nomer hp pelanggan belum diisi
        if not hp:
            pesan = pesan + "Nomer HP Pelanggan harus diisi\n"
        
        if not hp.isdigit():
            # jika nomer hp pelanggan mengandung selain angka
            pesan = pesan + "Nomer HP harus digit !\n" 
        
        # jika alamat pelanggan belum diisis
        if not alamat:
            pesan = pesan + "Alamat Pelanggan harus diisi\n"
        
        # kembalikan pesan    
        return pesan


#-------------------------------------------------------------------------------
# BAGIAN EVENT
#-------------------------------------------------------------------------------

    def OnBtnRandomButton(self, event):
        """Event untuk merandom Kode Pelanggan"""
        rand_key = random_key("PLG",4)
        self.txtKodePelanggan.SetValue(rand_key)

    def OnBtnSimpanButton(self, event):
        """Event untuk menyimpan semua data pelanggan"""
        # cek data Pelanggan
        if self.__validasiSimpan():
            pesan_error = self.__validasiSimpan()
            pesan = wx.MessageDialog(
                self, pesan_error,
                'Pesan Kesalahan', wx.ICON_ERROR
                )
            pesan.ShowModal()
        else:
            kode_pelanggan = self.txtKodePelanggan.GetValue()
            nama_pelanggan = self.txtNamaPelanggan.GetValue()
            email = self.txtEmail.GetValue()
            if self.rbPria.GetValue():
                jenis_kelamin = "Pria"
            else:
                jenis_kelamin = "Wanita"
                
            hp = self.txtNomerHandphone.GetValue()
            alamat = self.richTextCtrl1.GetValue()
            
            model_pelanggan = ModelPelanggan()
            result = model_pelanggan.createPelanggan(
                kode_pelanggan, nama_pelanggan,
                email, jenis_kelamin, 
                hp, alamat
                )
            
            if result:
                
                self.__loadDataPelangganToListCtrl()
                
                # bersih
                self.__bersih()
                
                # notif
                pesan = wx.MessageDialog(
                    self, 'Penyimpanan Berhasil !',
                    'Pesan Sukses', wx.OK
                    )
                pesan.ShowModal()
            else:
                pesan = wx.MessageDialog(
                    self, 'Penyimpanan Gagal !',
                    'Pesan Kesalahan', wx.ICON_ERROR
                    )
                pesan.ShowModal()

    def OnLcPelangganListItemSelected(self, event):
        """Event menyeleksi list item pelanggan"""
        # Tombol yang dimatikan
        self.btnSimpan.Disable()
        self.btnRandom.Disable()
        # Tombol yang di hidupkan
        self.btnBatal.Enable()
        self.btnHapus.Enable()
        self.btnUbah.Enable()
        # Mengambil data-data yang ada di list ctrl pelanggan
        no_baris = event.m_itemIndex
        kode_pelanggan = self.lcPelanggan.GetItem(no_baris, 0).GetText()
        nama_pelanggan = self.lcPelanggan.GetItem(no_baris, 1).GetText()
        email = self.lcPelanggan.GetItem(no_baris, 2).GetText()
        jenkel = self.lcPelanggan.GetItem(no_baris, 3).GetText()
        hp = self.lcPelanggan.GetItem(no_baris, 4).GetText()
        alamat = self.lcPelanggan.GetItem(no_baris, 5).GetText()
        # Menempatkan semua data-data pelanggan ke element tertentu
        self.txtKodePelanggan.SetValue(kode_pelanggan)
        self.txtNamaPelanggan.SetValue(nama_pelanggan)
        self.txtEmail.SetValue(email)
        if jenkel == "Pria":
            self.rbPria.SetValue(True)
        else:
            self.rbWanita.SetValue(True)
        self.txtNomerHandphone.SetValue(hp)
        self.richTextCtrl1.SetValue(alamat)

    def OnBtnBatalButton(self, event):
        """Event membersihkan data pelanggan di layar"""
        self.__bersih()
        # Menghidupkan tombol
        self.btnSimpan.Enable()
        self.btnRandom.Enable()
        # Mematikan tombol
        self.btnHapus.Disable()
        self.btnUbah.Disable()
        self.btnBatal.Disable()

    def OnBtnHapusButton(self, event):
        """Event menghapus data pelanggan"""
        # Mendapatkan kode pelanggan
        kode_pelanggan = self.txtKodePelanggan.GetValue()
        # Menanyakan user apakah setuju untuk menghapus ?
        pesan = wx.MessageDialog(
            self, 'Anda yakin ingin menghapus ?',
            'Konfirmasi', wx.YES_NO
            )
        setuju = pesan.ShowModal()
        if setuju == wx.ID_YES:
            # Proses menghapus pelanggan
            model_pelanggan = ModelPelanggan()
            hasil_hapus = model_pelanggan.deletePelanggan(kode_pelanggan)
            if hasil_hapus:
                pesan = wx.MessageDialog(
                    self, 'Pelanggan berhasil dihapus',
                    'Pesan Sukses', wx.OK
                    )
                pesan.ShowModal()
                # Matikan tombol
                self.btnHapus.Disable()
                self.btnUbah.Disable()
                self.btnBatal.Disable()
                # Hidupkan tombol
                self.btnSimpan.Enable()
                self.btnRandom.Enable()
                # Bersihkan
                self.__bersih()
                # reload data list ctrl pelanggan
                self.__loadDataPelangganToListCtrl()
            else:
                pesan = wx.MessageDialog(
                    self, 'Pelanggan gagal dihapus',
                    'Pesan Kesalahan', wx.ICON_ERROR
                    )
                pesan.ShowModal()
                # Matikan tombol
                self.btnHapus.Disable()
                self.btnUbah.Disable()
                self.btnBatal.Disable()
                # Hidupkan tombol
                self.btnSimpan.Enable()
                self.btnRandom.Enable()
                self.__bersih()

    def OnBtnUbahButton(self, event):
        """Event mengubah data pelanggan"""
        # Validasi 
        valid = self.__validasiSimpan()
        if valid:
            pesan = wx.MessageDialog(
                self, valid,
                'Pesan Kesalahan', wx.ICON_ERROR
                )
            pesan.ShowModal()
        else:
            # Mendapatkan kode pelanggan
            kode_pelanggan = self.txtKodePelanggan.GetValue()
            # Mendapatkan nilai-nilai yang akan dirubah
            nama = self.txtNamaPelanggan.GetValue()
            email = self.txtEmail.GetValue()
            jenkel = ""
            if self.rbPria.GetValue() == True:
                jenkel = "Pria"
            else:
                jenkel = "Wanita"
            hp = self.txtNomerHandphone.GetValue()
            alamat = self.richTextCtrl1.GetValue()
            # Menanyakan ke user apakah setuju untuk merubah data ?
            # Merubah data pelanggan
            pesan = wx.MessageDialog(
                self, 'Anda yakin ingin merubah data ini ?',
                'Konfirmasi Perubahan', wx.YES_NO
                )
            hasil_pesan = pesan.ShowModal()
            if hasil_pesan == wx.ID_YES:
                # Merubah data pelanggan
                model_pelanggan = ModelPelanggan()
                hasil_perubahan = model_pelanggan.updatePelanggan(
                    kode_pelanggan, nama,
                    email, jenkel,
                    hp, alamat
                    )
                # Check apakah berhasil merubah data pelanggan ?
                if hasil_perubahan:
                    pesan = wx.MessageDialog(
                        self, 'Berhasil merubah data pelanggan',
                        'Pesan Sukses', wx.OK
                        )
                    pesan.ShowModal()
                else:
                    pesan = wx.MessageDialog(
                        self, 'Gagal merubah data pelanggan',
                        'Pesan Kesalahan', wx.ICON_ERROR
                        )
                    pesan.ShowModal()
            else:
                pass
            
            self.__loadDataPelangganToListCtrl()
            self.__bersih()
            # Matikan tombol
            self.btnHapus.Disable()
            self.btnUbah.Disable()
            self.btnBatal.Disable()
            # Hidupkan tombol
            self.btnSimpan.Enable()
            self.btnRandom.Enable()

    def OnTxtPencarianTextEnter(self, event):
        """Event pencarian data pelanggan"""
        # Clear item
        self.lcPelanggan.DeleteAllItems()
        # Ambil text pencarian
        text_cari = self.txtPencarian.GetValue()
        # Melakukan pencarian dan mengambil semua data pelanggan
        # berdasarkan pencarian tersebut
        model_pelanggan = ModelPelanggan()
        hasil_pencarian = model_pelanggan.searchPelanggan(text_cari)
        if hasil_pencarian:
            for i in hasil_pencarian:
                 ## mendapatkan jumlah baris
                jml_baris = self.lcPelanggan.GetItemCount()
                ## memasukan kode pelanggan pada kolom ke 0
                self.lcPelanggan.InsertStringItem(jml_baris, i[0])
                ## memasukan nama pelanggan pada kolom ke 1
                self.lcPelanggan.SetStringItem(
                    jml_baris, 1,
                    i[1])
                ## memasukan email pelanggan pada kolom ke 2
                self.lcPelanggan.SetStringItem(
                    jml_baris, 2,
                    i[2])
                ## memasukan jenis_kelamin pelanggan pada kolom ke 3
                self.lcPelanggan.SetStringItem(
                    jml_baris, 3,
                    i[3])
                ## memasukan nomer hp pelanggan pada kolom ke 4
                self.lcPelanggan.SetStringItem(
                    jml_baris, 4,
                    i[4])
                ## memasukan alamat pelanggan pada kolom ke 5
                self.lcPelanggan.SetStringItem(
                    jml_baris, 5,
                    i[5])
                ## menaikan jumlah baris yang ada
                jml_baris = jml_baris + 1
        else:
            pesan = wx.MessageDialog(
                self, 'Terjadi kesalahan saat pencarian',
                'pesan kesalahan', wx.ICON_ERROR
                )
            pesan.ShowModal()

    def OnTxtPencarianKeyUp(self, event):
        """Event untuk mengembalikan data semula setelah pencarian"""
        data = len(self.txtPencarian.GetValue())
        if data <= 0:
            self.__loadDataPelangganToListCtrl()
        else:
            pass
        
