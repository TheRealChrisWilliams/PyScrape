import requests
from bs4 import BeautifulSoup

url = 'https://munafasutra.com/nse/BestIntradayTips'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

stocks = soup.find_all('tr')
for stock in stocks:
    cells = stock.find_all('td')
    if len(cells) == 7:
        name = cells[0].text.strip()
        entry_price = cells[2].text.strip()
        first_target = cells[3].text.strip()
        try:
            entry_price = float(entry_price)
            if entry_price < 100.00:
                print(f'{name} - Entry Price: {entry_price} - First Target: {first_target}\n')
        except ValueError:
            print(f"{entry_price} is not a valid number.")
