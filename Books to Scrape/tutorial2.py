from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://books.toscrape.com/"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

# print(soup)

# a_tags = soup.select("article.product_pod h3 a")
# for tag in a_tags:
#     title = tag["title"]
#     print(title)

# book_price = soup.select("article.product_pod div p.price_color")
# for price in book_price:
#     print(price.get_text(strip=True))

# in_stock = soup.select("article.product_pod div p.instock")
# for stock in in_stock:
#     print(stock.get_text(strip=True))

titles = [tag['title'] for tag in soup.select("article.product_pod h3 a")]
prices = [price.get_text(strip=True) for price in soup.select("article.product_pod div p.price_color")]
in_stock = [stock.get_text(strip=True) for stock in soup.select("article.product_pod div p.instock")]

books_df = pd.DataFrame({
    "title": titles,
    "price": prices,
    "in_stock": in_stock
})

print(books_df)

books_df.to_csv("books.csv", index=False)