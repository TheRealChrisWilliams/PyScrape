import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup


def scrape():
    # Get the user input
    url = website_entry.get()
    lower_bound = int(lower_bound_entry.get())
    upper_bound = int(upper_bound_entry.get())
    option = option_var.get()

    # Make the request and parse the HTML
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the relevant information
    stocks = []
    for stock in soup.find_all('tr'):
        cells = stock.find_all('td')
        if len(cells) == 7:
            stocks.append({
                'name': cells[0].text.strip(),
                'buy_or_sell': cells[1].text.strip(),
                'entry_price': cells[2].text.strip(),
                'first_target': cells[3].text.strip()
            })

    for stock in stocks:
        try:
            entry_price = float(stock['entry_price'])
            if (float(lower_bound) < entry_price < float(upper_bound)) and (option == stock['buy_or_sell']):
                print(f'{stock["name"]} - Entry Price: {entry_price} - First Target: {stock["first_target"]}\n')
        except ValueError:
            print(f"\n")


# Create the main window
root = tk.Tk()
root.title("PyScrape")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
icon = tk.PhotoImage(file="4222002.png")

# Create the widgets
website_label = ttk.Label(root, text="Website:")
website_entry = ttk.Entry(root)
website_label.grid(row=0, column=0, sticky='W',padx=10,pady=10)
website_entry.grid(row=0, column=1,padx=10,pady=10)
lower_bound_label = ttk.Label(root, text="Lower bound:")
lower_bound_entry = ttk.Entry(root)
upper_bound_label = ttk.Label(root, text="Upper bound:")
upper_bound_entry = ttk.Entry(root)
option_var = tk.StringVar(value="SELL")
sell_option = ttk.Radiobutton(root, text="SELL", variable=option_var, value="SELL")
buy_option = ttk.Radiobutton(root, text="BUY", variable=option_var, value="BUY")
scrape_button = ttk.Button(root, text="Scrape", command=scrape)

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
