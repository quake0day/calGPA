# -*- coding: utf-8 -*-
import os 
import time 
import MySQLdb
import re
import os,sys
from time import sleep
from conn import connMysql
import threading
from popen import _popen

scaddress = '/home/quake0day/gpa/scoreScanner.py'

childthreads = []

def select_id_which_cal():
	conn2 = connMysql()
	cur = conn2.cursor()
	sql = "SELECT * FROM  `signup` WHERE  `set` =0 LIMIT 0 , 30"
	cur.execute(sql)
	data = cur.fetchone()
	conn2.close()
	return data
		
		
def do_calGPA(id,userid,passwd):
	conn3 = connMysql()
	cur = conn3.cursor()
	dust1 = '/usr/bin/python ' + scaddress
	dust2 = ' ' + userid +' '+ passwd + ' '+ str(id)
	dust = dust1 + dust2
	print dust # 打印执行的语句
	try:
		str0 = int(_popen(dust).read())
		sleep(5)
	except:
		str0 = 1
	print str0
	if str0 != 2:
		if userid != '':
			updatewk = "UPDATE `chensi`.`signup` SET `set` = 1 where id= "+ str(id) #when up to return True then change database "0" to "1"
		else:
			updatewk = "delete from `chensi`.`signup` where id= "+ str(id) #when up to return True then change database "0" to "1"
	else:
		updatewk = "UPDATE `chensi`.`signup` SET `set` = 2 where id= "+ str(id)
	try:
		cur.execute(updatewk)
	except:
		print 'fuckU'	
	cur.close()
	conn3.close() 
	print "Done."		
					
def main():
	while 1:
		sleep(1)
		data = select_id_which_cal()
		print data
		try:
			count = len(data)
		except:
			count = 0 
		if count != 0:
			try:
				id = data[0]
			except:
				print "fuck id"
			userid = mytrim(data[1])
			passwd = mytrim(data[2])	
			t = threading.Thread(target = do_calGPA(id,userid,passwd), name = "childThread- %d")
			t.setDaemon(1)
			t.start()
			#childthreads.append(t)
			#for t in childthreads:
				#t.join()

def mytrim(zstr):
	ystr=zstr.lstrip()
	ystr=ystr.rstrip()
	ystr=ystr.strip()
	return ystr
	
if '__main__' ==__name__:
	main()

