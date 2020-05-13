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
        name=soup.find("h2",{"class":"_9c44d_LUA1k"}).get_text()
        price=soup.find("span",{"class":"_9c44d_1zemI"}).get_text()

        print(urls)
        print("\n\nitem " + name)
        print("price " + price + "\n") 

        elements = soup.find_all("h2", class_="_9c44d_LUA1k".split())
        #parameters = soup.find_all("div", class_="_9c44d_Pjt1U".split())
        print("\n".join("{}".format(el.get_text()) for el in elements))

        #print("\n".join("{}".format(pr.get_text()) for pr in parameters))

        
            

foo = Core_Class
name = foo.make_url("opel astra")
print("\n")
foo.allegro_scrap(foo.make_url("opel astra"))