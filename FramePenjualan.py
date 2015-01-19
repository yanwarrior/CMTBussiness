#Boa:Frame:Frame1

import wx

from misc import random_key
from models import ModelPelanggan
from models import ModelArtikel
from models import ModelStokUkuran
from models import ModelPengguna
from models import ModelTransaksi
from models import ModelDetilTransaksi
from misc import ExcelOutput
import datetime


def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTNRANDOM, wxID_FRAME1BTNSIMPAN, 
 wxID_FRAME1BTNTAMBAH, wxID_FRAME1CCUKURAN, wxID_FRAME1CMBKODEARTIKEL, 
 wxID_FRAME1CMBKODEPELANGGAN, wxID_FRAME1DATEPICK, wxID_FRAME1LBLNAMAARTIKEL, 
 wxID_FRAME1LBLNAMAPELANGGAN, wxID_FRAME1LCPENJUALAN, wxID_FRAME1PANEL1, 
 wxID_FRAME1SPNJUMLAH, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT10, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5, 
 wxID_FRAME1STATICTEXT7, wxID_FRAME1STATICTEXT8, wxID_FRAME1STATICTEXT9, 
 wxID_FRAME1TXTHARGAJUAL, wxID_FRAME1TXTKODETRANSAKSI, wxID_FRAME1TXTSUBTOTAL, 
] = [wx.NewId() for _init_ctrls in range(24)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(392, 129), size=wx.Size(830, 482),
              style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX,
              title=u'Penjualan')
        self.SetClientSize(wx.Size(830, 482))
        self.Bind(wx.EVT_CLOSE, self.OnFrame1Close)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(830, 482),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Kode Transaksi', name='staticText1', parent=self.panel1,
              pos=wx.Point(24, 24), size=wx.Size(82, 14), style=0)

        self.txtKodeTransaksi = wx.TextCtrl(id=wxID_FRAME1TXTKODETRANSAKSI,
              name=u'txtKodeTransaksi', parent=self.panel1, pos=wx.Point(24,
              40), size=wx.Size(216, 24), style=0, value=u'')
        self.txtKodeTransaksi.SetEditable(False)
        self.txtKodeTransaksi.Enable(False)

        self.btnRandom = wx.Button(id=wxID_FRAME1BTNRANDOM, label=u'Random',
              name=u'btnRandom', parent=self.panel1, pos=wx.Point(248, 40),
              size=wx.Size(72, 24), style=0)
        self.btnRandom.Bind(wx.EVT_BUTTON, self.OnBtnRandomButton,
              id=wxID_FRAME1BTNRANDOM)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Kode Pelanggan : ', name='staticText2',
              parent=self.panel1, pos=wx.Point(24, 72), size=wx.Size(98, 14),
              style=0)

        self.lblNamaPelanggan = wx.StaticText(id=wxID_FRAME1LBLNAMAPELANGGAN,
              label=u'......', name=u'lblNamaPelanggan', parent=self.panel1,
              pos=wx.Point(120, 72), size=wx.Size(19, 14), style=0)

        self.cmbKodePelanggan = wx.ComboBox(choices=[],
              id=wxID_FRAME1CMBKODEPELANGGAN, name=u'cmbKodePelanggan',
              parent=self.panel1, pos=wx.Point(24, 88), size=wx.Size(296, 27),
              style=0, value=u'')
        self.cmbKodePelanggan.SetLabel(u'')
        self.cmbKodePelanggan.Bind(wx.EVT_COMBOBOX,
              self.OnCmbKodePelangganCombobox, id=wxID_FRAME1CMBKODEPELANGGAN)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'Tanggal Transaksi', name='staticText4',
              parent=self.panel1, pos=wx.Point(632, 16), size=wx.Size(96, 14),
              style=0)

        self.datePick = wx.DatePickerCtrl(id=wxID_FRAME1DATEPICK,
              name=u'datePick', parent=self.panel1, pos=wx.Point(632, 32),
              size=wx.Size(168, 24), style=wx.DP_SHOWCENTURY)

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'Kode Artikel : ', name='staticText5', parent=self.panel1,
              pos=wx.Point(24, 144), size=wx.Size(78, 14), style=0)

        self.cmbKodeArtikel = wx.ComboBox(choices=[],
              id=wxID_FRAME1CMBKODEARTIKEL, name=u'cmbKodeArtikel',
              parent=self.panel1, pos=wx.Point(24, 160), size=wx.Size(208, 27),
              style=0, value=u'Pilih Kode Artikel ....')
        self.cmbKodeArtikel.SetLabel(u'')
        self.cmbKodeArtikel.Bind(wx.EVT_COMBOBOX, self.OnCmbKodeArtikelCombobox,
              id=wxID_FRAME1CMBKODEARTIKEL)

        self.lblNamaArtikel = wx.StaticText(id=wxID_FRAME1LBLNAMAARTIKEL,
              label=u'.......', name=u'lblNamaArtikel', parent=self.panel1,
              pos=wx.Point(104, 144), size=wx.Size(22, 14), style=0)

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label=u'Ukuran', name='staticText7', parent=self.panel1,
              pos=wx.Point(248, 144), size=wx.Size(40, 14), style=0)

        self.ccUkuran = wx.Choice(choices=['S28', 'M30', 'L32', 'XL34', 'XXL36',
              'XXXL38'], id=wxID_FRAME1CCUKURAN, name=u'ccUkuran',
              parent=self.panel1, pos=wx.Point(248, 160), size=wx.Size(80, 29),
              style=0)
        self.ccUkuran.Bind(wx.EVT_CHOICE, self.OnCcUkuranChoice,
              id=wxID_FRAME1CCUKURAN)

        self.staticText8 = wx.StaticText(id=wxID_FRAME1STATICTEXT8,
              label=u'Jumlah', name='staticText8', parent=self.panel1,
              pos=wx.Point(344, 144), size=wx.Size(48, 14), style=0)

        self.spnJumlah = wx.SpinCtrl(id=wxID_FRAME1SPNJUMLAH, initial=0,
              max=100, min=0, name=u'spnJumlah', parent=self.panel1,
              pos=wx.Point(344, 160), size=wx.Size(96, 24),
              style=wx.SP_ARROW_KEYS)
        self.spnJumlah.Bind(wx.EVT_SPINCTRL, self.OnSpnJumlahSpinctrl,
              id=wxID_FRAME1SPNJUMLAH)

        self.staticText9 = wx.StaticText(id=wxID_FRAME1STATICTEXT9,
              label=u'Harga Jual', name='staticText9', parent=self.panel1,
              pos=wx.Point(456, 144), size=wx.Size(58, 14), style=0)

        self.txtHargaJual = wx.TextCtrl(id=wxID_FRAME1TXTHARGAJUAL,
              name=u'txtHargaJual', parent=self.panel1, pos=wx.Point(456, 160),
              size=wx.Size(96, 24), style=0, value=u'')

        self.staticText10 = wx.StaticText(id=wxID_FRAME1STATICTEXT10,
              label=u'Sub Total ', name='staticText10', parent=self.panel1,
              pos=wx.Point(568, 144), size=wx.Size(54, 14), style=0)

        self.txtSubTotal = wx.TextCtrl(id=wxID_FRAME1TXTSUBTOTAL,
              name=u'txtSubTotal', parent=self.panel1, pos=wx.Point(568, 160),
              size=wx.Size(152, 24), style=0, value=u'')

        self.btnTambah = wx.Button(id=wxID_FRAME1BTNTAMBAH, label=u'Tambah',
              name=u'btnTambah', parent=self.panel1, pos=wx.Point(728, 160),
              size=wx.Size(72, 24), style=0)
        self.btnTambah.Bind(wx.EVT_BUTTON, self.OnBtnTambahButton,
              id=wxID_FRAME1BTNTAMBAH)

        self.lcPenjualan = wx.ListCtrl(id=wxID_FRAME1LCPENJUALAN,
              name=u'lcPenjualan', parent=self.panel1, pos=wx.Point(24, 200),
              size=wx.Size(776, 208), style=wx.LC_REPORT)
        self.lcPenjualan.Bind(wx.EVT_LIST_ITEM_ACTIVATED,
              self.OnLcPenjualanListItemActivated, id=wxID_FRAME1LCPENJUALAN)

        self.btnSimpan = wx.Button(id=wxID_FRAME1BTNSIMPAN, label=u'Simpan',
              name=u'btnSimpan', parent=self.panel1, pos=wx.Point(24, 432),
              size=wx.Size(85, 34), style=0)
        self.btnSimpan.Bind(wx.EVT_BUTTON, self.OnBtnSimpanButton,
              id=wxID_FRAME1BTNSIMPAN)

    def __init__(self, parent):
        self._init_ctrls(parent)
        # set default generate kode penjualan
        self.OnBtnRandomButton(None)
        # Load data kode pelanggan
        self.__loadDataKodePelangganTocmb()
        # seleksi cmb kode pelanggan ke keadaan default
        self.cmbKodePelanggan.SetStringSelection("Pilih Kode Pelanggan ....")
        # matikan fungsi choice
        self.ccUkuran.Disable()
        # matikan fungsi spin
        self.spnJumlah.Disable()
        # matikan fungsi kode pelanggan
        self.cmbKodeArtikel.Disable()
        # load kode artikel
        self.__loadDataKodeArtikelToCmb()
        # add column header
        self.__addColumnPenjualanToListCtrl()

#-------------------------------------------------------------------------------
# BAGIAN BUILD
#-------------------------------------------------------------------------------
    def __loadDataKodePelangganTocmb(self):
        """Meload data pelanggan ke dalam combo box"""
        # Mendapatkan kode pelanggan dari database
        model_pelanggan = ModelPelanggan()
        data_pelanggan = model_pelanggan.readPelanggan()
        if data_pelanggan:
            self.cmbKodePelanggan.Append("Pilih Kode Pelanggan ....")
            for kode_pelanggan in data_pelanggan:
                self.cmbKodePelanggan.Append(kode_pelanggan[0])
            
            
        else:
            pass
    
    def __loadDataKodeArtikelToCmb(self):
        """Meload data artikel ke combobox"""
        model_artikel = ModelArtikel()
        kode_artikel = model_artikel.readArtikel()
        self.cmbKodeArtikel.Append("Pilih Kode Artikel ....")
        if kode_artikel:
            for data in kode_artikel:
                self.cmbKodeArtikel.Append(str(data[0]))
        else:
            pass
        
    def __resetHarga(self):
        """Mereset harga sub total dan mereset spin jumlah pembelian"""
        # Reset
        self.spnJumlah.SetValue(0)
        #self.txtHargaJual.SetValue("0")
        self.txtSubTotal.SetValue("0")
        
    def __addColumnPenjualanToListCtrl(self):
        """Menambahkan kolom header List ctrl"""
        self.lcPenjualan.InsertColumn(
            0, 'Kode Artikel',
            width=100
            )
        self.lcPenjualan.InsertColumn(
            1, 'Nama Artikel',
            width=180
            )
        self.lcPenjualan.InsertColumn(
            2, 'Jenis Ukuran',
            width=120
            )
        self.lcPenjualan.InsertColumn(
            3, 'Jumlah',
            width=120
            )
        self.lcPenjualan.InsertColumn(
            4, 'Harga Jual',
            width=120
            )
        self.lcPenjualan.InsertColumn(
            5, 'Total',
            width=120
            )
            
    def __insertDataTransaksi(self):
        """Menyimpan data Transaksi"""
        
        # Mendapatkan jumlah baris (item) pada list ctrl
        jml_baris = self.lcPenjualan.GetItemCount()
        
        # Mengambil kode transaksi
        kode_transaksi = self.txtKodeTransaksi.GetValue()
        
        # Mengambil nama pelanggan
        kode_pelanggan = self.cmbKodePelanggan.GetStringSelection()
        
        # Mengambil kode pengguna
        kode_pengguna = ModelPengguna().readDataPengguna()
        
        # Mengammbil tanggal
        tgl = self.datePick.GetValue()
        bulan, hari, tahun = tgl.Month + 1, tgl.Day, tgl.Year 
        tanggal = datetime.date(tahun, bulan, hari)
        
        # Mengambil jam
        jam = str(datetime.datetime.now().time())[:5]
        
        # Mengambil total semuanya
        total = 0
        for i in range(0, jml_baris):
            sub_total = int(self.lcPenjualan.GetItem(i, 5).GetText())
            total = total + sub_total
        
        # Menyimpan data ke Transaksi
        model_transaksi = ModelTransaksi()
        hasil_transaksi = model_transaksi.createTransaksi(
            kode_transaksi, kode_pelanggan,
            kode_pengguna, tanggal, 
            jam, total
            )
        print hasil_transaksi
        # Mengecek apakah data transaksi berhasil di simpan ?
        if hasil_transaksi:
            for i in range(jml_baris):
                # Mendapatkan data untuk di simpan ke Detil Transaksi
                kode_artikel = self.lcPenjualan.GetItem(i, 0).GetText()
                ukuran = self.lcPenjualan.GetItem(i, 2).GetText()
                jumlah_qty = self.lcPenjualan.GetItem(i, 3).GetText()
                harga_jual = self.lcPenjualan.GetItem(i, 4).GetText()
                sub_total = self.lcPenjualan.GetItem(i, 5).GetText()
                
                # Menyimpan data ke Detil Transaksi
                model_detil_transaksi = ModelDetilTransaksi()
                print kode_transaksi
                print kode_artikel
                print ukuran
                print jumlah_qty
                print harga_jual
                print sub_total
                hasil_simpan_transaksi = model_detil_transaksi.createDetilTransaksi(
                    kode_transaksi, kode_artikel,
                    ukuran, jumlah_qty,
                    harga_jual, sub_total
                    )
                
                # Mengecek data detil transaksi apakah berhasil di simpan
                if not hasil_simpan_transaksi:
                    # Penyimpanan dibatalkan
                    '''
                    pesan = wx.MessageDialog(
                        self, 'Penyimpanan Detil transaksi gagal',
                        'Pesan Kesalahan', wx.ICON_ERROR
                        )
                    pesan.ShowModal()
                    break
                    '''
            # Tampil pesan sukses
            pesan = wx.MessageDialog(
                self, 'Penyimpanan Transaksi berhasil',
                'Pesan Sukses', wx.OK
                )
            pesan.ShowModal()
                
        # Jika data transaksi gagal di simpan
        else:
            
            pesan = wx.MessageDialog(
                self, 'Transaksi gagal disimpan',
                'Pesan Kesalahan', wx.ICON_ERROR
                )
            pesan.ShowModal()
            
    def __insertDataToExcel(self, path):
        """Membuat file excel"""
        # Mendapatkan direktori untuk penyimpana file excel
        direktori_simpan =  path
        # Menyimpan file ke dalam format xls
        excel = ExcelOutput()
        excel.namaSheet = self.txtKodeTransaksi.GetValue()
        excel.namaHeader = "SURAT BUKTI TRANSAKSI"
        excel.kodeTransaksi = self.txtKodeTransaksi.GetValue()
        excel.tanggalTransaksi = str(self.datePick.GetValue().Day + 1) + "/" + \
        str(self.datePick.GetValue().Month + 1) + "/" + str(self.datePick.GetValue().Year) 
        excel.kodePelanggan = self.cmbKodePelanggan.GetStringSelection()
        excel.jmlBaris = self.lcPenjualan.GetItemCount()
        excel.namaVendor = "Erfolghaben"
        
        excel.createBook()
        excel.createSheet()
        excel.setBorder(1)
        excel.setBg()
        excel.setBgHead()
        excel.createStyle()
        excel.createStyleHead()
        excel.createHeader()
        excel.createTable()
        data_lc = []
        total_semua = 0
        
        # Mengambil data-data Transaksi dari List ctrl
        for i in range(0,self.lcPenjualan.GetItemCount()):
            nama_artikel = self.lcPenjualan.GetItem(i,1).GetText()
            jenis_ukuran = self.lcPenjualan.GetItem(i,2).GetText()
            jumlah_qty = self.lcPenjualan.GetItem(i,3).GetText()
            harga_total = self.lcPenjualan.GetItem(i,5).GetText()
            total_semua = total_semua + int(harga_total)
            data_lc.append([nama_artikel, jenis_ukuran, jumlah_qty, harga_total])
        
        excel.fillArtikel(total_semua, data_lc)
        excel.setWidthColumn()
        excel.saveToPath(direktori_simpan)
                    
        # Menyimpan data transaksi dan detil transaksi
        self.__insertDataTransaksi()
        self.lcPenjualan.DeleteAllItems()
        
        

#-------------------------------------------------------------------------------
# BAGIAN EVENT
#-------------------------------------------------------------------------------

    def OnBtnRandomButton(self, event):
        """Event menggenerate kode Penjualan"""
        kode_penjualan = random_key("KTR-",6)
        self.txtKodeTransaksi.SetValue(kode_penjualan)

    def OnCmbKodePelangganCombobox(self, event):
        """Event untuk memilih kode pelanggan"""
        # Mengambil kode pelanggan
        kode_pelanggan = self.cmbKodePelanggan.GetStringSelection()
        # Mendapatkan nama pelanggan
        model_pelanggan = ModelPelanggan()
        nama_pelanggan = model_pelanggan.readNamaPelanggan(kode_pelanggan)
        if nama_pelanggan:
            self.lblNamaPelanggan.SetLabel(nama_pelanggan[0])
            self.cmbKodeArtikel.Enable()
        else:
            pass
        
        if kode_pelanggan == "Pilih Kode Pelanggan ....":
            self.lblNamaPelanggan.SetLabel("....")
            self.cmbKodeArtikel.SetStringSelection("Pilih Kode Artikel ....")
            # matikan kode artikel
            self.cmbKodeArtikel.Disable()
            self.__loadDataKodeArtikelToCmb()

    def OnCmbKodeArtikelCombobox(self, event):
        """Event untuk memilih kode artikel"""
        # Reset
        self.spnJumlah.SetValue(0)
        self.txtHargaJual.SetValue("0")
        self.txtSubTotal.SetValue("0")
        # Mengambil kode artikel
        kode_artikel = self.cmbKodeArtikel.GetStringSelection()
        model_artikel = ModelArtikel()
        nama_artikel = model_artikel.readArtikelFromKodeArtikel(kode_artikel)
        if nama_artikel:
            self.lblNamaArtikel.SetLabel(nama_artikel[0])
            self.txtHargaJual.SetValue(str(nama_artikel[11]))
            # Mengaktifkan choice ukuran artikel
            self.ccUkuran.Enable()
            
        if self.cmbKodeArtikel.GetStringSelection() == "Pilih Kode Artikel ....":
            self.lblNamaArtikel.SetLabel("....")
            self.ccUkuran.Disable()
            self.txtHargaJual.SetValue("0")

    def OnCcUkuranChoice(self, event):
        """Event untuk memilih ukuran artikel"""
        
        
        # Mengambil kode artikel
        kode_artikel = self.cmbKodeArtikel.GetStringSelection()
        # mengambil jenis ukuran
        jenis_ukuran = self.ccUkuran.GetStringSelection()
        
        # Mengecek ukuran S28
        if jenis_ukuran == "S28":
            # mengambil ukuran s28
            model_stok_ukuran = ModelStokUkuran()
            ukuran = model_stok_ukuran.readUkuran(kode_artikel, jenis_ukuran)
            if ukuran == 0:
                pesan = wx.MessageDialog(
                    self, "Ukuran S28 tidak tersedia",
                    'Informasi', wx.ICON_WARNING
                    )
                pesan.ShowModal()
                self.__resetHarga()
                self.spnJumlah.SetRange(0, 0)
            else:
                self.spnJumlah.SetRange(0, ukuran)
                self.spnJumlah.Enable()
        
        # Mengecek ukuran M30    
        elif jenis_ukuran == "M30":
            # mengambil ukuran m30
            model_stok_ukuran = ModelStokUkuran()
            ukuran = model_stok_ukuran.readUkuran(kode_artikel, jenis_ukuran)
            if ukuran == 0:
                pesan = wx.MessageDialog(
                    self, "Ukuran M30 tidak tersedia",
                    'Informasi', wx.ICON_WARNING
                    )
                pesan.ShowModal()
                self.__resetHarga()
                self.spnJumlah.SetRange(0, 0)
            else:
                self.spnJumlah.SetRange(0, ukuran)
                self.spnJumlah.Enable()
        
        # Mengecek ukuran L32    
        elif jenis_ukuran == "L32":
            model_stok_ukuran = ModelStokUkuran()
            ukuran = model_stok_ukuran.readUkuran(kode_artikel, jenis_ukuran)
            if ukuran == 0:
                pesan = wx.MessageDialog(
                    self, "Ukuran L32 tidak tersedia",
                    'Informasi', wx.ICON_WARNING
                    )
                pesan.ShowModal()
                self.__resetHarga()
                self.spnJumlah.SetRange(0, 0)
            else:
                self.spnJumlah.SetRange(0, ukuran)
                self.spnJumlah.Enable()
        
        # Pengecekan XL34
        elif jenis_ukuran == "XL34":
            model_stok_ukuran = ModelStokUkuran()
            ukuran = model_stok_ukuran.readUkuran(kode_artikel, jenis_ukuran)
            if ukuran == 0:
                pesan = wx.MessageDialog(
                    self, "Ukuran XL34 tidak tersedia",
                    'Informasi', wx.ICON_WARNING
                    )
                pesan.ShowModal()
                self.__resetHarga()
                self.spnJumlah.SetRange(0, 0)
            else:
                self.spnJumlah.SetRange(0, ukuran)
                self.spnJumlah.Enable()
        
        # Pengecekan XXL36        
        elif jenis_ukuran == "XXL36":
            model_stok_ukuran = ModelStokUkuran()
            ukuran = model_stok_ukuran.readUkuran(kode_artikel, jenis_ukuran)
            if ukuran == 0:
                pesan = wx.MessageDialog(
                    self, "Ukuran XXL36 tidak tersedia",
                    'Informasi', wx.ICON_WARNING
                    )
                pesan.ShowModal()
                self.__resetHarga()
                self.spnJumlah.SetRange(0, 0)
            else:
                self.spnJumlah.SetRange(0, ukuran)
                self.spnJumlah.Enable()
        
        # Pengecekan XXXL 38        
        elif jenis_ukuran == "XXXL38":
            model_stok_ukuran = ModelStokUkuran()
            ukuran = model_stok_ukuran.readUkuran(kode_artikel, jenis_ukuran)
            if ukuran == 0:
                pesan = wx.MessageDialog(
                    self, "Ukuran XXXL38 tidak tersedia",
                    'Informasi', wx.ICON_WARNING
                    )
                pesan.ShowModal()
                self.__resetHarga()
                self.spnJumlah.SetRange(0, 0)
            else:
                self.spnJumlah.SetRange(0, ukuran)
                self.spnJumlah.Enable()

    def OnSpnJumlahSpinctrl(self, event):
        """Event untuk memilih jumlah pembelian yang di inginkan"""
        # Mengambil jumlah pembelian
        jml_pembelian = self.spnJumlah.GetValue()
        # Mengalikan jml_pembelian dengan harga jual
        harga_jual = self.txtHargaJual.GetValue()
        sub_total = jml_pembelian * int(harga_jual)
        # Mengeset sub total 
        self.txtSubTotal.SetValue(str(sub_total)) 

    def OnBtnTambahButton(self, event):
        """Event menambahkan daftar belanja ke list ctrl penjualan"""
        # Mengecek self.txtSubTotal
        sub_total = self.txtSubTotal.GetValue()
        if sub_total != "0":
            # Mengambil kode artikel
            kode_artikel = self.cmbKodeArtikel.GetStringSelection()
            # Mengambil nama artikel
            nama_artikel = self.lblNamaArtikel.GetLabel()
            # Mengambil jenis ukuran
            jenis_ukuran = self.ccUkuran.GetStringSelection()
            # Mengambil jumlah pemesanan dari ukuran
            jumlah = str(self.spnJumlah.GetValue())
            # Mengambil harga jual
            harga_jual = self.txtHargaJual.GetValue()
            # Mengambil harga sub total
            sub_total = self.txtSubTotal.GetValue()
            
            # memasukan ke list ctrl
            jml_baris = self.lcPenjualan.GetItemCount()
            self.lcPenjualan.InsertStringItem(jml_baris, kode_artikel)
            self.lcPenjualan.SetStringItem(
                jml_baris, 1,
                nama_artikel)
            self.lcPenjualan.SetStringItem(
                jml_baris, 2,
                jenis_ukuran)
            self.lcPenjualan.SetStringItem(
                jml_baris, 3,
                jumlah)
            self.lcPenjualan.SetStringItem(
                jml_baris, 4,
                harga_jual)
            self.lcPenjualan.SetStringItem(
                jml_baris, 5,
                sub_total)
            jml_baris = jml_baris + 1
            
            # update stok ukuran (mengurangi)
            if jenis_ukuran == "S28":
                model_stok_ukuran = ModelStokUkuran()
                update_stok = model_stok_ukuran.updateStokUkuranS28(kode_artikel, jumlah)
            
            if jenis_ukuran == "M30":
                model_stok_ukuran = ModelStokUkuran()
                update_stok = model_stok_ukuran.updateStokUkuranM30(kode_artikel, jumlah)
            
            if jenis_ukuran == "L32":
                model_stok_ukuran = ModelStokUkuran()
                update_stok = model_stok_ukuran.updateStokUkuranL32(kode_artikel, jumlah)
                
            if jenis_ukuran == "XL34":
                model_stok_ukuran = ModelStokUkuran()
                update_stok = model_stok_ukuran.updateStokUkuranXL34(kode_artikel, jumlah)
            
            if jenis_ukuran == "XXL36":
                model_stok_ukuran = ModelStokUkuran()
                update_stok = model_stok_ukuran.updateStokUkuranXXL36(kode_artikel, jumlah)
            
            if jenis_ukuran == "XXXL38":
                model_stok_ukuran = ModelStokUkuran()
                update_stok = model_stok_ukuran.updateStokUkuranXXXL38(kode_artikel, jumlah)
            
            self.ccUkuran.Disable()
            self.spnJumlah.Disable()
            
        else:
            pesan = wx.MessageDialog(
                self, 'Anda belum memilih Artikel',
                'Peringatan', wx.ICON_WARNING
                )
            pesan.ShowModal()

    def OnLcPenjualanListItemActivated(self, event):
        """Event double click di list ctrl untuk membatalkan pesanan"""
        no_baris = event.m_itemIndex
        # Ambil kode artikel
        kode_artikel = self.lcPenjualan.GetItem(no_baris,0).GetText()
        # Ambil nama artikel
        nama_artikel = self.lcPenjualan.GetItem(no_baris,1).GetText()
        # Ambil jenis ukuran
        jenis_ukuran = self.lcPenjualan.GetItem(no_baris,2).GetText()
        # Ambil Jumlah ukuran
        jumlah_ukuran = self.lcPenjualan.GetItem(no_baris,3).GetText()
    
        msg = "Anda yakin ingin membatalkan item %s di penjualan ?" % nama_artikel
        pesan = wx.MessageDialog(
                self, msg,
                'Peringatan', wx.YES_NO
                )
        hasil = pesan.ShowModal()
        if hasil == wx.ID_YES:
            # Membatalkan dan mengembalikan stok ukuran artikel
            model_stok_ukuran = ModelStokUkuran()
            if jenis_ukuran == "S28":
                update_stok = model_stok_ukuran.updateStokUkuranS28(
                    kode_artikel,jumlah_ukuran, types=None
                    )
                # Delete Item
                self.lcPenjualan.DeleteItem(no_baris)
            
            if jenis_ukuran == "M30":
                update_stok = model_stok_ukuran.updateStokUkuranM30(
                    kode_artikel,jumlah_ukuran, types=None
                    )
                # Delete Item
                self.lcPenjualan.DeleteItem(no_baris)
        
            if jenis_ukuran == "L32":
                update_stok = model_stok_ukuran.updateStokUkuranL32(
                    kode_artikel,jumlah_ukuran, types=None
                    )
                # Delete Item
                self.lcPenjualan.DeleteItem(no_baris)
            
            if jenis_ukuran == "XL34":
                update_stok = model_stok_ukuran.updateStokUkuranXL34(
                    kode_artikel,jumlah_ukuran, types=None
                    )
                
                # Delete Item
                self.lcPenjualan.DeleteItem(no_baris)

            if jenis_ukuran == "XXL36":
                update_stok = model_stok_ukuran.updateStokUkuranXXL36(
                    kode_artikel,jumlah_ukuran, types=None
                    )
                
                # Delete Item
                self.lcPenjualan.DeleteItem(no_baris)
            if jenis_ukuran == "XXXL38":
                update_stok = model_stok_ukuran.updateStokUkuranXXXL38(
                    kode_artikel,jumlah_ukuran, types=None
                    )
                # Delete Item
                self.lcPenjualan.DeleteItem(no_baris)
        else:
            pass

    def OnFrame1Close(self, event):
        """Event sebelum di close framenya"""
        
        # Mendapatkan jumlah baris yang ada di list ctrl
        # sebagai tanda kalau 0 maka list tidak terisi item
        jml_baris = self.lcPenjualan.GetItemCount()
        
        # Mengecek jumlah baris (item) di dalam list ctrl
        # jika nilainya lebih dari 0 maka terdapat
        # item-item di list ctrl sebagai data transaksi
        if jml_baris > 0:
            
            # Menanyakan user jika aplikasi frame di close
            # kalau iya berarti data-data transaksi dibatalkan
            # jika tidak, maka data transaksi masih tetap ada
            pesan = wx.MessageDialog(
                    self, "Anda yakin membatalkan semua item penjualan ?",
                    'Informasi', wx.YES_NO
                    )
            
            # Jika user menekan tombol yes
            if pesan.ShowModal() == wx.ID_YES:
                
                # Mengambil semua data-data list ctrl 
                # untuk mengembalikan (membatalkan) proses transaks
                for i in range(0, jml_baris):
                    
                    kode_artikel = self.lcPenjualan.GetItem(i,0).GetText()
                    # Mengambil kode_artikel
                    # Mengambil jenis ukuran
                    jenis_ukuran = self.lcPenjualan.GetItem(i,2).GetText()
                    # Mengambil total
                    total = self.lcPenjualan.GetItem(i,3).GetText()
                    # Mengembalikan semua data-data Artikel 
                    # pada jumah stok ukurannya
                    model_stok_ukuran = ModelStokUkuran()
                    # Mengecek jenis ukuran S28
                    if jenis_ukuran == "S28":
                        model_stok_ukuran.updateStokUkuranS28(
                            kode_artikel, total, types=None
                            )
                    # Mengecek jenis ukuran M30
                    if jenis_ukuran == "M30":
                        model_stok_ukuran.updateStokUkuranM30(
                            kode_artikel, total, types=None
                            )
                    
                    if jenis_ukuran == "L32":
                        model_stok_ukuran.updateStokUkuranL32(
                            kode_artikel, total, types=None
                            )
                    
                    if jenis_ukuran == "XL34":
                        model_stok_ukuran.updateStokUkuranXL34(
                            kode_artikel, total, types=None
                            )
                            
                    if jenis_ukuran == "XXL36":
                        model_stok_ukuran.updateStokUkuranXXL36(
                            kode_artikel, total, types=None
                            )
                            
                    if jenis_ukuran == "XXXL38":
                        model_stok_ukuran.updateStokUkuranXXXL38(
                            kode_artikel, total, types=None
                            )
                    
                self.Destroy()
        else:
            self.Destroy()

    def OnBtnSimpanButton(self, event):
        """Event untuk menyimpan data-data penjualan"""
        
        # Mengambil jumlah baris yang ada di list ctrl
        jml_baris = self.lcPenjualan.GetItemCount()
        
        # mengecek jumlah baris. yang berarti
        # kalau > 0 ada item yang terdaftar di list ctr;
        if jml_baris > 0:
            
            # Membuat konfirmasi apakah setuju mencetak ke excel ?
            pesan = wx.MessageDialog(
                self, 'Anda ingin mencetak ke Excel ?',
                'Konfirmasi', wx.YES_NO
                )
            
            # Konfirmasi tombol yes no
            if pesan.ShowModal() == wx.ID_YES:
                
                # Dialog box untuk memilih tempat penyimpanan file excel
                dialog = wx.DirDialog(
                        None, "Pilih direktori penyimpanan :",
                        style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
                
                if dialog.ShowModal() == wx.ID_OK:
                    # Mendapatkan direktori untuk penyimpana file excel
                    direktori_simpan =  dialog.GetPath()
                    self.__insertDataToExcel(direktori_simpan)
                    
            # Jika user tidak setuju datanya dicetak ke format XLS
            else:
                self.__insertDataTransaksi()
                self.lcPenjualan.DeleteAllItems()
                    
        else:
            pesan = wx.MessageDialog(
                self, 'Tak ada satupun list item penjualan !',
                'Pesan', wx.ICON_WARNING
                )
            pesan.ShowModal()
            
    
    
    
                  
            
