import requests
from bs4 import BeautifulSoup
import pandas as pd
import regex as re

# Setting soup
url = "https://listado.tucarro.com.co/renault-logan-2018_DisplayType_LF"
req = requests.get(url)
soup = BeautifulSoup(req.content, features="html.parser")

# Specifying desired tags
first_class = ["ui-search-item__title"]
second_class = ["price-tag-text-sr-only"]

# Getting car names
names = soup.find_all(class_=first_class)
names = [x.contents[0] for x in names]

# Getting car prices
prices = soup.find_all(class_=second_class)
prices = [x.contents[0] for x in prices]

# Getting only numbers
prices = [re.findall(pattern='[\d]+', string=x)[0] for x in prices]

# Dropping slide prices
prices.pop(0)
prices.pop(0)

# Saving results on a csv
to_save = pd.DataFrame({
    "Nombre": names,
    "Precio": prices
})

to_save.to_csv("carros2018.csv")
