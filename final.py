from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
 
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import subprocess
from bs4 import BeautifulSoup
import requests
import re
import calendar
import time
import math
import re
import requests
from gtts import gTTS
from gtts_token.gtts_token import Token
 
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.edmundson import EdmundsonSummarizer   #found this is the best as 
# it is picking from beginning also while other skip
 
from tkinter import *
import os
 
root = Tk()
 
root.geometry('500x300')
root.title("VideoBeta")

label_0 = Label(root, text="VideoBeta",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="Enter URL : ",width=20,font=("bold", 10))
label_1.place(x=30,y=130)

url1 = Entry(root)
url1.place(x=160,y=130)
url1.config(width=35)

 
def clicked():
	file = open('testfile.txt','a')
	#website to text file as testfile.txt
	html = requests.get(url1.get()).content
	#1 Recoding
	unicode_str = html.decode("utf8")
	encoded_str = unicode_str.encode("ascii",'ignore')
	news_soup = BeautifulSoup(encoded_str, "html.parser")
	title = news_soup.find_all('h1')
	z=[re.sub(r'<.+?>',r'',str(b)) for b in title]
	s1=''.join(z)+'.'+'\n'
	file.write(s1)
 
	#finding the summary of text file and again store it into testfile.txt
	LANGUAGE = "english"
	SENTENCES_COUNT = 10

 
	if __name__ == "__main__":
    
		url=url1.get()
   
		parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    		# or for plain text files
    		# parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    
 
		print ("--LuhnSummarizer--")     
		summarizer = LuhnSummarizer() 
		summarizer = LsaSummarizer(Stemmer(LANGUAGE))
		summarizer.stop_words = ("I", "am", "the", "you", "are", "me", "is", "than", "that", "this",)
		for sentence in summarizer(parser.document, SENTENCES_COUNT):
			str1 = str(sentence)
			file.write(str1)
		file.close()

	#open the text file and divide it into 10 parts as 0 to 9.txt
	str1 = open('testfile.txt', 'r').read()
	#print(str1)
	l = str1.split(".")
	i = len(l)
	for j in range(8):
		file = open('text/'+str(j)+'.txt','a')
		s0= ''.join(l[j])
		file.write(s0)

	
	def _patch_faulty_function(self):
		if self.token_key is not None:
			return self.token_key
		timestamp = calendar.timegm(time.gmtime())
		hours = int(math.floor(timestamp / 3600))

		response = requests.get("https://translate.google.com/")
		line = response.text.split('\n')[-1]
		parsed = re.search("(?:TKK='(?:(\d+)\.(\d+))';)", line)
		a, b = parsed.groups()
		result = str(hours) + "." + str(int(a) + int(b))
		self.token_key = result
		return result


	# Monkey patch faulty function.
	Token._get_token_key = _patch_faulty_function

	# Then call it normally.
	#with open('testfile.txt', 'r') as myfile:
	#   data=myfile.readlines()

	for k in range(8):
		str1 = open('text/'+str(k)+'.txt', 'r').read()
		#print(str1)
		#str1 = "my name is khan"
		if(len(str1)!=0):
			tts = gTTS(str1)
			tts.save('voice/'+str(k)+'.mp3')

	keyword = open('text/0.txt', 'r').read()
	#print(keyword)
	st = 'googleimagesdownload --keywords "'+keyword+'" --limit 8'
	    
	os.system(st)
	os.system("D:/VideoBeta/VideoBeta.exe")

	#num=0
	#for filename in os.listdir("."):
    	#	if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        #		os.rename(filename, str(i)+".jpg")
        #		num=num+1


 
Button(root, text='Submit',width=20,bg='green',fg='white', command=clicked).place(x=180,y=190)

root.mainloop()
