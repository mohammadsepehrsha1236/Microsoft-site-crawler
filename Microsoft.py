from bs4 import BeautifulSoup
import requests
import re
from time import sleep

mic = requests.get("https://www.microsoft.com/en-us/licensing/default?rtc=1")
soup = BeautifulSoup(mic.content,"html.parser")
soup1 = BeautifulSoup(mic.content,"html.parser")
result = soup.find_all("h4",attrs={"class":"c-heading"})
result_1 = soup1.findAll("a",attrs={"class":"c-call-to-action c-glyph"})
lst = []
for i in result:
    licensing = i.text
    lst.append(licensing.strip())
lst1 = []
for l in result_1:
    licensing1 = l.text
    lst1.append(licensing1.strip())

print(lst)
sleep(30)