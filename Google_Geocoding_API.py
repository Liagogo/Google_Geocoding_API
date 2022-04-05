#!/usr/bin/env python
# coding: utf-8

# In[57]:


# Google Geocoding
import json
import requests
import urllib

key = 'ENTER_YOUR_KEY_HERE'#Replace with your own key, otherwise the code won't run

# define a function of crawing json from google api
def geturl(url):
    r = requests.get(url, timeout = 10)
    r.encoding = r.apparent_encoding
    return r.text

# define a function of parsing json from google api
def getinfo(js):
    try: 
        js = json.loads(text)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('-----------Something Wrong-------------')
        print(text)
    else:
        print('Adsress:', js['results'][0]['formatted_address'])
        print('Latitude:', js['results'][0]['geometry']['location']['lat'])
        print('Longitude:', js['results'][0]['geometry']['location']['lng'])


# In[62]:


# Enter any location （English or Chinese）
# Print the corresponding json file
address = input('Give me an address: ')
url = 'https://maps.googleapis.com/maps/api/geocode/json?{}&key={}'.format(urllib.parse.urlencode({'address':address}), key)
print('Retrieving', url)
text = geturl(url)
try: 
    js = json.loads(text)
except:
    js = None
print(json.dumps(js,indent = 4))


# In[52]:


# Get the latitude and longitude with defined functions
address = '1954 Huashan road, Xuhui District, Shanghai'
url = 'https://maps.googleapis.com/maps/api/geocode/json?{}&key={}'.format(urllib.parse.urlencode({'address':address}), key)
text = geturl(url)
try: 
    js = json.loads(text)
except:
    js = None
getinfo(js)


# In[53]:


# The same for Chinese addresses
address = '上海市徐汇区华山路1954号'
url = 'https://maps.googleapis.com/maps/api/geocode/json?{}&key={}'.format(urllib.parse.urlencode({'address':address}), key)
text = geturl(url)
try: 
    js = json.loads(text)
except:
    js = None
getinfo(js)

