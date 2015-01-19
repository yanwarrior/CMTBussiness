from ConnectorMySQL import *

class ModelPengguna(ConnectorMySQL):
	
	def __init__(self):
		"""Membuat koneksi pertama untuk Pengguna"""
		ConnectorMySQL.__init__(self)
		
	def readPengguna(self):
		"""Membaca nama_pengguna (username)"""
		sql = "SELECT kode_pengguna, email, kata_sandi FROM Pengguna"
		try:
			self.cursor.execute(sql)
			kode_pengguna = self.cursor.fetchone()
			return kode_pengguna
		except:
			return False
			
	def readDataPengguna(self):
		"""Membaca nama_pengguna (username)"""
		sql = "SELECT kode_pengguna FROM Pengguna"
		try:
			self.cursor.execute(sql)
			kode_pengguna = self.cursor.fetchone()
			return kode_pengguna[0]
		except:
			return False
			
	def updatePengguna(self, email, password, kode_pengguna):
		sql = """
		
			UPDATE 	Pengguna
			SET		email = '%s',
					kata_sandi = '%s'
			WHERE	kode_pengguna = '%s'
		""" % (email, password, kode_pengguna)
		
		try:
			self.cursor.execute(sql)
			self.db.commit()
			return True
		except:
			return False
			
	def __del__(self):
	  try:
	    self.db.close()
	  except:
	    return False
