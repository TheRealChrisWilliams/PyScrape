# PyScrape

This script uses the `requests` and `BeautifulSoup` libraries to scrape stock prices in India and displays all stocks below 100 INR.

## Requirements

- Python 3.x
- requests
- bs4

## Usage

1. Clone or download the repository
2. Install the required libraries by running `pip install -r requirements.txt`
3. Run the script by using the command `python stock_scraper.py`

The script will scrape the website https://www.moneycontrol.com/indian-indices/nifty-50-9.html and display the name and prices of the stocks below 100 INR.

## Note

The script is for educational purpose only, the website might change their structure and the script may not work as expected. It's always a good practice to check the website's terms of use and robots.txt before scraping.
