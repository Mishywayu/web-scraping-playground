from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.imdb.com/"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
print(soup)