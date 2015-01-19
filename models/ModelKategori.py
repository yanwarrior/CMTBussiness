from ConnectorMySQL import *

class ModelKategori(ConnectorMySQL):
	
	def __init__(self):
	  """Membuat koneksi pertama untuk Kategori"""
	  ConnectorMySQL.__init__(self)
	
	def createKategori(self, *args):
	  """Menambahkan data Kategori"""
	  sql = """
	    INSERT INTO		Kategori
	    VALUES 		('%s','%s')""" %\
	  args
	  
	  try:
	    self.cursor.execute(sql)
	    self.db.commit()
	    return True
	  except:
	    return False
	    self.db.rollback()
	  
	def readKategori(self):
	  """Membaca data kategori"""
	  sql = """SELECT * FROM Kategori WHERE kode_kategori != 'KTGDFT'"""
	  
	  try:
	    self.cursor.execute(sql)
	    results = self.cursor.fetchall()
	    return results
	  except:
	    return False
	
	def readNamaKategori(self, kodeKategori):
		sql = """
		SELECT 	nama_kategori
		FROM 	Kategori
		WHERE 	kode_kategori='%s'
		""" % kodeKategori
		try:
			self.cursor.execute(sql)
			results = self.cursor.fetchone()
			return results
		except:
			return False
	
	def updateKategori(self,kodeKategori, *args):
	  """Mengupdate Kategori berdasaekan kodeKategori"""
	  
	  data = args + (kodeKategori,)
	  sql = """
	    UPDATE	Kategori
	    SET 	nama_kategori='%s'
	    WHERE	kode_kategori='%s'
	  """ % data
	  
	  try:
	    self.cursor.execute(sql)
	    self.db.commit()
	    return True
	  except:
	    return False
	    self.db.rollback()
	
	def deleteKategori(self, kodeKategori):
	  """Menghapus data Kategori berdasarkan kode kategori"""
	  sql = """
	    DELETE	
	    FROM	Kategori
	    WHERE	kode_kategori='%s'
	  """ % kodeKategori
	  
	  try:
	    self.cursor.execute(sql)
	    self.db.commit()
	    return True
	  except:
	    return False
	    self.db.rollback()
	
	def __del__(self):
	  try:
	    self.db.close()
	  except:
	    return False
