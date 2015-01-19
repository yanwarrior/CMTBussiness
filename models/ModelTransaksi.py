from ConnectorMySQL import *

class ModelTransaksi(ConnectorMySQL):
	
	def __init__(self):
		"""Membuat koneksi pertama untuk Transaksi"""
		ConnectorMySQL.__init__(self)
		
	def readTransaksiFromDate(self, date_from, date_to):
		"""Membaca data transaksi untuk omzet"""
		sql = """
		
			SELECT kode_transaksi, total
			FROM Transaksi
			WHERE tanggal >='%s' AND tanggal <= '%s'
		
		""" % (date_from, date_to)
		
		try:
			self.cursor.execute(sql)
			results = self.cursor.fetchall()
			return results
		except:
			return False
		
	def createTransaksi(self, *args):
		"""Membuat Data Transaksi"""
		sql = """
			INSERT INTO Transaksi
			VALUES('%s','%s','%s','%s','%s','%s')
		""" % args
		
		try:
			self.cursor.execute(sql)
			self.db.commit()
			return True
		except:
			self.db.rollback()
			return False
	
		
	def __del__(self):
	  try:
	    self.db.close()
	  except:
	    return False

