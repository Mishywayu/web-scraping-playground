from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

# Proper Chrome user-agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/117.0.0.0 Safari/537.36"
}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

# print(soup)

# print(soup.find_all("table")[0])

tables = soup.select("table.wikitable")
print(len(tables)) 

df = pd.read_html(str(tables[0]))[0]
print(df.head())

df.to_csv("companies.csv", index=False)