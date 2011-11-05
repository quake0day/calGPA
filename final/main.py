# -*- coding: utf-8 -*-
import csv
import codecs
def calGPA(filename):
	j = 0 
	a = ['优秀','良好','中等','及格']
	b = ['95','85','75','65']
	c = ['90','85','82','78','75','72','68','64','60']
	d = ['4','3.7','3.3','3.0','2.7','2.3','2.0','1.5','1.0']
	k = 0
	fullgrade = 0
	Name = []
	Proportion = []
	changePro = []
	Score = []
	cgp = 0
	T = []
	f = 0
	for line in open(filename):
		t =  (len(line.split("@")) -1) /7
		f = t
		while t != 0:
			jd = float(line.split("@")[j * 7 + 4].strip())
			fullgrade += jd
			Proportion.append(jd)
			zz = line.split("@")[j * 7 + 6].strip()
			for k in [0,1,2,3]:
				if zz == a[k]:
					zz = b[k]		
			score = float(zz)
			Score.append(score)
			t -= 1
			j += 1


	for x in Score:
		for k in [0,1,2,3,4,5,6,7,8]:
			
			tr = (x >= int(c[k]))
			if tr == True:
				changePro.append(d[k])
				break
			
			
	print Score
	print Proportion
	print changePro

	while f > 0:
		cgp += float(Proportion[f - 1]) * float(changePro[f - 1])
		f-=1
	GPA = cgp / fullgrade
	#print GPA
	return GPA
