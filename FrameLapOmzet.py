#Boa:Frame:Frame1

import datetime
import os

import wx

from models import ModelTransaksi
from misc import excel_omzet
from misc import chart_omzet

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTNCETAK, wxID_FRAME1BTNCHART, 
 wxID_FRAME1BTNPROSESDATA, wxID_FRAME1DATEPICFROM, wxID_FRAME1DATEPICTO, 
 wxID_FRAME1LCOMZET, wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, 
 wxID_FRAME1TXTTOTALKESELURUHAN, 
] = [wx.NewId() for _init_ctrls in range(12)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(384, 194), size=wx.Size(840, 468),
              style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, title=u'Laporan Omzet')
        self.SetClientSize(wx.Size(840, 468))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(840, 468),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Dari Tanggal', name='staticText1', parent=self.panel1,
              pos=wx.Point(24, 32), size=wx.Size(68, 14), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Sampai Tanggal', name='staticText2', parent=self.panel1,
              pos=wx.Point(720, 32), size=wx.Size(84, 14), style=0)

        self.datePicFrom = wx.DatePickerCtrl(id=wxID_FRAME1DATEPICFROM,
              name=u'datePicFrom', parent=self.panel1, pos=wx.Point(24, 48),
              size=wx.Size(101, 28), style=wx.DP_DROPDOWN | wx.DP_SHOWCENTURY)
        self.datePicFrom.SetThemeEnabled(False)

        self.datePicTo = wx.DatePickerCtrl(id=wxID_FRAME1DATEPICTO,
              name=u'datePicTo', parent=self.panel1, pos=wx.Point(720, 48),
              size=wx.Size(101, 28), style=wx.DP_SHOWCENTURY)

        self.btnProsesData = wx.Button(id=wxID_FRAME1BTNPROSESDATA,
              label=u'Proses Data', name=u'btnProsesData', parent=self.panel1,
              pos=wx.Point(720, 88), size=wx.Size(96, 32), style=0)
        self.btnProsesData.Bind(wx.EVT_BUTTON, self.OnBtnProsesDataButton,
              id=wxID_FRAME1BTNPROSESDATA)

        self.lcOmzet = wx.ListCtrl(id=wxID_FRAME1LCOMZET, name=u'lcOmzet',
              parent=self.panel1, pos=wx.Point(24, 144), size=wx.Size(792, 256),
              style=wx.LC_REPORT)

        self.btnCetak = wx.Button(id=wxID_FRAME1BTNCETAK, label=u'Cetak',
              name=u'btnCetak', parent=self.panel1, pos=wx.Point(728, 416),
              size=wx.Size(88, 34), style=0)
        self.btnCetak.Bind(wx.EVT_BUTTON, self.OnBtnCetakButton,
              id=wxID_FRAME1BTNCETAK)

        self.btnChart = wx.Button(id=wxID_FRAME1BTNCHART, label=u'Chart',
              name=u'btnChart', parent=self.panel1, pos=wx.Point(632, 416),
              size=wx.Size(85, 34), style=0)
        self.btnChart.Bind(wx.EVT_BUTTON, self.OnBtnChartButton,
              id=wxID_FRAME1BTNCHART)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Total Keseluruhan', name='staticText3',
              parent=self.panel1, pos=wx.Point(24, 408), size=wx.Size(99, 14),
              style=0)

        self.txtTotalKeseluruhan = wx.TextCtrl(id=wxID_FRAME1TXTTOTALKESELURUHAN,
              name=u'txtTotalKeseluruhan', parent=self.panel1, pos=wx.Point(24,
              424), size=wx.Size(192, 24), style=0, value=u'')

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.__createColumnListCtrl()
        
#-------------------------------------------------------------------------------
# BAGIAN BUILD
#-------------------------------------------------------------------------------


    def __createColumnListCtrl(self):
        """Membuat kolom List CTrl"""
        self.lcOmzet.InsertColumn(0,"Nota Transaksi", width=140)
        self.lcOmzet.InsertColumn(1,"Total Penjualan", width=260)
        
    def __loadDataOmzet(self):
        tanggal1 = self.datePicFrom.GetValue()
        tanggal2 = self.datePicTo.GetValue()
        
        dari_bulan = tanggal1.Month + 1
        dari_hari = tanggal1.Day
        dari_tahun = tanggal1.Year
        dari_tanggal = datetime.date(dari_tahun, dari_bulan, dari_hari)
        
        sampai_bulan = tanggal2.Month + 1
        sampai_hari = tanggal2.Day
        sampai_tahun = tanggal2.Year
        sampai_tanggal = datetime.date(sampai_tahun, sampai_bulan, sampai_hari)
        
        self.lcOmzet.DeleteAllItems()
        model_transaksi = ModelTransaksi()
        hasil_omzet = model_transaksi.readTransaksiFromDate(dari_tanggal, sampai_tanggal)
        if hasil_omzet:
            jml_baris = self.lcOmzet.GetItemCount()
            total = 0
            for omzet in hasil_omzet:
                self.lcOmzet.InsertStringItem(jml_baris, omzet[0])
                self.lcOmzet.SetStringItem(jml_baris, 1, str(omzet[1]))
                jml_baris += 1
                total += omzet[1]
            
            self.txtTotalKeseluruhan.SetValue(str(total))

    def __chartOmzetPenjualan(self):
        jml_baris = self.lcOmzet.GetItemCount()
        tuple_nota = []
        list_nota = []
        office = "Erfolghaben"
        about = "DATA OMZET"
        total_semua = 0
        
        for i in range(jml_baris):
            kode_transaksi = self.lcOmzet.GetItem(i, 0).GetText()
            sub_total = self.lcOmzet.GetItem(i, 1).GetText()
            tuple_nota.append(kode_transaksi)
            list_nota.append(int(sub_total))
            total_semua += int(sub_total)
        
        if self.lcOmzet.GetItemCount() > 0:
            chart_omzet(tuple(tuple_nota), list_nota, office, about)
        else:
            pesan = wx.MessageDialog(
                self, 'Tidak adat data yang ditampilkan',
                'Pesan Peringatan', wx.ICON_WARNING
                )
            pesan.ShowModal()
            
    def __getDir(self):
        dialog = wx.DirDialog(None, "Choose a directory:",style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        direktori = ""
        if dialog.ShowModal() == wx.ID_OK:
            direktori = dialog.GetPath()
        
        return direktori
        dialog.Destroy()
    
    def OnBtnProsesDataButton(self, event):
        self.__loadDataOmzet()

    def OnBtnChartButton(self, event):
        self.__chartOmzetPenjualan()

    def OnBtnCetakButton(self, event):
        """"""
        item = self.lcOmzet.GetItemCount()
        
        # ambil tanggal dari
        tgl = self.datePicFrom.GetValue()
        dari_tanggal = datetime.date(
            tgl.Year, tgl.Month+1, 
            tgl.Day)
        tgl = self.datePicTo.GetValue()
        sampai_tanggal = datetime.date(
            tgl.Year, tgl.Month+1, 
            tgl.Day
            )
        
        # ambil tanggal sampai
        if item > 0:
            jml_baris = self.lcOmzet.GetItemCount()
            
            data = []
            total = 0
            for i in range(jml_baris):
                kode_transaksi = self.lcOmzet.GetItem(i,0).GetText()
                sub_total = self.lcOmzet.GetItem(i,1).GetText()
                data.append([kode_transaksi, sub_total])
                total = total + int(sub_total)
            
            # ambil direktori
            direktori = self.__getDir()
            filename = direktori + "/" + str(sampai_tanggal) + ".xls" 
            
            # konvert ke excel
            excel_omzet(str(dari_tanggal), str(sampai_tanggal), jml_baris, data, total, str(filename))
            
            # notofikasi berhasil
            pesan = wx.MessageDialog(
                self, 'Pembuatan Laporan Excel berhasil',
                'Pesan Sukses', wx.OK
                )
            pesan.ShowModal()
            
            self.lcOmzet.DeleteAllItems()
        else:
            pesan = wx.MessageDialog(
                self, 'Tidak ada data yang ingin di cetak',
                'Peringatan', wx.ICON_WARNING
                )
            pesan.ShowModal()
                
        
