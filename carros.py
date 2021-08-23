import requests
from bs4 import BeautifulSoup
import pandas as pd

# Setting soup
url = "https://listado.mercadolibre.com.co/renalut-logan"
req = requests.get(url)
soup = BeautifulSoup(req.content, features="html.parser")

# Setting desired classes
first_class = ["ui-search-item__title ui-search-item__group__element"]
second_class = ["price-tag-fraction"]
third_class = ["ui-search-card-attributes__attribute"]

# Getting names
names = soup.find_all(class_=first_class)
names = [x.contents[0] for x in names]

# Getting prices
prices = soup.find_all(class_=second_class)
prices = [x.contents[0] for x in prices]

years = soup.find_all(class_=third_class)
years =  [x.contents[0] for x in years if x.contents[0].isdigit()]
print(years)
print(len(prices), len(names), len(years))

# Dropping slider prices
prices.pop(0)
prices.pop(0)

# Saving results on a csv
to_save = pd.DataFrame({
    "Nombre": names,
    "Modelo": years,
    "Precio": prices
})

to_save.to_csv("carros.csv", index = False)