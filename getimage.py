from bs4 import BeautifulSoup as bs
import requests
import sys
import re

def return_image_links(url, headers):
    page = requests.get(url, headers=headers)
    if page.status_code == 200:
        soup = bs(page.text, "html.parser")
        img_tags = soup.select('img[alt="Post image"]')

        image_urls = []
        for img_tag in img_tags:
           image_urls.append(img_tag['src'])
        return image_urls
    else:
        print('Bad response from reddit server.')
        sys.exit()
    
def getMeme(url):
    headers = {"User-Agent": 'Mozilla/5.0'}
    imgs = return_image_links(url, headers)
    img = imgs[0]
    #print(*imgs, sep='\n')
    return img
    
def getnewMeme(url):
    with open('./posted_log') as reader:
        alreadyPosted = re.split('\n',reader.read())
    headers = {"User-Agent": 'Mozilla/5.0'}
    imgs = return_image_links(url, headers)
    #print(*imgs, sep='\n')
    for i in range (0, len(imgs)):
        img = imgs[i]
        if img not in alreadyPosted:
            return img
    return ''
