import codecs
import re
import time
import os 
os.chdir('files//wiki_00.txt')
inputfile=open('wiki_00.txt', 'r', encoding='utf-8')
outputfile=open('new1.txt','w',encoding='utf-8')
pfn=open('sample.txt','r',encoding='utf-8')
pread=pfn.read()
psplit=pread.split("\n")
txt=" ".join(psplit)
iread=inputfile.read()
isplit=iread.split("\n")
for words in isplit:
	ss=words.split(" ")
	for word in ss:
		word=re.sub('<','',word)
		word=re.sub('>','',word)
		word=re.sub(']','',word)
		word=re.sub('=','',word)
		word=re.sub('/','',word)
		word=re.sub(':','',word)
		word=re.sub('"','',word)
		word=re.sub('\.','',word)
		word=re.sub(',','',word)
		word=re.sub(';','',word)
		word=re.sub('\[','',word)
		word=re.sub('{','',word)
		word=re.sub('}','',word)
		word=re.sub('\+','',word)
		word=re.sub('-','',word)
		word=re.sub('_','',word)
		word=re.sub('\*','',word)
		word=re.sub('&','',word)
		word=re.sub('^','',word)
		word=re.sub('%','',word)
		word=re.sub('$','',word)
		word=re.sub('#','',word)
		word=re.sub('@','',word)
		word=re.sub('~','',word)
		word=re.sub('`','',word)
		if(re.search("[0-9]+",word)):
			word=re.sub("[0-9]+","",word)
		if(re.search("[a-zA-Z]+",word)):
			word=re.sub("[a-zA-Z]+","",word)		
		if(re.search(" "+word+" ",txt) and not re.search(" "+" ",txt)):
			print(word+"_pfn ",file=outputfile,end='')
		else:
			print(word+" ",file=outputfile,end='')	
print('done')
num = input('how long to wait')