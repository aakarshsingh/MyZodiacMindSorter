from os import listdir
from os.path import isfile, join
from pytesser import *
import re
import shutil
import os

# Zodiac Mind - zodiacmind.com
# I first ran a test with 1000 images as test data to see how Tesseract is reading the images
# Based on this, I generalized cases for each sun sign

def hammer (str1,str2):
	if len(str2)!=len(str1) or str2 is "leo":
		return 0
	else:
		count=0
		for i in range(0,len(str1)):
			if str1[i]!=str2[i]:
				count=count+1
		if count is 1:
			print "Hammed because of "+str1
			return 1
	return 0

mypath="\data"

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

nums = [0,1,2,3,4,5,6,7,8,9,10,11,12]
out = ["00"] * 13
wnum = [0]*13
for i in nums:
		out[i] = "outdata\\" + str(i+1) + "\\"

real = ["aries","taurus","gemini","cancer","leo","virgo","libra","scorpio","sagittarius","capricorn","aquarius","pisces"]
matched = ["aries","taurus","gemini","cancer","leo","v\w{2,3}o","libra","scorpio|sco","sa\w{1,4}~?\w{1,4}us","capricorn","a\w{4,5,6}us|aquarius","p\w{4,5}s"]

loopvar = 0
count = 0
wcount = 0

outFile = open("out.txt", 'w')

for s in onlyfiles:
	wcount = wcount + 1
	if wcount % 50 is 0:
		print "***********"
		print "Current Stats"
		print "Success = "+str(wcount-wnum[12])
		print "Total = "+str(wcount)
		per=(((wcount-wnum[12])*1.0/wcount*1.0)*100.00)
		print "Percentage = "+str(per)
		print "***********"
		print "\n"
	s=mypath+"\\" + s
	image = Image.open(s)  
	image = image.convert('L')
	imageText = image_to_string(image).lower()
	flag = 0


	for loopvar in range(0,12) : 

		#Normal Sign Name and Regex Code
		#Regex Code is needed because some signs are almost never matched to their original form
		textFound=re.findall(matched[loopvar], imageText)
		if len(textFound) > 0 : 
			wnum[loopvar]=wnum[loopvar]+1
			print "Direct Match : "+real[loopvar]
			print "Total Here : "+str(wnum[loopvar])
			print "\n"
			shutil.copy2(s, out[loopvar])
			flag=1

		#Match because of a Hamming Distance of 1
		#Test Data Analysis showed that many matches will happen because of a Hamming Distance Logic
		words = imageText.split() 
		for word in words:
			if hammer(word,real[loopvar]):
				wnum[loopvar]=wnum[loopvar]+1
				count = count + 1
				print "Hammed Match : "+real[loopvar]
				print "Total Here : "+str(wnum[loopvar])
				print str(count)+" out of "+str(wcount)+" sorted because of Hamming Distance"
				print "\n"
				flag=1
				shutil.move(s,out[loopvar])

	#This is the case for no match			
	if not flag:		
		wnum[12]=wnum[12]+1
		print "No Match"
		print "Total Here : "+str(wnum[12])
		outFile.write(s+"\n")
		outFile.write(imageText+"\n") 
		outFile.write("\n")
		print "\n"
		

print matched
print wnum

outFile.close()