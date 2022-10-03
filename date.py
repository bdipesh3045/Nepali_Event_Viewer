from bs4 import BeautifulSoup
from requests import request
import requests
from curses.ascii import BS
from pyBSDate import convert_AD_to_BS
print('''Note to write correct date!''')
# Taking date in international form converting the date
date=input("Enter the date in international system like(2022-10-3) \n")
date_list=date.split('-')
bs_date = convert_AD_to_BS(int(date_list[0]), int(date_list[1]),int(date_list[2]))
Bs_li=[]
for x in bs_date:
    Bs_li.append(x)
year_nepali=int(Bs_li[0])
month_nepali=int(Bs_li[1])
url=f"https://www.hamropatro.com/calendar/{year_nepali}/{month_nepali}"
li=[]
data=requests.get(url)
soup=BeautifulSoup(data.text,'html.parser')
soup= soup.find('li' , {"id":date})
h1=soup.find('span' , {"class":'event'})
h1=h1.get_text(strip = True)
li.append(h1)
for i in range(1,4):
    a=f"col{i}"
    if(i==1):
        div= soup.find('div' , {"class":a})
        sp1=div.find('span')
        li.append(sp1.get_text(strip = True))
    elif(a=="col2"):
        div= soup.find('div' , {"class":a})
        li.append(div.get_text(strip = True))
    else:
        div= soup.find('div' , {"class":"panchangaWrapper"})
        li.append(div.get_text(strip = True))
with open('festival.txt', 'w') as f:
    for line in li:
        f.write(line)
        f.write('\n')
