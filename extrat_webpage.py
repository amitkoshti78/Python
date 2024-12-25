import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

def get_price_amazon(item_url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(item_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    price_element = soup.find(id="priceblock_ourprice")
    if not price_element:
        price_element = soup.find(id="priceblock_dealprice")
    price = price_element.get_text() if price_element else "Price not found"
    return price

def get_price_ebay(item_url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(item_url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    #soup = BeautifulSoup(response.content, 'html.parser')
    #price = soup.find(class_="notranslate").get_text()
    price_element = soup.find(id="productTitle")
    price = price_element.get_text() if price_element else "Price not found"
    

    return price

def display_prices(item_name, amazon_url, ebay_url):
    amazon_price = get_price_amazon(amazon_url)
    ebay_price = get_price_ebay(ebay_url)
    
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("Item Prices", f"Item: {item_name}\n\nAmazon: {amazon_price}\nEbay: {ebay_price}")
    root.destroy()

def fetch_prices():
        amazon_url = amazon_entry.get()
        ebay_url = ebay_entry.get()
        item_name = item_entry.get()
       

        display_prices(item_name, amazon_url, ebay_url)

if __name__ == "__main__":
    item_name = "Samsung Galaxy S24 Ultra"
    amazon_url = "https://www.amazon.de/dp/B08N5WRWNW"
    ebay_url = "https://www.ebay.de/itm/1234567890"

    #display_prices(item_name, amazon_url, ebay_url)
    root = tk.Tk()
    root.title("Price Checker")

    tk.Label(root, text="Item Name:").grid(row=0)
    tk.Label(root, text="Amazon URL:").grid(row=1)
    tk.Label(root, text="Ebay URL:").grid(row=2)

    item_entry = tk.Entry(root)
    amazon_entry = tk.Entry(root)
    ebay_entry = tk.Entry(root)

    item_entry.grid(row=0, column=1)
    amazon_entry.grid(row=1, column=1)
    ebay_entry.grid(row=2, column=1)

    tk.Button(root, text="Check Prices", command=fetch_prices).grid(row=3, column=1)

    root.mainloop()