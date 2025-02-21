import requests
from bs4 import BeautifulSoup
import random
import time

# Function to get the response object from Yahoo.com's finance page
# Top news articles of the moment, in the response object, are  tags of class 'js-content-viewer'

def get_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if not response.ok:
        print('Status code:', response.status_code)
        raise Exception(f'Failed to load page {url}')
    page_content = response.text
    doc = BeautifulSoup(page_content, 'html.parser')
    return doc


my_url = "https://finance.yahoo.com/news/"

doc = get_page(my_url)

a_tags = doc.find_all('div', {'class': "content yf-82qtw3"})
articles = []

for i in range(min(15,len(a_tags))):      #restricting to 25 articles
  articles.append(a_tags[i].find('a'))

  
# Searching for and saving the links to articles embedded in the  tags

links = []
url = ""                 #https://finance.yahoo.com/news

for anchor in articles:

  href=anchor.get('href')
  links.append(url+href)

print(links)


# Extracting the text from the actual news article using the links stored before

articles_text = []
headlines = []


for link in links:

  if link.find('video')==-1:                      # Excluding news links with videos instead of articles

    curr = ""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    res = requests.get(link, headers=headers)

    sleep_time = random.uniform(1, 4)  # Wait between 2 to 5 seconds
    time.sleep(sleep_time)


    article = BeautifulSoup(res.text, 'html.parser')

    #print(article)
    outer = article.find_all('div',{'class':'body yf-tsvcyu'})
    title = article.find('div',{'class':'cover-title yf-1rjrr1'})


    if outer!= []:
      paras = outer[0].find_all('p')

      for i in range(1,len(paras)-1):               # Excluding  tags with irrelevant info. like date, time, author etc.
        curr+=paras[i].text
      articles_text.append(curr)


      headlines.append(title.text)



print('Number of articles: ',len(articles_text))
print(headlines)


