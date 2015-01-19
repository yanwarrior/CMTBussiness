from xlwt import *
import os

class ExcelOutput:
	
	def __init__(self):
		self.namaSheet = ""
		self.namaHeader = ""
		self.kodeTransaksi = ""
		self.tanggalTransaksi = ""
		self.kodePelanggan = ""
		self.jmlBaris = 0
		self.namaVendor = ""
		
	def createBook(self):
		self.__book = Workbook()
	
	def createSheet(self):
		self.__sheet = self.__book.add_sheet(self.namaSheet)
		
	def setBorder(self, size):
		self.__border = Borders()
		self.__border.left = size
		self.__border.right = size
		self.__border.top = size
		self.__border.bottom = size
	
	def setBg(self):
		self.__bg = Pattern()
		self.__bg.pattern = Pattern.SOLID_PATTERN
		self.__bg.pattern_fore_colour = Style.colour_map['aqua']
	
	def setBgHead(self):
		self.__bgHead = Pattern()
		self.__bgHead.pattern = Pattern.SOLID_PATTERN
		self.__bgHead.pattern_fore_colour = Style.colour_map['light_orange']
		
	def createStyle(self):
		self.__style0 = XFStyle()
		self.__style0.borders = self.__border
		self.__style0.pattern = self.__bg
		
	def createStyleHead(self):
		self.__styleHead = XFStyle()
		self.__styleHead.pattern = self.__bgHead
		self.__styleHead.borders = self.__border
		
	
	def createHeader(self):
		self.__sheet.write(0, 1, self.namaHeader)
		self.__sheet.write(1, 0, "Transaksi")
		self.__sheet.write(1, 1, self.kodeTransaksi)
		self.__sheet.write(2, 0, "Tanggal")
		self.__sheet.write(2, 1, self.tanggalTransaksi)
		self.__sheet.write(3, 0, "No Kode Pelanggan")
		self.__sheet.write(3, 1, self.kodePelanggan)
		
	def createTable(self):
		self.__i = 6
		self.__sheet.write(self.__i, 0, "Nama Artikel", self.__styleHead)
		self.__sheet.write(self.__i, 1, "Ukuran", self.__styleHead)
		self.__sheet.write(self.__i, 2, "Quantity", self.__styleHead)
		self.__sheet.write(self.__i, 3, "Harga", self.__styleHead)
	
	def fillArtikel(self, total_semua, data):
		self.__j = 0
		while self.__j < self.jmlBaris:
			# input nama artikel data[0]
			self.__sheet.write(self.__j+self.__i+1, 0, data[self.__j][0], self.__style0)
			# input ukuran
			self.__sheet.write(self.__j+self.__i+1, 1, data[self.__j][1], self.__style0)
			# input qty
			self.__sheet.write(self.__j+self.__i+1, 2, data[self.__j][2], self.__style0)
			# input harga total
			self.__sheet.write(self.__j+self.__i+1, 3, data[self.__j][3], self.__style0)
			
			self.__j = self.__j + 1
	
		self.__k = self.__j + self.__i + 2
		
		self.__sheet.write(self.__k, 2, "Total Semuanya ", self.__style0)
		self.__sheet.write(self.__k, 3, int(total_semua), self.__style0)
		self.__sheet.write(self.__k+4, 1, self.namaVendor + ", Terimakasih.")
		
	def setWidthColumn(self):
		self.__sheet.col(0).width = 3500
		self.__sheet.col(1).width = 5000
		self.__sheet.col(3).width = 4000

	def saveToPath(self, path):
		# Check file exist ?
		path = path + "/" + self.kodeTransaksi + ".xls"
		if os.path.exists(path):
			os.remove(path)
			
		self.__book.save(path)
		#os.system("")
			
			
			
			
			
			
			
			
			

