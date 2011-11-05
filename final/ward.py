import os,sys,time

scaddress = '/home/cal/cal/judge.py'

def ward():
	str0 = os.popen('ps aux | grep judge').readlines()
	#print str0
	print len(str0)
	if (len(str0) < 3):
		os.popen('/usr/bin/python '+ scaddress)
	

def main():
	while 1: 
		ward()
		time.sleep(15) 

if '__main__' ==__name__:
	main()

