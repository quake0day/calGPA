# -*- coding: utf-8 -*-
import csv
import codecs
from conn import connMysql
import MySQLdb
#计算GPA的主文件，读取数据库中的成绩并最终计算出GPA
#该函数最终返回计算出的GPA
GPA = [0,0]
def calGPA(username,passwd,id,mode):
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
	sql = "SELECT score FROM  `signup` WHERE id = '" + id  + "'"
	cur.execute(sql)
	temp = cur.fetchall()
	print temp
	cur.close()
	conn.close()
	wholedata = temp[0][0]
	data = wholedata.split("@")

	t =  (len(data) -1) /7 #判断一共有多少门课程
	f = t #用f来保存课程总数
	while t != 0:
		zz = data[j * 7 + 6].strip() #从filename中取出成绩
		print zz
		if zz != a[4]: #如果没有免修的科目
			for k in [0,1,2,3]: #判断是否有需要转换五级分制的成绩
				if zz == a[k]:
					zz = b[k]	#将五级分制的成绩替换为相应的百分制			
			jd = float(data[j * 7 + 4].strip()) #取出绩点
			fullgrade += jd #计算学分总数
			Proportion.append(jd) #将学分单独存放在一个数组中
			score = float(zz)
			Score.append(score)  #将成绩单独存放在另外一个数组中
		else:
			f -= 1 # 如果存在免修的情况 课程数要减去一，同时忽略该课程
		t -= 1 #更改课程数量，直到处理完毕
		j += 1 

 #循环读取成绩，计算成绩对应的绩点，并将其保存到一个新数组中
	for x in Score:
		for k in [0,1,2,3,4,5,6,7,8,9]:
			
			tr = (x >= int(c[k]))
			if tr == True:
				changePro.append(d[k])
				break
			
	#DEBUG时使用		
	#print Score
	#print Proportion,
	#print changePro

#按照公式计算GPA
	while f > 0:
		cgp += float(Proportion[f - 1]) * float(changePro[f - 1])
		f-=1
	GPA [0]= cgp / fullgrade
	GPA [1] = fullgrade
	return GPA

