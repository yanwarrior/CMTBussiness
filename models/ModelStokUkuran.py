from ConnectorMySQL import *

class ModelStokUkuran(ConnectorMySQL):
	
	def __init__(self):
		"""Membuat koneksi pertama untuk Stok Ukuran"""
		ConnectorMySQL.__init__(self)
    
	def createStokUkuran(self, *args):
		"""Menambahkan data Stok Ukuran"""
		sql = """INSERT INTO Stok_Ukuran VALUES 
		('','%s','%s','%s','%s','%s','%s','%s','%s')
		""" % args[0]
    
		try:
			self.cursor.execute(sql)
			self.db.commit()
			return True
		except:
			return False
			self.db.rollback()
      
	def readStokUkuran(self):
		"""Membaca data Stok Ukuran"""
		sql = """SELECT * FROM	Stok_Ukuran"""
    
		try:
			self.cursor.execute(sql)
			results = self.cursor.fetchall()
			return results
		except:
			return False
		
	def readUkuran(self, kode_artikel, field):
		"""Membaca ukuran S28 dari kode artikel"""
		sql = """
			
			SELECT	%s
			
			FROM 	Stok_Ukuran
			
			WHERE	kode_artikel = '%s'
		""" % (field, kode_artikel)
		
		try:
			self.cursor.execute(sql)
			ukuran = self.cursor.fetchone()
			return ukuran[0]
		except:
			return False
  
	def updateStokUkuran(self, kodeArtikel, *args):
		"""Mengubah data Stok Ukuran"""
		data = args + (kodeArtikel,)

		sql = """
			UPDATE	Stok_Ukuran
	    
			SET		S28 = '%s',
					M30 = '%s',
					L32 = '%s',
					XL34 = '%s',
					XXL36 = '%s',
					XXXL38 = '%s',
					total_stok = '%s'
			
			WHERE 	kode_artikel = '%s'
		""" % data
	  
		try:
			self.cursor.execute(sql)
			self.db.commit()
			return True
		except:
			return False
			self.db.rollback()
	
	def updateStokUkuranS28(self, kode_artikel, s28, types="SUB"):
		"""Mengupdate jumlah S28 dari Stok Ukuran berdasarkan kode_artikel"""
		sql = """
			SELECT 	S28, total_stok
			
			FROM 	Stok_Ukuran
			
			WHERE	kode_artikel = '%s'
		""" % kode_artikel
		try:
			self.cursor.execute(sql)
			ukuran = self.cursor.fetchone()
			total_ukuran = 0
			total_stok = 0
			if types == "SUB":
				ukuran_s28 = int(ukuran[0]) - int(s28)
				total_stok = int(ukuran[1]) - int(s28)
			else:
				ukuran_s28 = int(ukuran[0]) + int(s28)
				total_stok = int(ukuran[1]) + int(s28)
			
			sql = """
				UPDATE 	Stok_Ukuran
				
				SET 	S28 = %d,
						total_stok = %d
						
				WHERE 	kode_artikel = '%s'
			""" % (ukuran_s28, total_stok, kode_artikel)
			
			try:
				self.cursor.execute(sql)
				self.db.commit()
				return True
			except:
				return False
		except:
			return False
	
	def updateStokUkuranM30(self, kode_artikel, m30, types="SUB"):
		"""Mengupdate jumlah M30 dari Stok Ukuran berdasarkan kode_artikel"""
		sql = """
			SELECT 	M30, total_stok
			
			FROM 	Stok_Ukuran
			
			WHERE	kode_artikel = '%s'
		""" % kode_artikel
		try:
			self.cursor.execute(sql)
			ukuran = self.cursor.fetchone()
			total_ukuran = 0
			total_stok = 0
			if types == "SUB":
				ukuran_m30 = int(ukuran[0]) - int(m30)
				total_stok = int(ukuran[1]) - int(m30)
			else:
				ukuran_m30 = int(ukuran[0]) + int(m30)
				total_stok = int(ukuran[1]) + int(m30)
			
			sql = """
				UPDATE 	Stok_Ukuran
				
				SET 	M30 = %d,
						total_stok = %d
						
				WHERE 	kode_artikel = '%s'
			""" % (ukuran_m30, total_stok, kode_artikel)
			
			try:
				self.cursor.execute(sql)
				self.db.commit()
				return True
			except:
				return False
		except:
			return False
		
	def updateStokUkuranL32(self, kode_artikel, l32, types="SUB"):
		"""Mengupdate jumlah L32 dari Stok Ukuran berdasarkan kode_artikel"""
		sql = """
			SELECT 	L32, total_stok
			
			FROM 	Stok_Ukuran
			
			WHERE	kode_artikel = '%s'
		""" % kode_artikel
		try:
			self.cursor.execute(sql)
			ukuran = self.cursor.fetchone()
			total_ukuran = 0
			total_stok = 0
			if types == "SUB":
				ukuran_l32 = int(ukuran[0]) - int(l32)
				total_stok = int(ukuran[1]) - int(l32)
			else:
				ukuran_l32 = int(ukuran[0]) + int(l32)
				total_stok = int(ukuran[1]) + int(l32)
			sql = """
				UPDATE 	Stok_Ukuran
				
				SET 	L32 = %d,
						total_stok = %d
						
				WHERE 	kode_artikel = '%s'
			""" % (ukuran_l32, total_stok, kode_artikel)
			
			try:
				self.cursor.execute(sql)
				self.db.commit()
				return True
			except:
				return False
		except:
			return False
		
	def updateStokUkuranXL34(self, kode_artikel, xl34, types="SUB"):
		"""Mengupdate jumlah XL34 dari Stok Ukuran berdasarkan kode_artikel"""
		sql = """
			SELECT 	XL34, total_stok
			
			FROM 	Stok_Ukuran
			
			WHERE	kode_artikel = '%s'
		""" % kode_artikel
		try:
			self.cursor.execute(sql)
			ukuran = self.cursor.fetchone()
			total_ukuran = 0
			total_stok = 0
			if types == "SUB":
				ukuran_xl34 = int(ukuran[0]) - int(xl34)
				total_stok = int(ukuran[1]) - int(xl34)
			else:
				ukuran_xl34 = int(ukuran[0]) + int(xl34)
				total_stok = int(ukuran[1]) + int(xl34)
			
			sql = """
				UPDATE 	Stok_Ukuran
				
				SET 	XL34 = %d,
						total_stok = %d
						
				WHERE 	kode_artikel = '%s'
			""" % (ukuran_xl34, total_stok, kode_artikel)
			
			try:
				self.cursor.execute(sql)
				self.db.commit()
				return True
			except:
				return False
		except:
			return False
		
	def updateStokUkuranXXL36(self, kode_artikel, xxl36, types="SUB"):
		"""Mengupdate jumlah XXL36 dari Stok Ukuran berdasarkan """
		sql = """
			SELECT 	XXL36, total_stok
			
			FROM 	Stok_Ukuran
			
			WHERE	kode_artikel = '%s'
		""" % kode_artikel
		try:
			self.cursor.execute(sql)
			ukuran = self.cursor.fetchone()
			total_ukuran = 0
			total_stok = 0
			if types == "SUB":
				ukuran_xxl36 = int(ukuran[0]) - int(xxl36)
				total_stok = int(ukuran[1]) - int(xxl36)
			else:
				ukuran_xxl36 = int(ukuran[0]) + int(xxl36)
				total_stok = int(ukuran[1]) + int(xxl36)
			
			sql = """
				UPDATE 	Stok_Ukuran
				
				SET 	XXL36 = %d,
						total_stok = %d
						
				WHERE 	kode_artikel = '%s'
			""" % (ukuran_xxl36, total_stok, kode_artikel)
			
			try:
				self.cursor.execute(sql)
				self.db.commit()
				return True
			except:
				return False
		except:
			return False
	
	def updateStokUkuranXXXL38(self, kode_artikel, xxxl38, types="SUB"):
		"""Mengupdate jumlah XXXL38 dari Stok Ukuran berdasarkan """
		sql = """
			SELECT 	XXXL38, total_stok
			
			FROM 	Stok_Ukuran
			
			WHERE	kode_artikel = '%s'
		""" % kode_artikel
		try:
			self.cursor.execute(sql)
			ukuran = self.cursor.fetchone()
			
			total_ukuran = 0
			total_stok = 0
			if types == "SUB":
				ukuran_xxxl38 = int(ukuran[0]) - int(xxxl38)
				total_stok = int(ukuran[1]) - int(xxxl38)
			else:
				ukuran_xxxl38 = int(ukuran[0]) + int(xxxl38)
				total_stok = int(ukuran[1]) + int(xxxl38)
			
			sql = """
				UPDATE 	Stok_Ukuran
				
				SET 	XXXL38 = %d,
						total_stok = %d
						
				WHERE 	kode_artikel = '%s'
			""" % (ukuran_xxxl38, total_stok, kode_artikel)
			
			try:
				self.cursor.execute(sql)
				self.db.commit()
				return True
			except:
				return False
		except:
			return False
	
	  
	def deleteStokUkuran(self, kodeArtikel):
		"""Menghapus Stok Ukuran berdasarkan Kode Artikel"""
		sql = """
			DELETE
			FROM 	Stok_Ukuran
			WHERE	kode_artikel = '%s'
		  """ % kodeArtikel
		try:
			self.cursor.execute(sql)
			self.db.commit()
			return True
			
		except:
			return False
			self.db.rollback()
      
	def __del__(self):
		self.db.close()
    
 
if __name__ == '__main__':
	msu = ModelStokUkuran()
	msu.updateStokUkuranXL34('ARTTIMN',1, types="NONE")

