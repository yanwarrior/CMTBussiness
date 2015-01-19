from ConnectorMySQL import *

class ModelDetilTransaksi(ConnectorMySQL):
	
	def __init__(self):
		"""Membuat koneksi pertama untuk Detil Transaksi"""
		ConnectorMySQL.__init__(self)
		
	def createDetilTransaksi(self, *args):
		"""Membuat Data Detil Transaksi"""
		sql = """
			INSERT INTO Detil_Transaksi
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

