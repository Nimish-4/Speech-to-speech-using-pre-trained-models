import requests
from bs4 import BeautifulSoup

# Function to get the response object from Yahoo.com's finance page
# Top news articles of the moment, in the response object, are  tags of class 'js-content-viewer'

def get_page(url):
    response = requests.get(url)
    if not response.ok:
        print('Status code:', response.status_code)
        raise Exception('Failed to load page {}'.format(url))
    page_content = response.text
    doc = BeautifulSoup(page_content, 'html.parser')
    return doc


my_url = "https://finance.yahoo.com/news"

doc = get_page(my_url)

a_tags = doc.find_all('div', {'class': "content svelte-w27v8j"})
articles = []

for i in range(min(25,len(a_tags))):      #restricting to 25 articles
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
    res = requests.get(link)
    article = BeautifulSoup(res.text, 'html.parser')
    outer = article.find_all('div',{'class':'caas-body'})
    title = article.find('h1',{'id':'caas-lead-header-undefined'})


    if outer!= []:
      paras = outer[0].find_all('p')

      for i in range(1,len(paras)-1):               # Excluding  tags with irrelevant info. like date, time, author etc.
        curr+=paras[i].text
      articles_text.append(curr)


      headlines.append(title.text)



print('Number of articles: ',len(articles_text))
print(headlines)


