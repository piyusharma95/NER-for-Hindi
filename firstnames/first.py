import codecs
import re
import os 
os.chdir('C:\\Users\\Piyush\\Desktop\\VISHNU\\firstnames')
inputfile=open('2.txt', 'r', encoding='utf-8')
outputfile=open('new.txt','w',encoding='utf-8')
for line in inputfile:
	print("a")
	line=line.decode("utf-8", "ignore")
	line=re.sub('<','',line)
	line=re.sub('>','',line)
	line=re.sub(']','',line)
	line=re.sub('=','',line)
	line=re.sub('/','',line)
	line=re.sub(':','',line)
	line=re.sub('"','',line)
	line=re.sub('\?','',line)
	line=re.sub('\.','',line)
	if(re.search("[a-zA-Z]+",line)):
		line=re.sub("[a-zA-Z]+","",line)
	print(line,file=outputfile,end='')
print('done')