import psycopg2

class pg_conn():
	def __init__(self):
		pass

	def newconn(self,host,database,user,password):
		conn = psycopg2.connect(host = host,
			database=database,
			user = user,
			password = password
			)