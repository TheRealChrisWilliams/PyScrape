import threading
import requests
import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup


def scrape_data(url):
    lower_bound = int(lower_bound_entry.get())
    upper_bound = int(upper_bound_entry.get())
    option = option_var.get()
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    stocks = soup.find_all('tr')
    for stock in stocks:
        cells = stock.find_all('td')
        if len(cells) == 7:
            name = cells[0].text.strip()
            buy_or_sell = cells[1].text.strip()
            entry_price = cells[2].text.strip()
            first_target = cells[3].text.strip()
            try:
                entry_price = float(entry_price)
                if (float(lower_bound) < entry_price < float(upper_bound)) and (option == buy_or_sell):
                    print(f'{name} - Entry Price: {entry_price} - First Target: {first_target}\n')
            except ValueError:
                print(f"\n")


def start_scraping():
    url = website_entry.get()
    scraping_thread = threading.Thread(target=scrape_data, args=(url,))
    scraping_thread.start()


root = tk.Tk()
root.title("PyScrape")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
icon = tk.PhotoImage(file="4222002.png")

# Create the widgets
website_label = ttk.Label(root, text="Website:")
website_entry = ttk.Entry(root)
website_label.grid(row=0, column=0, sticky=tk.W + tk.E, padx=10, pady=10)
lower_bound_label = ttk.Label(root, text="Lower bound:")
lower_bound_entry = ttk.Entry(root)
lower_bound_label.grid(row=0, column=0, sticky=tk.W + tk.E, padx=10, pady=10)
upper_bound_label = ttk.Label(root, text="Upper bound:")
upper_bound_entry = ttk.Entry(root)
upper_bound_label.grid(row=0, column=0, sticky=tk.W + tk.E, padx=10, pady=10)
upper_bound_entry.grid(row=0, column=1, sticky=tk.W + tk.E, padx=10, pady=10)
option_var = tk.StringVar(value="SELL")
sell_option = ttk.Radiobutton(root, text="SELL", variable=option_var, value="SELL")
buy_option = ttk.Radiobutton(root, text="BUY", variable=option_var, value="BUY")
scrape_button = ttk.Button(root, text="Scrape", command=start_scraping)

# Add the widgets to the window
website_label.grid(row=0, column=0, sticky='W')
website_entry.grid(row=0, column=1)
lower_bound_label.grid(row=1, column=0, sticky='W')
lower_bound_entry.grid(row=1, column=1)
upper_bound_label.grid(row=2, column=0, sticky='W')
upper_bound_entry.grid(row=2, column=1)
sell_option.grid(row=3, column=0, sticky='W')
buy_option.grid(row=3, column=1, sticky='W')
scrape_button.grid(row=4, column=1, pady=10)
root.iconphoto(False, icon)

# Start the main
root.mainloop()
