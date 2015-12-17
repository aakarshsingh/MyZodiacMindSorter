from os import listdir
from os.path import isfile, join
from pytesser import *
import re
import shutil
import os

# After running RipperScript, I could sort about 13000 of the 16000 images
# The rest responses were stored in a text file, which when studied show that certain regexs will result in succesful matches
# After running the following regexs, about 700 images were left. Those responses are there in out.text


mypath="C:\Users\ACER\Desktop\Poetry\MyZodiacMindSorter\data"

matched = ["aries","taurus","gemini","cancer","leo","virgo","libra","scorpio","sagittarius","capricorn","aquarius","pisces"]
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
nums = [0,1,2,3,4,5,6,7,8,9,10,11,12]
out = ["00"] * 13
arrlen = [0]*13
wnum = [0]*13
for i in nums:
		out[i] = "outdata\\" + str(i+1) + "\\"
		
count = 1


arr0=[]
arr1=["tau( )?(n|r)us"]
arr2=[]
arr3=["(c|i)anc(s|e)r"]
arr4=["u[a-z]{2}"]
arr5=["v[a-z]{1,2}eo","(v|w)[a-z]{2}o?o"]
arr6=["libri","usra"]
arr7=["seerpiq","sco[a-z]{4,6}"]
arr8=["sag","sa[a-z]{2,3}~([a-z]{4}us)?"]
arr9=["caprlcorn","cap*!er"]
arr10=["a[a-z]{4,6}us"]
arr11=["p[a-z]{4}is","p[a-z]{3}(e|s)s"]


outFile = open("out.txt", 'w')
for s in onlyfiles:
	s="data\\" + s	
	image = Image.open(s)  
	image = image.convert('L')
	imageText = image_to_string(image).lower()

	for loopvar in range(0,len(arr0)):
		textFound=re.findall(arr0[loopvar], imageText)
		if len(textFound) > 0 :
				wnum[0]=wnum[0]+1
				print "Written to : "+matched[0]
				print "Total Here : "+str(wnum[0])
				print "\n"
				shutil.move(s, out[0])

	for loopvar in range(0,len(arr1)):
		textFound=re.findall(arr1[loopvar], imageText)
		if len(textFound) > 0 :
				wnum[1]=wnum[1]+1
				print "Written to : "+matched[1]
				print "Total Here : "+str(wnum[1])
				print "\n"
				shutil.move(s, out[1])

	for loopvar in range(0,len(arr2)):
		textFound=re.findall(arr2[loopvar], imageText)
		if len(textFound) > 0 :
				wnum[2]=wnum[2]+1
				print "Written to : "+matched[2]
				print "Total Here : "+str(wnum[2])
				print "\n"
				shutil.move(s, out[2])

	for loopvar in range(0,len(arr3)):
		textFound=re.findall(arr3[loopvar], imageText)
		if len(textFound) > 0 :
				wnum[3]=wnum[3]+1
				print "Written to : "+matched[3]
				print "Total Here : "+str(wnum[3])
				print "\n"
				shutil.move(s, out[3])

	for loopvar in range(0,len(arr4)):
		textFound=re.findall(arr4[loopvar], imageText)
		if len(textFound) > 0 :
				wnum[4]=wnum[4]+1
				print "Written to : "+matched[4]
				print "Total Here : "+str(wnum[4])
				print "\n"
				shutil.move(s, out[4])

	for loopvar in range(0,len(arr5)):
		textFound=re.findall(arr5[loopvar], imageText)
		if len(textFound) > 0 :
				wnum[5]=wnum[5]+1
				print "Written to : "+matched[5]
				print "Total Here : "+str(wnum[5])
				print "\n"
				shutil.move(s, out[5])

	for loopvar in range(0,len(arr6)):
		textFound=re.findall(arr6[loopvar], imageText)
		if len(textFound) > 0 :
				wnum[6]=wnum[6]+1
				print "Written to : "+matched[6]
				print "Total Here : "+str(wnum[6])
				print "\n"
				shutil.move(s, out[6])

	for loopvar in range(0,len(arr7)):
		textFound=re.findall(arr7[loopvar], imageText)
		if len(textFound) > 0 :
				wnum[7]=wnum[7]+1
				print "Written to : "+matched[7]
				print "Total Here : "+str(wnum[7])
				print "\n"
				shutil.move(s, out[7])

	for loopvar in range(0,len(arr8)):
		textFound=re.findall(arr8[loopvar], imageText)
		if len(textFound) > 0 :
				wnum[8]=wnum[8]+1
				print "Written to : "+matched[8]
				print "Total Here : "+str(wnum[8])
				print "\n"
				shutil.move(s, out[8])

	for loopvar in range(0,len(arr9)):
		textFound=re.findall(arr9[loopvar], imageText)
		if len(textFound) > 0 :
				wnum[9]=wnum[9]+1
				print "Written to : "+matched[9]
				print "Total Here : "+str(wnum[9])
				print "\n"
				shutil.move(s, out[9])

	for loopvar in range(0,len(arr10)):
		textFound=re.findall(arr10[loopvar], imageText)
		if len(textFound) > 0 :
				wnum[10]=wnum[10]+1
				print "Written to : "+matched[10]
				print "Total Here : "+str(wnum[10])
				print "\n"
				shutil.move(s, out[10])

	for loopvar in range(0,len(arr11)):
		textFound=re.findall(arr11[loopvar], imageText)
		if len(textFound) > 0 :
				wnum[11]=wnum[11]+1
				print "Written to : "+matched[11]
				print "Total Here : "+str(wnum[11])
				print "\n"
				shutil.move(s, out[11])