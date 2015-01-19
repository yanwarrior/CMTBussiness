#Boa:Frame:Frame1

import wx
import wx.lib.buttons

import FrameDataArtikel
import FrameDataKategori
import FrameDataPelanggan
import FramePenjualan
import FrameLapMinimum
import FrameLapOmzet
import FramePengguna
import FrameAbout

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1PANEL1, wxID_FRAME1PNGGAMBAR, wxID_FRAME1STATICLINE1, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
] = [wx.NewId() for _init_ctrls in range(6)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(458, 156), size=wx.Size(600, 354),
              style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, title=u'Menu Utama')
        self.SetClientSize(wx.Size(600, 354))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(600, 354),
              style=wx.TAB_TRAVERSAL)

        self.pngGambar = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_FRAME1PNGGAMBAR, name=u'pngGambar', parent=self.panel1,
              pos=wx.Point(236, 57), size=wx.Size(128, 128), style=0)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAME1STATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(208, 200),
              size=wx.Size(184, 2), style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Clothing Management Tools', name='staticText1',
              parent=self.panel1, pos=wx.Point(190, 224), size=wx.Size(223, 17),
              style=0)
        self.staticText1.Center(wx.HORIZONTAL)
        self.staticText1.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Sans'))
        self.staticText1.SetForegroundColour(wx.Colour(30, 144, 255))

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Versi 1.0 - Betha', name='staticText2',
              parent=self.panel1, pos=wx.Point(254, 248), size=wx.Size(91, 14),
              style=0)
        self.staticText2.SetForegroundColour(wx.Colour(77, 77, 77))
        self.staticText2.Center(wx.HORIZONTAL)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self._menuUtama()
        
        # set image gambar tampilan depan
        gambar  = 'img/bisnis.png'
        img     = wx.Image(gambar, wx.BITMAP_TYPE_ANY)
        self.pngGambar.SetBitmap(wx.BitmapFromImage(img))
        
    def _menuUtama(self):
        """Create Main Menu"""
        
        idArtikel = wx.NewId()
        idKategori = wx.NewId()
        idPelanggan = wx.NewId()
        idPenjualan = wx.NewId()
        idLapMin = wx.NewId()
        idLapOmzet = wx.NewId()
        idPengguna = wx.NewId()
        idTentang = wx.NewId()
        
        # set menubar and menu
        menuUtama = wx.MenuBar()
        menuMaster = wx.Menu()
        menuTransaksi = wx.Menu()
        menuLaporan = wx.Menu()
        menuPengaturan = wx.Menu()
        
        # set sub menu data artikel -> menu master
        subMenuArtikel  = wx.MenuItem(menuMaster,idArtikel,'Data Artikel')
        subMenuArtikel.SetBitmap(wx.Bitmap('img/artikel.png'))
        menuMaster.AppendItem(subMenuArtikel)
        
        # set sub menu data kategori -> menu master
        subMenuKategori = wx.MenuItem(menuMaster,idKategori,'Data Kategori')
        subMenuKategori.SetBitmap(wx.Bitmap('img/kategori.png'))
        menuMaster.AppendItem(subMenuKategori)
        
        # set sub menu data pelanggan -> menu master
        subMenuPelanggan= wx.MenuItem(menuMaster,idPelanggan,'Data Pelanggan')
        subMenuPelanggan.SetBitmap(wx.Bitmap('img/pelanggan.png'))
        menuMaster.AppendItem(subMenuPelanggan)
        
        # menu master created
        menuUtama.Append(menuMaster, 'Master')
        
        # set sub menu penjualan -> menu transaksi
        subMenuPenjualan= wx.MenuItem(menuTransaksi,idPenjualan,'Penjualan')
        subMenuPenjualan.SetBitmap(wx.Bitmap('img/penjualan.png'))
        menuTransaksi.AppendItem(subMenuPenjualan)
        
        # menu transaksi created
        menuUtama.Append(menuTransaksi, 'Transaksi')
        
        # set sub menu laporan minimum -> menu laporan
        subMenuLapMin   = wx.MenuItem(menuLaporan,idLapMin,'Laporan Minimum')
        subMenuLapMin.SetBitmap(wx.Bitmap('img/report_min.png'))
        menuLaporan.AppendItem(subMenuLapMin)
        
        # set sub menu laporan omzet -> menu laporan
        subMenuLapOmzet = wx.MenuItem(menuLaporan,idLapOmzet,'Laporan Omzet')
        subMenuLapOmzet.SetBitmap(wx.Bitmap('img/report_omzet.png'))
        menuLaporan.AppendItem(subMenuLapOmzet)
        
        # menu laporan created
        menuUtama.Append(menuLaporan, 'Laporan')
        
        # set sub menu pengguna -> menu pengaturan
        
        subMenuPengguna = wx.MenuItem(menuPengaturan,idPengguna,'Pengguna')
        subMenuPengguna.SetBitmap(wx.Bitmap('img/pengguna.png'))
        menuPengaturan.AppendItem(subMenuPengguna)
        
        # set sub menu pengguna -> menu pengaturan
        
        subMenuTentang = wx.MenuItem(menuPengaturan,idTentang,'Tentang')
        subMenuTentang.SetBitmap(wx.Bitmap('img/about.png'))
        menuPengaturan.AppendItem(subMenuTentang)
        '''
        # set sub menu tentang -> menu pengaturan
        subMenuTentang = wx.MenuItem(menuPengaturan, idTentang,'Tentang')
        subMenuTentang.setBitmap(wx.Bitmap('img/about.png'))
        menuPengaturan.AppendItem(subMenuTentang)
        '''
        
        # menu pengaturan created
        menuUtama.Append(menuPengaturan, 'Pengaturan')
        
        self.SetMenuBar(menuUtama)
        
        # set Binding Event
        self.Bind(wx.EVT_MENU, self.panggilArtikel, id=idArtikel)
        self.Bind(wx.EVT_MENU, self.panggilKategori, id=idKategori)
        self.Bind(wx.EVT_MENU, self.panggilPelanggan, id=idPelanggan)
        self.Bind(wx.EVT_MENU, self.panggilPenjualan, id=idPenjualan)
        self.Bind(wx.EVT_MENU, self.panggilLapMin, id=idLapMin)
        self.Bind(wx.EVT_MENU, self.panggilLapOmzet, id=idLapOmzet)
        self.Bind(wx.EVT_MENU, self.panggilPengguna, id=idPengguna)
        self.Bind(wx.EVT_MENU, self.panggilAbout, id=idTentang)
    
    def panggilArtikel(self,e):
        """Calling Frame artikel"""
        self.main = FrameDataArtikel.Frame1(self)
        self.main.Show()

    def panggilKategori(self,e):
        """Calling Frame kategori"""
        self.main = FrameDataKategori.create(self)
        self.main.Show(True)
        
    def panggilPelanggan(self,e):
        """Calling Frame pelanggan"""
        framePelanggan = FrameDataPelanggan.create(None)
        framePelanggan.Show(True)
    
    def panggilPenjualan(self,e):
        """Calling Frame penjualan"""
        framePenjualan = FramePenjualan.create(None)
        framePenjualan.Show(True)
    
    def panggilLapMin(self,e):
        """Calling Frame laporan minimum"""
        frameLapMin = FrameLapMinimum.create(None)
        frameLapMin.Show(True)
    
    def panggilLapOmzet(self,e):
        """Calling Frame laporan omzet"""
        frameLapOmzet = FrameLapOmzet.create(None)
        frameLapOmzet.Show(True) 
    
    def panggilPengguna(self,e):
        """Calling Frame Pengguna"""
        framePengguna = FramePengguna.create(None)
        framePengguna.Show(True)
    
    def panggilAbout(self,e):
        """Calling Frame Tentang"""
        frameAbout= FrameAbout.create(None)
        frameAbout.Show(True)
        
    
        
        
        
        
        
