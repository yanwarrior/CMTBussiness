import MySQLdb

class ConnectorMySQL:
	def __init__(self):
		self.db = MySQLdb.connect("localhost","root",
								"junox", "penjualan")
		self.cursor = self.db.cursor()
