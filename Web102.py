from bs4 import BeautifulSoup               ''' Importing Modules'''
import random
import requests

def core_spider(max_pages):                           '''creation of the main core_spider that does the crawling.
                                                                            The url can be changed according to the desired webpage needed to crawl'''


    page=1
    while page<=max_pages:                                                '''Incrementing page value to visit the next page
    
    
        url="https://www.ebay.in/sch/Games-Consoles-Accessories/1249/i.html?_sop=12&_from=R40&_nkw=&LH_BIN=1&_pgn="+str(page)+"&_skc=50&rt=nc"
        
        source=requests.get(url)                             #Retrieving the given URL
        
        plain_text=source.text
        soup=BeautifulSoup(plain_text,'html.parser')                              #Creation of a BeautifulSoup Object
        for link in soup.findAll('a',{'class':'vip'}):                            
        
            href=link.get('href')                                               #href class stores the link url
            
            
            title=link.get('title')                                            #title class stores the title
            print (title)
            print (href)
            sing_item(href)                                                 #Invoking the second function that crawls the webpage of an item
        page+=1


def sing_item(item_url):
    source = requests.get(item_url)
    plain_text = source.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for new_item in soup.findAll('span',{'class':'notranslate'},{'itemprop':'price'}):            #Retrieving and printing the price of the item to the console
    
    
        print (new_item.string)
    for link in soup.findAll('a'):                                                                #'a' means anchor points which stores all the links in that page
    
    
        print (link.string)
        print (link.get('href'))



core_spider(1)                                                              #INVOKING THE MAIN SPIDER FUNCTION/THE CRAWLER
