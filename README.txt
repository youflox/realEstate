														Web Scraping

Summary:

    Using python tools to scrape content from different websites for latest news and articles about Real Estate and compiling a list of the links.

Modules used:
   import requests
   from bs4 import BeautifulSoup as soup


Function: 

def real_estate_stories(url, main_class, *args, **kwargs):

Function : real_estate_stories()

The order of the arguments should be as follows:

arguments --> URL, Main_class_of_the_content, sub_classes_if_any, kwargs -> (tag = name )  


Url : url of the latest news web page 
   Eg : https://realty.economictimes.indiatimes.com/latest-news
liveMint = 'https://www.livemint.com/topic/real-estate'
   
 
real_estate_stories(liveMint, 'listView', meta=['url'])
real_estate_stories(realty, 'wdgt', tag='a')

Main_class = Main class of the stories (not id)
   Listview & wdgt  are the main class for the respective sites.
   
*args :  can be sub classes
   No argumenst were given in the above eg.

**kwargs :  keyword with argument(s)

   
   meta = [`urls¨] & tag = `a¨ are **kwargs.

To find a Meta tag property should be included. 

   
Web Scraping
   
   
   New URLS can be added to the list.

Add a new URL in the code :
liveMint ='https://www.livemint.com/topic/real-estate'
realty='https://realty.economictimes.indiatimes.com/latest-news'



Then add an instance to the function(real_estate_stories)
   
real_estate_stories(URL, Main_class, (args)sub_calasses_if_any, (kwargs))




