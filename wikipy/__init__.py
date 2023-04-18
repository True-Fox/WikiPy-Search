import wikipedia as wiki
from bs4 import BeautifulSoup
import urllib
import requests

def search_list(keysearch):

    srch_list = wiki.search(keysearch)

    if (not(srch_list)):
        return "Invalid search element. Please try again."  

    return srch_list
def search_wiki(keysearch,index):
    is_disambi = False
    response = 0
    
    try:
        summary = wiki.summary(keysearch)
                
        title = keysearch.replace(" ", '_')

        title = title.replace("'", "%27")

        url = "https://en.wikipedia.org/wiki/" + title

        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page)

        image =  soup.find('td', {'class': 'infobox-image'}).find('img')
        image_url = image.get('src')
        image_url = 'https:' + image_url
        is_disambi = False
    except wiki.exceptions.DisambiguationError as e:
        summary = e.options
        image_url = ''
        is_disambi = True
    except AttributeError:
        image_url = ''
    return (summary, is_disambi, image_url, url)
