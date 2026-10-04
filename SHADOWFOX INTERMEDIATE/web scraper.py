'''
#Task 2(Intermediate Level): Do both the tasks
1. Web Scraper: Extract data from websites using libraries like Beautiful Soup or
Scrapy.

'''
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")

print("Quotes from the website:")

for quote in quotes:
    print(quote.text)
    