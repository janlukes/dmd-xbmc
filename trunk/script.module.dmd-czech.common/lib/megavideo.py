# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Conector para Megavideo
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------
# A partir del c�digo de Voinage y Coolblaze
#------------------------------------------------------------
# Modify: 2011-08-12, by Ivo Brhel
#------------------------------------------------------------

import re, sys, os
import urlparse, urllib, urllib2
#import os.path
#import sys


_UserAgent_ =  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)'
#Python Video Decryption and resolving routines.
#Courtesy of Voinage, Coolblaze.


#Megavideo - Coolblaze # Part 1 put this below VIDEOLINKS function. Ctrl & C after highlighting.

def ajoin(arr):
	strtest = ''
	for num in range(len(arr)):
		strtest = strtest + str(arr[num])
	return strtest

def asplit(mystring):
	arr = []
	for num in range(len(mystring)):
		arr.append(mystring[num])
	return arr
		
def decrypt(str1, key1, key2):

	__reg1 = []
	__reg3 = 0
	while (__reg3 < len(str1)):
		__reg0 = str1[__reg3]
		holder = __reg0
		if (holder == "0"):
			__reg1.append("0000")
		else:
			if (__reg0 == "1"):
				__reg1.append("0001")
			else:
				if (__reg0 == "2"): 
					__reg1.append("0010")
				else: 
					if (__reg0 == "3"):
						__reg1.append("0011")
					else: 
						if (__reg0 == "4"):
							__reg1.append("0100")
						else: 
							if (__reg0 == "5"):
								__reg1.append("0101")
							else: 
								if (__reg0 == "6"):
									__reg1.append("0110")
								else: 
									if (__reg0 == "7"):
										__reg1.append("0111")
									else: 
										if (__reg0 == "8"):
											__reg1.append("1000")
										else: 
											if (__reg0 == "9"):
												__reg1.append("1001")
											else: 
												if (__reg0 == "a"):
													__reg1.append("1010")
												else: 
													if (__reg0 == "b"):
														__reg1.append("1011")
													else: 
														if (__reg0 == "c"):
															__reg1.append("1100")
														else: 
															if (__reg0 == "d"):
																__reg1.append("1101")
															else: 
																if (__reg0 == "e"):
																	__reg1.append("1110")
																else: 
																	if (__reg0 == "f"):
																		__reg1.append("1111")

		__reg3 = __reg3 + 1

	mtstr = ajoin(__reg1)
	__reg1 = asplit(mtstr)
	__reg6 = []
	__reg3 = 0
	while (__reg3 < 384):
	
		key1 = (int(key1) * 11 + 77213) % 81371
		key2 = (int(key2) * 17 + 92717) % 192811
		__reg6.append((int(key1) + int(key2)) % 128)
		__reg3 = __reg3 + 1
	
	__reg3 = 256
	while (__reg3 >= 0):

		__reg5 = __reg6[__reg3]
		__reg4 = __reg3 % 128
		__reg8 = __reg1[__reg5]
		__reg1[__reg5] = __reg1[__reg4]
		__reg1[__reg4] = __reg8
		__reg3 = __reg3 - 1
	
	__reg3 = 0
	while (__reg3 < 128):
	
		__reg1[__reg3] = int(__reg1[__reg3]) ^ int(__reg6[__reg3 + 256]) & 1
		__reg3 = __reg3 + 1

	__reg12 = ajoin(__reg1)
	__reg7 = []
	__reg3 = 0
	while (__reg3 < len(__reg12)):

		__reg9 = __reg12[__reg3:__reg3 + 4]
		__reg7.append(__reg9)
		__reg3 = __reg3 + 4
		
	
	__reg2 = []
	__reg3 = 0
	while (__reg3 < len(__reg7)):
		__reg0 = __reg7[__reg3]
		holder2 = __reg0
	
		if (holder2 == "0000"):
			__reg2.append("0")
		else: 
			if (__reg0 == "0001"):
				__reg2.append("1")
			else: 
				if (__reg0 == "0010"):
					__reg2.append("2")
				else: 
					if (__reg0 == "0011"):
						__reg2.append("3")
					else: 
						if (__reg0 == "0100"):
							__reg2.append("4")
						else: 
							if (__reg0 == "0101"): 
								__reg2.append("5")
							else: 
								if (__reg0 == "0110"): 
									__reg2.append("6")
								else: 
									if (__reg0 == "0111"): 
										__reg2.append("7")
									else: 
										if (__reg0 == "1000"): 
											__reg2.append("8")
										else: 
											if (__reg0 == "1001"): 
												__reg2.append("9")
											else: 
												if (__reg0 == "1010"): 
													__reg2.append("a")
												else: 
													if (__reg0 == "1011"): 
														__reg2.append("b")
													else: 
														if (__reg0 == "1100"): 
															__reg2.append("c")
														else: 
															if (__reg0 == "1101"): 
																__reg2.append("d")
															else: 
																if (__reg0 == "1110"): 
																	__reg2.append("e")
																else: 
																	if (__reg0 == "1111"): 
																		__reg2.append("f")
																	
		__reg3 = __reg3 + 1

	endstr = ajoin(__reg2)
	return endstr

########END OF PART 1

#Part 2
# Paste this into your Default.py
# To activate it just call Megavideo(url) - where url is your megavideo url.
def getcode(mega):
	if mega.startswith('http://www.megavideo.com/?v='):
		mega = mega[-8:]
	if mega.startswith('http://wwwstatic.megavideo.com'):
		mega = re.compile('.*v=(.+?)$').findall(mega)
		mega = mega[0]
	if mega.startswith('http://www.megavideo.com/v/'):
		mega = re.compile('.*/v/(.+?)$').findall(mega)
		mega = mega[0][0:8]
	return mega

def getURL(mega):
	#mega = getcode(mega)
	movielink = getlowurl(mega)
	return movielink
#####END of part 2

def getlowurl(code):
	#code=getcode(code)
	try:
	    quality = config.get_setting("quality_flv")
	except:
	    quality = "1"

	modoPremium = "false"
	req = urllib2.Request("http://www.megavideo.com/xml/videolink.php?v="+code)
	#req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
	req.add_header('User-Agent', _UserAgent_)
	req.add_header('Referer', 'http://www.megavideo.com/')
	page = urllib2.urlopen(req);response=page.read();page.close()
		
	#errort = re.compile(' errortext="(.+?)"').findall(response)
	#movielink = ""
	#if len(errort) <= 0:
	#	s = re.compile(' s="(.+?)"').findall(response)
	#	k1 = re.compile(' k1="(.+?)"').findall(response)
	#	k2 = re.compile(' k2="(.+?)"').findall(response)
	#	un = re.compile(' un="(.+?)"').findall(response)
	#	movielink = "http://www" + s[0] + ".megavideo.com/files/" + decrypt(un[0], k1[0], k2[0]) + "/?.flv"
	
	#return movielink

        errort = re.compile(' errortext="(.+?)"').findall(response)
        movielink = ""
        if len(errort) <= 0:
            
            if quality == "1":
                hd = re.compile(' hd="(.+?)"').findall(response)
                if len(hd)>0 and hd[0]=="1":
                    s = re.compile(' hd_s="(.+?)"').findall(response)
                    k1 = re.compile(' hd_k1="(.+?)"').findall(response)
                    k2 = re.compile(' hd_k2="(.+?)"').findall(response)
                    un = re.compile(' hd_un="(.+?)"').findall(response)
                    movielink = "http://www" + s[0] + ".megavideo.com/files/" + decrypt(un[0], k1[0], k2[0]) + "/?.flv"
                    return movielink        
            
            s = re.compile(' s="(.+?)"').findall(response)
            k1 = re.compile(' k1="(.+?)"').findall(response)
            k2 = re.compile(' k2="(.+?)"').findall(response)
            un = re.compile(' un="(.+?)"').findall(response)
            movielink = "http://www" + s[0] + ".megavideo.com/files/" + decrypt(un[0], k1[0], k2[0]) + "/?.flv"

	return movielink
