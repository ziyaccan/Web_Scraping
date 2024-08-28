from urllib import response
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.example.com"
response = requests.get(url)

html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")
title = soup.find_all("span", attrs={"class": "prdct-desc-cntnr-name hasRatings"})
price = soup.find_all("div", attrs={"class": "prc-box-dscntd"})

liste = list()

for i in range(len(isim)):
    title[i] = (title[i].text).strip("\n").strip()
    price[i] = (price[i].text).strip("\n").strip()

    liste.append ([price[i],title[i]])


output = pd.DataFrame(liste,columns= ["title" , " price"])
print(output)
