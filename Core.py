from bs4 import BeautifulSoup
import requests
import pypyodbc
import db_connection as dbConn


class Core_Class:
    def make_url(name):
        url="https://allegro.pl/kategoria/samochody-osobowe-4029?string="
        
        urls=url+name.replace(" ","%20")

        return urls
    

    def allegro_scrap(urls):
        res=requests.get(urls)
        res.raise_for_status()
        soup=BeautifulSoup(res.text,'html.parser')
        tablica = []
        min =0
        max=5
        for post in soup.find_all("div",{"class":"_9c44d_1V-js"}):
            h = post.find_all("h2",{"class":"_9c44d_LUA1k"})[0]
            title=h.text

            basic_link=post.find_all("a",{"class":"_9c44d_1MOYf"})[0]
            link=basic_link['href']
    
            basic_price=post.find_all("span",{"class":"_9c44d_1zemI"})[0]
            price=basic_price.text

            stats=post.find_all("div",{"class":"_9c44d_wFSmn _9c44d_1AacC"})[0]

            for ele in stats.find_all("dd"):
                tablica+=[ele.text]
    
            print(link)
            print(title)
            print(price)
            for i in range(min,max):
                print(tablica[i])
                min+=1
                max+=1
            
            

            return

foo = Core_Class
name = foo.make_url("opel astra")
print("\n")
foo.allegro_scrap(foo.make_url("opel astra"))