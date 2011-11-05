# -*- coding: utf-8 -*-
from conn import connMysql
import MySQLdb




GPA = [0,0]
j = 0 
a = ['优秀','良好','中等','及格','免修']
b = ['95','85','75','65','0']
c = ['90','85','82','78','75','72','68','64','60','0']
d = ['4','3.7','3.3','3.0','2.7','2.3','2.0','1.5','1.0','0']
k = 0
fullgrade = 0
Name = []
Proportion = []
changePro = []
Score = []
cgp = 0
T = []
f = 0
	
conn = connMysql()
cur = conn.cursor()
sql = "SELECT score FROM  `signup` WHERE id = '" + '271'  + "'"
cur.execute(sql)
t = cur.fetchall()

b = t[0][0]
print b
d = b.split("@")
print d[2]
t =  (len(d) -1) /7
print t
z = d[2*7+6]
print z
cur.close()
conn.close()

	
