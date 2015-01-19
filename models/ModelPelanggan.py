from ConnectorMySQL import *
import string

class ModelPelanggan(ConnectorMySQL):
	
	def __init__(self):
		"""Membuat koneksi pertama untuk Pelanggan"""
		ConnectorMySQL.__init__(self)
		
	def createPelanggan(self, *args):
		"""Menambahkan data Pelanggan"""
		sql = """
		INSERT INTO 	Pelanggan
		VALUES ('%s','%s','%s','%s','%s','%s')
		""" % args
		
		try:
			self.cursor.execute(sql)
			self.db.commit()
			return True
		except:
			return False
			self.db.rollback()
	
	def readPelanggan(self):
		"""Membaca data Pelanggan"""
		sql = """SELECT * FROM Pelanggan"""
		
		try:
			self.cursor.execute(sql)
			results = self.cursor.fetchall()
			return results
		except:
			return False
			
	def readNamaPelanggan(self, kode_pelanggan):
		"""Membaca nama pelanggan berdasarkan kode pelanggan"""
		sql = """
			SELECT 	nama_pelanggan
			
			FROM 	Pelanggan
			
			WHERE	kode_pelanggan = '%s'
		
		""" % kode_pelanggan
		
		try:
			self.cursor.execute(sql)
			result = self.cursor.fetchone()
			return result
		except:
			return False
			
	def updatePelanggan(self, kode_pelanggan, *args):
		"""Mengubah data Pelanggan"""
		
		data = args + (kode_pelanggan,)
		sql = """
			UPDATE		Pelanggan
			
			SET			nama_pelanggan = '%s',
						email = '%s',
						jenis_kelamin = '%s',
						hp = '%s',
						alamat = '%s'
						
			WHERE		kode_pelanggan = '%s'
		""" % data
		
		try:
			self.cursor.execute(sql)
			self.db.commit()
			return True
		except:
			return False
			self.db.rollback()
		
			
	def deletePelanggan(self, kode_pelanggan):
		"""Menghapus data pelanggan"""
		sql = """
			DELETE
			FROM Pelanggan
			WHERE kode_pelanggan = '%s'
		""" % kode_pelanggan
		
		try:
			self.cursor.execute(sql)
			self.db.commit()
			return True
		except:
			return False
			self.db.rollback()
			
	def searchPelanggan(self, nama_pelanggan):
		"""Mencari data pelanggan"""
		data = {"pencarian":nama_pelanggan}
		
		sql_template = string.Template("""
			SELECT 	*
			
			FROM	Pelanggan
			
			WHERE 	nama_pelanggan 
			
			LIKE	'%$pencarian%'
		""")
		
		sql = sql_template.substitute(data)
		
		try:
			self.cursor.execute(sql)
			results = self.cursor.fetchall()
			return results
		except:
			return False
			
	
	def __del__(self):
		self.db.close()
