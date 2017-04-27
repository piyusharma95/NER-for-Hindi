import codecs
import re
import os 
os.chdir('C:\\Users\\PIYUSH-PC\\Desktop\\VISHNU\\wikiextractor-master\\extracted\\AA')
inputfile=open('wiki_00', 'r', encoding='utf-8')
outputfile=open('new.txt','w',encoding='utf-8')
for line in inputfile:
	line=re.sub('<','',line)
	line=re.sub('>','',line)
	line=re.sub(']','',line)
	line=re.sub('=','',line)
	line=re.sub('/','',line)
	line=re.sub(':','',line)
	line=re.sub('"','',line)
	line.replace('?','')
	line.replace('.','')
	line.replace('|','')
	print(line,file=outputfile,end='')
print('done')