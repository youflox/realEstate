import requests
from bs4 import BeautifulSoup as soup

# Web sites
liveMint = ['https://www.livemint.com/topic/real-estate']
realty = 'https://realty.economictimes.indiatimes.com/latest-news'  # id = id="recent-news-listing"
magicBricks = 'https://content.magicbricks.com/property-news/pune-real-estate-news-industry-news'  # leftContainer

urls = {
    # 'name' : [ 'url', 'main_class_to_search_on_website', ]

    'liveMint': [liveMint, 'listing']

}


def real_estate_stories(url, mainClass, ):
    request = requests.get(liveMint)
    page = soup(request.content, 'html.parser')
    allHeadlines = page.find_all(class_='listing')

    for headline in allHeadlines:
    headlineTitle = headline.find('meta', itemprop="name")
    headlineURL = headline.find('meta', itemprop="url")

    print((headlineTitle)['content'] + " : " + (headlineURL)['content'])
