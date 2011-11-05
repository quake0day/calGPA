# -*- coding: utf-8 -*-
# 作者 陈思 康孜雯
# 测控061
# 课程设计

# 使用方法： python xxx(文件名).py 参数1 参数2 参数3 参数 4
# 参数1： 学生学号 参数2: 学生学号对应密码
# 参数3 : 要接收成绩的手机号 参数4：对应的飞信登陆密码

import urllib,urllib2,cookielib
import re
import MySQLdb
import os,sys,filecmp,shutil
from BeautifulSoup import BeautifulSoup
from main import calGPA
from conn import connMysql
from trim import trim
import hashlib

sedaddress = "' /home/quake0day/gpa/quake" 
 
# 通过urllib查询成绩，并将返回的HTML代码转换成为具有可读性的成绩信息
# 输入学号 密码 返回对应学期的课程名称和成绩
# 该函数使用了saveFile和changeFile这两个函数 具体过程参见这两个函数说明

def scoreScanner(username,password,id):
	a_jar = cookielib.CookieJar()
	b_jar = urllib2.build_opener(urllib2.HTTPCookieProcessor(a_jar))
	urllib2.install_opener(b_jar)
	dust1 = 'http://202.205.91.54:8000/forward.jsp?zjh='
	dust2 = username
	dust3 = '&mm='
	dust4 = password
	dust5 = '&yhlbdm=01'
	try:
		response = urllib2.urlopen(dust1+dust2+dust3+dust4+dust5)
		t = len(response.read())
		if t > 2111:    #如果帐号密码错误！
			return 2
			sys.exit()
	except Exception,e:
		sys.exit()
		return 1
	else:
		next = urllib2.urlopen("http://202.205.91.54:8000/gradeLnAllAction.do?type=ln&oper=qbinfo")
		#print len(next.read())
		doc = next.read()
		docc = unicode(doc,'gb2312','ignore').encode('utf-8','ignore')
		soup = BeautifulSoup(''.join(docc)) 
		score_raw = str(soup)
		#print score_raw
		saveFile(username,score_raw)    
		changeFile(username)
		saveFileToDatabase(username,password,id)
		return 0  

    

    #print final_score

# 发送短信函数，调用PyFetion库 直接给自己手机发送信息
# 接收参数 手机号 飞信密码 要发送的数据
# 返回参数 无

def sendSMS(phone_num,passwd,data):
    fetion = PyFetion(phone_num,passwd,'HTTP')
    i = 0
    fetion.login(FetionOnline)
    fetion.send_sms(data)
    fetion.logout()


# 保存临时文件函数 传入参数 用户名（用来生成文件） 原始数据（即从网上抓取的成绩混合html代码）  
def saveFile(username,score_raw):
    newfile = open(username,'w')
    newfile.write(score_raw)
    newfile.close()

# 成绩提取函数，传入参数：用户名（用来对应saveFile所生成的文件）返回可读成绩
# 对saveFile说生成的文件进行处理 调用sed.sh脚本
# 对应处理过程见sed.sh
# 现有问题：对于第一次查询的号码 貌似sudo chmod +x 这句话不能很好执行 必须执行两次这个函数才行 需要进一步修改    
def changeFile(username):
    file = username + '_get'
    file1 = "file1='" + username + "'"
    com1 = "sed 1'i\\"+ file1 + sedaddress
    str1 = os.popen(com1).read()
    createfile = open(file,'w')
    createfile.write(str1)
    createfile.close()
    str2 = os.popen('sudo chmod 777 ' + file) 
    str3 = os.popen('sh ' + file).read()
    #score_final = os.popen('cat ' + username + '_1').read()
    #print score_final
    #return score_final
    
def saveFileToDatabase(username,passwd,id):
	newfile = open(username+'_1','r')
	data = newfile.read()
	#print data[1]
	print "here"
	data = trim(data)
	print "here"
	conn = connMysql()
	cur = conn.cursor()
	#sql="insert into signup (username,passwd,score) values (%s,%s,%s)"
	sql = "UPDATE signup SET score ='"+ data +"' where id = '" + id  + "'" 
	#print sql
	#param = (username,passwd,data)
	
	cur.execute(sql)
	print "here"
	cur.close()
	conn.close()
	
# 保存成绩函数 传入参数 用户名 要保存的数据
# 连接数据库 存入最新一次的成绩
# 该函数通过判断这次获取的成绩数据对应的md5值和原有数据的md5值来确定
# 是否两次成绩一致， 如果一致 则说明没必要发送短信通知
# 返回值 1： 需要发送短信  0： 不需要发送短信
def saveScore(username,passwd,info_data):
		conn = connMysql()
		#cur = conn.cursor()
		cur = conn.cursor()
		sql_a = str(info_data[0])
		sql_b = str(info_data[1])
		print sql_a
		sql1 = "UPDATE signup SET info_data ='"+ sql_a +"' where userid = '" + username  + "' AND passwd= '"+ passwd + "'" 
		sql2 = "UPDATE signup SET fullgrade ='"+ sql_b +"' where userid = '" + username  + "' AND passwd= '"+ passwd + "'" 
		#print sql_0
		cur.execute(sql1)
		cur.execute(sql2)
		cur.close()
		conn.close()
		return 1


# 主函数 程序从这里开始执行
if __name__ == '__main__':
	try:
		username = sys.argv[1]
		passwd = sys.argv[2]
		id = sys.argv[3]
	except IndexError,e:
		sys.exit()
	k = scoreScanner(username,passwd,id)
	if k == 0 :
		#proFile = username + '_1'
		GPA = calGPA(username,passwd,id,0)
		a = saveScore(username ,passwd,GPA)
	print k
	#if (a == 1):
#		sendSMS(phone_num,phone_passwd,final_s)

