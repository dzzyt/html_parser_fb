from bs4 import BeautifulSoup
''' beautiful soup xml html scraper must be imported from bs4 like this'''
path = 'C:\some_path\fb_file.html'
file = open(path,'rb')
soup = BeautifulSoup(file,'html5lib',)
#classes
#_12gz = note titles
#_2pin = things you posted (on walls, incl. notes, and self wall)
#_3-96 _2let = outside of _2pin
output_list = []
title_string=''
for d in soup.find_all('div',class_='_2pin'):
	title = d.find('div',class_='_12gz')
	#for your notes separates titles from body
	if title != None:
		title_string = title.text.strip()
		title.decompose()
	string = d.text.strip()
	if len(string) > 10 and not string[:4] == 'http':
		if len(title_string) > 2:
			string = title_string+'\n'+string	
		output_list.append(string)
	title_string =''
string = '\n\n\n'.join(output_list)
f = open('fb_txt.txt','w+',encoding='utf-8')
f.write(string)
f.close