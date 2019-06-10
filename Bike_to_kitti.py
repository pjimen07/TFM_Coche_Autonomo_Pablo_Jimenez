#! /usr/bin/python
print ("Leyendo...") #chmod 777 ./text.py

import os

files = [fil for fil in os.listdir('.') if os.path.isfile(fil)]
for fil in files:
	if fil.endswith(".json"):
		f=open(fil,'r')
		g = open("../label_voc/"+fil[:-5]+".txt","w")
		linea = f.readline()
		linea = f.readline()
		while linea != "":	
			if linea[7:13] == "mincol":  
				le=linea[16:]
				le = le[:-3]
				le=str(int(le)-1)

				if le[0]=="-":
					le="1"
				print('le=',le)
			if linea[7:13] == "minrow": 
				bot=linea[16:]
				bot=bot[:-3]
				bot=str(int(bot)-1)
				if bot[0]=="-":
					bot="1"
				print('bot=',bot)
			if linea[7:13] == "maxrow":  
				top=linea[16:]
				top = top[:-3]
				top=str(int(top)-1)
				if int(top)>=1023:
					top="1023"
				if top[0]=="-":
					top="1"
				print('top=',top)
			if linea[7:13] == "maxcol":  
				ri=linea[16:]
				ri = ri[:-3]
				ri=str(int(ri)-1)
				if int(ri)>=2047:
					ri="2047"
				if ri[0]=="-":
					ri="1"
				print('ri=',ri)

			if linea[7:15] == "identity":  
				cat=linea[19:]
				cat = cat[:-2]
				print('cat=',cat)
				l=cat+" "+"0.00"+" "+"0"+" "+"0.00"+" "+le+".00"+" "+bot+".00"+" "+ri+".00"+" "+top+".00"+" "+"1.00"+" "+"1.00"+" "+"1.00"+" "+"1.00"+" "+"2.00"+" "+"3.00"+" "+"1.50"+"\n"
				g.write(l)

			#print('cat=',linea[-2])
			linea = f.readline()

		g.close()
		f.close()
