from ConnectorMySQL import *
import string

class ModelArtikel(ConnectorMySQL):
	
	def __init__(self):
	  """Membuat koneksi pertama"""
	  ConnectorMySQL.__init__(self)
		
	def createArtikel(self, *args):
		"""Memasukan data Artikel"""
		sql = """
		INSERT INTO Artikel
		VALUES('%s','%s','%s','%s','%s','%s')
		""" % args[0]
      
		try:
			self.cursor.execute(sql)
			self.db.commit()
			return True
		except:
			return False
			self.db.rollback()
		
		
	def readArtikel(self):
	  """Membaca data Artikel"""
	  sql = """
        SELECT  A.kode_artikel, 
                K.nama_kategori, 
                S.total_stok, 
                A.nama_artikel,
                A.harga_jual,
                A.stok_minimum
        
        FROM    Artikel as A, 
                Kategori as K, 
                Stok_Ukuran as S
                
        WHERE   K.kode_kategori = A.kode_kategori
        
        AND     A.kode_artikel = S.kode_artikel
        
        ORDER BY    A.nama_artikel
        """
	  
	  try:
	    self.cursor.execute(sql)
	    results = self.cursor.fetchall()
	    return results
	  except:
	    return False
	
	def readArtikelFromKodeArtikel(self, kodeArtikel):
		"""Membaca data Artikel dari Kode Artikel"""
		sql = """
			SELECT 	A.nama_artikel,
					A.kode_kategori,
					K.nama_kategori,
					S.S28,
					S.M30,
					S.L32,
					S.XL34,
					S.XXL36,
					S.XXXL38,
					S.total_stok,
					A.stok_minimum,
					A.harga_modal,
					A.harga_jual
			FROM	Artikel as A,
					Kategori as K,
					Stok_Ukuran as S
					
			WHERE	A.kode_artikel = '%s' 
			
			AND		A.kode_kategori = K.kode_kategori 
			
			AND		S.kode_artikel = A.kode_artikel
		""" % kodeArtikel
		
		try:
			self.cursor.execute(sql)
			result = self.cursor.fetchone()
			return result
		except:
			return False
	
	def readArtikelStokMin(self):
		"""Membaca artikel di bawah stok minimum"""
		sql = """
		SELECT 	A.kode_artikel, K.nama_kategori, A.nama_artikel, 
				A.harga_jual, SK.total_stok, A.stok_minimum
		FROM 	Artikel as A, Kategori as K, Stok_Ukuran as SK
		WHERE 	A.kode_kategori = K.kode_kategori
		AND 	SK.kode_artikel = A.kode_artikel
		AND 	SK.total_stok <= A.stok_minimum
		"""		
		try:
			self.cursor.execute(sql)
			results = self.cursor.fetchall()
			return results
		except:
			return False
			
	def __readArtikelFromKodeKategori(self, kode_kategori):
		"""Membaca Kode Artikel dari kode_kategori"""
		# mendapatkan semua kode artikel 
		# dari kode kategori yang akan dihapus
		sql_alternatif = """
				SELECT 	kode_artikel 
				
				FROM	Artikel
				
				WHERE 	kode_kategori = '%s' 
				""" % kode_kategori
		try:
			self.cursor.execute(sql_alternatif)
			return self.cursor.fetchall()
		except:
			return False
	
	def updateArtikel(self, kodeArtikel, *args):
	  """Mengupdate data Artikel"""
	  data = args + (kodeArtikel,)

	  sql = """
	    UPDATE	Artikel
	    
	    SET		kode_kategori = '%s',
				nama_artikel = '%s',
				harga_modal = '%s',
				harga_jual = '%s',
				stok_minimum = '%s'
			
	    WHERE 	kode_artikel = '%s'
	  """ % data
	  
	  try:
	    self.cursor.execute(sql)
	    self.db.commit()
	    return True
	  except:
	    return False
	    self.db.rollback()

	def updateArtikelWhenKategoriDelete(self, kode_kategori):
		"""Mengubah data Artikel bagian Kode Kategori ke default 
		ketika Kategori yang bersangkutan telah dihapus"""
		
		results = self.__readArtikelFromKodeKategori(kode_kategori)
		'''
		for kode_artikel in results:
			print kode_artikel[0]
		'''
		status = False
		if results:
			for kode_artikel in results:
				
				sql = """
						UPDATE 	Artikel
					
						SET		kode_kategori = 'KTGDFT'
					
						WHERE	kode_artikel = '%s'
					""" % kode_artikel[0]
			
				try:
					self.cursor.execute(sql)
					self.db.commit()
					status = True
				except:
					status = False
					self.db.rollback()
		
			return status
		else:
			return True


	def deleteArtikel(self, kodeArtikel):
	  """Menghapus data Artikel"""
	  sql = """
	    DELETE 
	    FROM 	Artikel
	    WHERE	kode_artikel = '%s'
	  """ % kodeArtikel
	  
	  try:
	    self.cursor.execute(sql)
	    self.db.commit()
	    return True
	  except:
	    return False
	    self.db.rollback()
	
	def searchArtikel(self, namaArtikel):
		"""Mencari data Artikel berdasarkan nama Artikel"""
		nilai_pencarian = {'nama_artikel':namaArtikel}
		
		# Templating Sistem
		sql_template = string.Template(
		"""
        SELECT  A.kode_artikel, 
                K.nama_kategori, 
                S.total_stok, 
                A.nama_artikel,
                A.harga_jual,
                A.stok_minimum
        
        FROM    Artikel as A, 
                Kategori as K, 
                Stok_Ukuran as S
                
        WHERE   K.kode_kategori = A.kode_kategori
        
        AND     A.kode_artikel = S.kode_artikel
        
        AND 	A.nama_artikel LIKE '%$nama_artikel%'
        
        ORDER BY    A.nama_artikel
        """)
        
		sql = sql_template.substitute(nilai_pencarian)
		
		try:
			self.cursor.execute(sql)
			results = self.cursor.fetchall()
			return results
		except:
			return False
			
			
	def searchArtikelStokMin(self, pencarian):
		"""Mencari artikel di bawah stok minimum berdasarkan nama"""
		
		data = {"cari":pencarian}
		
		sql_template = string.Template("""
		SELECT 	A.kode_artikel, K.nama_kategori, A.nama_artikel, 
				A.harga_jual, SK.total_stok, A.stok_minimum
		FROM 	Artikel as A, Kategori as K, Stok_Ukuran as SK
		WHERE 	A.kode_kategori = K.kode_kategori
		AND 	SK.kode_artikel = A.kode_artikel
		AND 	SK.total_stok <= A.stok_minimum
		AND 	A.nama_artikel LIKE '%$cari%'
		""")
		
		sql = sql_template.substitute(data)
		
		try:
			self.cursor.execute(sql)
			results = self.cursor.fetchall()
			return results
		except:
			return False
	    
	def __del__(self):
	  try:
	    self.db.close()
	  except:
	    return False
	    
	

	
'''
ma = ModelArtikel()
data = ('ART456','KTG90','Artikel Testoing','12','56','8')
data = ma.updateArtikelWhenKategoriDelete('KTGDFT')
'''
