import os 
import time 
import MySQLdb
import re
import os,sys
from time import sleep

scaddress = '/home/quake0day/calGPA/scoreScanner.py'

def select_id_which_cal():
	try:
			conn =  MySQLdb.connect(host='localhost',user='root',passwd='chensi',db='chensi')
	except Exception, e:
				print e
				sys.exit()
	cur = conn.cursor()
	cur2 = conn.cursor()
	cur3 = conn.cursor()
	sql = "SELECT * FROM  `signup` WHERE  `set` =0 LIMIT 0 , 30"
	cur.execute(sql)
	cur2.execute(sql)
	len_t = len(cur.fetchall())
	cur.close()
	i = 0
	if len_t != 0:
			res = cur2.fetchone()
			cur2.close()
			#if res[j] != None:
				#j++
				#if j !=5
				#continue
			try:
				id = res[0]
			except:
				print "fuck id"
				sys.exit()
			userid = mytrim(res[1])
			passwd = mytrim(res[2])
			dust1 = '/usr/bin/python ' + scaddress
			dust2 = ' ' + userid +' '+ passwd 
			dust = dust1 + dust2
			print dust
			str0 = os.popen(dust)
			if res[1] != '':
				updatewk = "UPDATE `chensi`.`signup` SET `set` = 1 where id= "+ str(res[0]) #when up to return True then change database "0" to "1"
			else:
				print res[0]
				updatewk = "delete from `chensi`.`signup` where id= "+ str(res[0]) #when up to return True then change database "0" to "1"
			try:
				cur3.execute(updatewk)
			except:
				print 'fuckU'
				sys.exit()    
			cur3.close() 
			conn.close()
			i+=1
			time.sleep(2)
	 

							
def main():
	while 1: 
		select_id_which_cal()
		time.sleep(2) 
		
def mytrim(zstr):
	ystr=zstr.lstrip()
	ystr=ystr.rstrip()
	ystr=ystr.strip()
	return ystr
	
if '__main__' ==__name__:
	main()

