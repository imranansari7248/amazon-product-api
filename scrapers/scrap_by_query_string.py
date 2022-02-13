from urllib import  parse , error
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re
import sys
import json


argv = sys.argv

query = " ".join(argv[argv.index('-query') + 1 : argv.index('-price')])
price = " ".join(argv[argv.index('-price')+1 : argv.index('-brand')])
brand = " ".join(argv[argv.index('-brand')+1 : argv.index('-page')])
page =  int(argv[argv.index('-page')+1])

if price != '0' : 
    if '-' in price:
        i = price.index('-')
        price_min = int(price[:i])
        price_max = int(price[i+1:])
        if price_min > price_max :
            price = [price_max, price_min]
        else :
            price = [price_min, price_max]
    else :
        p = int(price)
        price = [p - 10000 if p > 10000 else 0, p + 10000]
else :
    price = 0


def price_validator(item) : # price validator 
    if price:
        if not (int(item['price']) >= price[0] and int(item['price']) <= price[1]) :
            return False
    return True

def brand_validator(item) : # brand validator
    if brand != 'all':
        if re.search(brand + '(?i)', item['product']):
            return True
        else:
            return False
    else:
        return True

def fetch_product(soup) :
    items = soup.find_all('div', attrs={'class': "s-result-item"})
    products = []
    for item in items:
        tempDict = {}
        try : 
            fromItemLeft = item.find('div', { 'class' : 'sg-col sg-col-4-of-12 sg-col-4-of-16 sg-col-4-of-20 s-list-col-left' })
            fromItemRight =  item.find('div', { 'class' : 'sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 s-list-col-right' })
            tempDict['imageURL'] = fromItemLeft.find('img')['src']
            tempDict['title'] = fromItemRight.find('h2').text
            tempDict['url'] = "https://www.amazon.in" + fromItemRight.find('h2').find('a')['href']
            tempDict['price'] = int(fromItemRight.find('span', {'class' : 'a-price-whole'}).text.replace(',', ''))
            tempDict['rating'] = fromItemRight.find('span', { 'class' : 'a-icon-alt'}).text
            if price_validator(tempDict) and brand_validator(tempDict):
                products.append(tempDict)
        except  :
            # print(tempDict)
            # print('in except')
            pass
    return products

HTML = ''
try :
    req = Request(f"https://www.amazon.in/s?k={parse.quote( query )}&ref=nb_sb_noss_2&page={ page }", headers={'User-Agent': 'Mozilla/5.0'})
    HTML = urlopen(req).read()
except  error.HTTPError as e :
    print(json.dumps({'error' : str(e)}))       
    sys.exit()

soup = BeautifulSoup(HTML.decode('utf-8'), "html.parser")

products = { 'status' : 'success', 'results' : fetch_product(soup) }



# print(products)
print(json.dumps(products))

sys.stdout.flush()

