from bs4 import BeautifulSoup
import requests
import json
import pprint
from flask import make_response
def make_url(name):
    url="https://allegro.pl/kategoria/samochody-osobowe-4029?string="
        
    url=url+name.replace(" ","%20")

    return url
    
def allegro_scrap(url):
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,'html.parser')
 
    offers = []
    for post in soup.find_all("div", {"class": "_9c44d_1V-js"}):
        offer = {
            "1.uri": post.find_next("a", {"class": "_9c44d_1MOYf"})["href"],
            "2.title": post.find_next("h2", {"class": "_9c44d_LUA1k"}).text,
            "3.price": post.find_next("span", {"class": "_9c44d_1zemI"}).text,
            "4.attributes": [attr.text for attr in post.find_all("dd")],

        }

        offers.append(offer)
    return offers
