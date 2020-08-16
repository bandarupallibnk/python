import datetime
import time



class cl_date():
	def __init__(self):
		today = datetime.date.today()
		self.currentdate =  today.strftime('%Y%m%d')


	def fcurrentdate(self):
		return self.currentdate