#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
def calc(*nums):
	sum = 0
	for n in nums:
		sum = sum + n * n
	return sum

def sums_1(*sum):
	def sums_2():
		sums = 0
		for n in sum:
			sums = sums + n
		return sums
	return sums_2


def count():
	fs = []
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs
def build(x,y):
	return lambda:x*x+y*y

def log(func):
	def wrapper(*args, **kw):
		print 'call %s():' %func.__name__
		return func(*args,**kw)
	return wrapper
@log
def now():
	print '201505'



def print_lol(list1,level):
	for val in list1:
		if isinstance(val,list):
			print_lol(val,level+1)
		else:
			for tab_stop in xrange(level):
				print("\t"),
			print(val)


def read_txt():
	print(os.getcwd())	
	data = open('test.txt')
	list_c = data.readlines()
	print list_c
	testdata=[]
	for content in data:
		(con1,con2) = content.split(':')
		print(con1),
		print('said'),
		print(con2),
		testdata.append(con1)
	data.close()
	testdata.append('abc')
	#print(testdata)


def WRFunction():
	ReadData = []
	
	try:
		data = open('ReadTxt.txt')
		#print(data)
		for eachLine in data:
			try:
				ReadData.append(eachLine)
				#print(eachLine),
			except Exception, e:
				pass
	except Exception, e:
		pass
	finally:
		data.close()
	print(ReadData)
	try:
		data = open('ReadTxt.txt').read()
		writeData = open('WriteTxt.txt', 'w')
		writeData.write(data)
	except Exception, e:
		
		print('error')
	finally:
		writeData.close()


passline = 60
def func (val):
	if val>passline:
		print 'pass'
	else:
		print 'failed'
	def in_func():
		print val
	in_func()
	return in_func

def set_passline(passline):
	def cmp(val):
		if val<passline:
			print('failed')
		else:
			print('pass')
	return cmp


def my_average(*arg):
	return sums(arg)/len(arg)

def dec(fun):
	print('dec run')
	def in_dec(*arg):
		print('in_dec run')
		if len(arg) == 0:
			return 0
		for val in arg:
			if not isinstance(val, int):
				return 0

		return fun(*arg)
	return in_dec

@dec
def my_sum(*arg):
	print ('my_sum run')
	return sum(arg)
