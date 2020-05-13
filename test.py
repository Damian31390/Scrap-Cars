import requests
from bs4 import BeautifulSoup 

base_url="https://allegro.pl/kategoria/samochody-osobowe-4029?string="

name ="opel astra"

urls=base_url+name.replace(" ","%20")

res=requests.get(urls)
res.raise_for_status()
soup=BeautifulSoup(res.text,'html.parser')

for post in soup.find_all("div",{"class":"_9c44d_1V-js"}):
    h = post.find_all("h2",{"class":"_9c44d_LUA1k"})[0]
    title=h.text
    
    basic_link=post.find_all("a",{"class":"_9c44d_1MOYf"})[0]
    link=basic_link['href']
    
    basic_price=post.find_all("span",{"class":"_9c44d_1zemI"})[0]
    price=basic_price.text
    
    stats=post.find_all("div",{"class":"_9c44d_Pjt1U"})[0]
    
    print(stats.text)
    #print(link)
    #print(title)
    #print(price)