from bs4 import BeautifulSoup
import urllib.request
import numpy as np

url="www.helistart.com/helicopter-list.aspx"

#http://www.helistart.com/helicopter-list.aspx?StartRow=10

page=list(range(1,25))

helicopter_models=[]

for p in page:
	print(p)
	current_url="http://"+url+"?StartRow="+str(p*10-10)
	print(current_url)
	html=urllib.request.urlopen(current_url).read()

	soup=BeautifulSoup(html,'html.parser')
	table=soup.find("table")

	models=table.findAll("a")
	liste=[]
	for m in models:
		liste.append(m.text)
	del liste[:4]
	helicopter_models.extend(liste)

print(helicopter_models)

np.save("models.npy",np.array(helicopter_models))