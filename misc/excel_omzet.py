from xlwt import *
import time
import os

def excel_omzet(dari1, sampai1, jumbar, list_transaksi, total, filename):
	"""Export data omzet ke excel"""
	# buat workbook book
	book = Workbook()
	# Buat Worksheet sheet1
	sheet1 = book.add_sheet('Omzet')
	
	## Setting Font
	font0 = Font()
	font0.name = 'Arial'
	font0.height = 200
	font0.bold = True
	
	## Setting Border
	borders = Borders()
	borders.left = 1
	borders.right = 1
	borders.top = 1
	borders.bottom = 1
	
	## Setting Pattern
	BkgPat = Pattern()
	BkgPat.pattern = Pattern.SOLID_PATTERN
	BkgPat.pattern_fore_colour = 22
	
	## Buat dan setting Style style0 (Judul Kolom dan Rekap Total)
	style0 = XFStyle()
	style0.font = font0
	style0.borders = borders
	style0.pattern = BkgPat
	
	## Buat dan setting Style style1
	style1 = XFStyle()
	style1.borders = borders
	
	## Buat dan setting Style style_judul
	style_judul = XFStyle()
	style_judul.font = font0
	
	## Format Tanggal
	fmt = 'DD-MM-YYYY'
	style_tgl = XFStyle()
	style_tgl.num_format_str = fmt
	
	## Format Nominal isi Kolom
	fmt = 'RP #,##0.00'
	style_num1 = XFStyle()
	style_num1.borders = borders
	style_num1.num_format_str = fmt
	
	## Format Nominal total omzet
	fmt = 'Rp #,##0.00'
	style_num2 = XFStyle()
	style_num2.borders = borders
	style_num2.num_format_str = fmt
	style_num2.pattern = BkgPat
	style_num2.font = font0
	
	## Cetak Header
	sheet1.write(0,0, "LAPORAN OMZET PENJUALAN", style_judul)
	sheet1.write(1,0, "ERFOLGHABEN", style_judul)
	sheet1.write(2,0, "Dari Tgl", style_judul)
	sheet1.write(2,1, dari1, style_tgl)
	sheet1.write(3,0, "Sampai Tgl", style_judul)
	sheet1.write(3,1, sampai1, style_tgl)
	
	i = 4
	
	# Beri Judul Kolom
	sheet1.write(i,0, "Nomor Transaksi", style0)
	sheet1.write(i,1, "Total Harga", style0)
	
	j = 0
	while j < jumbar - 1:
		# mengisi data barang
		sheet1.write(j+i+1,0, list_transaksi[j][0], style1)
		sheet1.write(j+i+1,1, list_transaksi[j][1], style1)
		j = j + 1
	
	k = j + i + 1
	sheet1.write(k,0, "Total Omzet", style0)
	sheet1.write(k,1, int(total), style_num2)
	
	# Atur lebar kolom
	sheet1.col(0).width = 3500
	sheet1.col(1).width = 5000
	
	# Cek apakah ada file lama 
	if os.path.exists(filename):
		# hapus file lama
		os.remove(filename)
	
	# simpan file baru
	book.save(filename)
	
