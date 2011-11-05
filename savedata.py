from conn import connMysql
def saveFileToDatabase(username,passwd):
	newfile = open(username+'_1','r')
	data_raw = newfile.read()
	data = unicode(data_raw,'gb2312','ignore').encode('utf-8','ignore')
	conn = connMysql()
	cur = conn.cursor()
	sql = "UPDATE signup SET score ='"+ data +"' where userid = '" + username  + "' AND passwd= '"+ passwd + "'" 
	print sql
	cur.execute(sql)
	cur.close()
	conn.close()


saveFileToDatabase('0901081109_1','19900427')
