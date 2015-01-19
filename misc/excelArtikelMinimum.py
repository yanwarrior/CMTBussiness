from xlwt import *
import time
import os

def excelArtikelMinimum(filename, sheet_name, data_artikel):
	"""Export data artikel minimum ke excel"""
	try:
		
		book = Workbook()
		sheet = book.add_sheet(sheet_name)		
		
		# Border
		garis = Borders()
		garis.left = 1
		garis.right = 1
		garis.top = 1
		garis.bottom = 1
		
		# Background Header
		bg_header = Pattern()
		bg_header.pattern = Pattern.SOLID_PATTERN
		bg_header.pattern_fore_colour = Style.colour_map['light_orange']
		style_header = XFStyle()
		style_header.pattern = bg_header
		style_header.borders = garis
		
		# Background Content
		bg_content = Pattern()
		bg_content.pattern = Pattern.SOLID_PATTERN
		bg_content.pattern_fore_colour = Style.colour_map['aqua']
		# Style Background Content
		style_content = XFStyle()
		style_content.pattern = bg_content
		# Style Border Content
		style_content.borders = garis
		
		
		# Style 
		style_data = XFStyle()
		style_data.borders = garis
		
		sheets = "LAPORAN MINIMUM " + sheet_name
		sheet.write(0, 0, sheets)
		sheet.write(1, 0, "Tanggal : ")
		sheet.write(1,1, str(time.strftime("%d %m %Y")))
			
		step = 4
		sheet.write(step, 0, "Kode Artikel", style_header)
		sheet.write(step, 1, "Kategori", style_header)
		sheet.write(step, 2, "Artikel", style_header)
		sheet.write(step, 3, "Harga", style_header)
		sheet.write(step, 4, "Stok", style_header)
		sheet.write(step, 5, "Stok Minimum", style_header)
		
		j = 0
		
		while j <= len(data_artikel) - 1:
			sheet.write(j+step+1, 0, str(data_artikel[j][0]), style_content)
			sheet.write(j+step+1, 1, str(data_artikel[j][1]), style_content)
			sheet.write(j+step+1, 2, str(data_artikel[j][2]), style_content)
			sheet.write(j+step+1, 3, str(data_artikel[j][3]), style_content)
			sheet.write(j+step+1, 4, str(data_artikel[j][4]), style_content)
			sheet.write(j+step+1, 5, str(data_artikel[j][5]), style_content)
			j += 1
			
			
		sheet.col(0).width = 3500
		sheet.col(2).width = 6000
		
		
		if os.path.exists(filename):
			os.remove(filename)
		
		book.save(filename)
		return True
	except:
		return False
		
	
