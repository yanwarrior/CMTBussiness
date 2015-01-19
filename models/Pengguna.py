import MySQLdb
from DBConf import *

class Pengguna:
	def __init__(self):
		'''
		Models Class For Pengguna
		'''
		self.db			= DBConf()
		self.dataDB		= self.db.getProperty()
		self.host 		= self.dataDB['host']
		self.user		= self.dataDB['user']
		self.pswd		= self.dataDB['pass']
		self.dbnm		= self.dataDB['dbnm']
		
	def __connected(self):
		# login create
		dbm     	= MySQLdb.connect( \
										self.host,\
                                        self.user,\
                                        self.pswd,\
                                        self.dbnm )
                                        
        cursor  	=  dbm.cursor()
        
        data 		= {"dbm":dbm,"cur":cursor}
        
        return data
        
		
	def loginAuth(self, kodePengguna, kataSandi):
		'''
		method for authentication Pengguna 
		when Pengguna login in yout App
		'''
		db		= self.__connected()
		sql 	= """
		SELECT 	* 
		FROM	Pengguna
		WHERE	kode_pengguna 	= '%s' 
		AND		kata_sandi		= '%s' 
		""" % \
		(kodePengguna.upper(), kataSandi)
		
		try:
			db['cur'].execute(sql)
			results = db['cur'].fetchone()
			print results
		except:
			print "error"
		finally:
			db['dbm'].close()
			
		
		
		
pgn = Pengguna()
pgn.loginAuth("PGN9999","123qwe")


