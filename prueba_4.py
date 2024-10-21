import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup


def scrape():
    url = url_entry.get()  
    if not url:
        messagebox.showerror("Error", "Por favor, ingresa una URL válida.")
        return

    try:
        
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')
        
        
        price = soup.find_all("div", class_="ui-search-result__wrapper")
        
        if price:
           
            result_text = "Información encontrada:\n"
            for price in price:
                result_text += price.get_text() + "\n"  
            result_label.config(text=result_text)
        else:
            result_label.config(text="No se encontró infromación en la página.")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"No se pudo obtener la página: {e}")

root = tk.Tk()
root.title("Scraping")


url_label = tk.Label(root, text="Ingresa la URL:")
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)


scrape_button = tk.Button(root, text="Iniciar Scraping", command=scrape)
scrape_button.pack(pady=20)


result_label = tk.Label(root, text="")
result_label.pack(pady=10)


root.mainloop()