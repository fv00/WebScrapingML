import requests
from bs4 import BeautifulSoup
import pandas as pd

# Setting soup
url = "https://carros.tucarro.com.co/logan/2013/renault-logan-2013#applied_filter_id%3DMODEL%26applied_filter_name%3DModelo%26applied_filter_order%3D3%26applied_value_id%3D62198%26applied_value_name%3DLogan%26applied_value_order%3D5%26applied_value_results%3D16%26is_custom%3Dfalse"
req = requests.get(url)
soup = BeautifulSoup(req.content, features="html.parser")

# Setting desired classes
first_class = ["ui-search-item__title ui-search-item__group__element"]
second_class = ["price-tag-fraction"]

# Getting names
names = soup.find_all(class_=first_class)
names = [x.contents[0] for x in names]

# Getting prices
prices = soup.find_all(class_=second_class)
prices = [x.contents[0] for x in prices]

# Dropping slider prices
prices.pop(0)
prices.pop(0)

# Saving results on a csv
to_save = pd.DataFrame({
    "Nombre": names,
    "Precio": prices
})

to_save.to_csv("carros2013.csv")
