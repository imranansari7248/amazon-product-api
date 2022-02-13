from urllib import  error
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re
import sys
import json

argv = sys.argv

link = argv[1]

HTML = ''
try :
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    HTML = urlopen(req).read()
except  error.HTTPError as e :
    print(json.dumps({'error' : str(e)}))       
    sys.exit()


soup = BeautifulSoup(HTML.decode('utf-8'), "html.parser")

title = soup.find('span', {'id' : 'productTitle'}).text

mrp = soup.find('div' , { 'id' : 'apex_desktop'}).find_all('span', { 'class' : 'a-offscreen'})[0].text.replace(',', '')
curent_price = soup.find('div' , { 'id' : 'apex_desktop'}).find_all('span', { 'class' : 'a-offscreen'})[1].text.replace(',', '')
you_saved = soup.find('div' , { 'id' : 'apex_desktop'}).find_all('span', { 'class' : 'a-offscreen'})[2].text.replace(',', '')


overview = {}
for tr in soup.find('div', { 'id' : 'productOverview_feature_div'}).find_all('tr'):
    key = ' '.join([ x for x in tr.find_all('td')[0].text.split(' ') if x != ''])
    value = ' '.join([ x for x in tr.find_all('td')[1].text.split(' ') if x!= ''] )
    overview[key] = value


features = {}
features_soup = soup.find('div', { 'id' : 'feature-bullets'})

key = ' '.join([x for x in features_soup.find('h1').text.split(' ') if x != ''])
features[key] = []
for li in features_soup.find_all('li'):
    features[key].append(' '.join([x for x in li.text.split(' ') if x != '']))


image_url = soup.find('img', { 'id' : 'landingImage'})['src']


customer_reviews = {}

customer_reviews['rating'] = soup.find('div', { 'id' : 'reviewsMedley'}).find('div' , { 'class' : 'a-fixed-left-grid-col a-col-left'}).find('span' , { 'class' : 'a-icon-alt'}).text
customer_reviews['reviews'] = []

for div in soup.find('div', { 'id' : 'cm-cr-dp-review-list'} ).find_all('div', { 'class' : 'a-section review aok-relative'}):
    user = div.find('span', { 'class' : 'a-profile-name'}).text
    review = div.find('span', { 'class' : 'a-size-base review-text' }).find('span').text
    customer_reviews['reviews'].append({'user' : user, 'review' : review})

data = {
    'title' : title,
    'image_url' : image_url,
    'mrp' : mrp,
    'curent_price' : curent_price,
    'you_saved' : you_saved,
    'overview' : overview,
    'features' : features,
    'customer_reviews' : customer_reviews
}

print(json.dumps(data))

sys.stdout.flush()
















