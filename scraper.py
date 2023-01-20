import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

stock_table = soup.find("table", {"class": "W(100%) M(0)"})
stock_rows = stock_table.find_all("tr")

for row in stock_rows:
    stock_data = row.find_all("td")
    if stock_data:
        stock_symbol = stock_data[0].text
        stock_price = float(stock_data[1].text)
        if stock_price < 25:
            print(f"{stock_symbol}: ${stock_price}")
