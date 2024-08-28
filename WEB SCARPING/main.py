import requests
from bs4 import BeautifulSoup


url = 'https://www.example.com'



response = requests.get(url, headers=headers)
response.raise_for_status() 

soup = BeautifulSoup(response.text, 'html.parser')


products = soup.find_all('div', class_='p-card-chldrn-cntnr') 
for product in products:
    title = product.find('div', class_='p-card-wrppr')
    price = product.find('div', class_='prc-box-dscntd')

    if title and price:
      
        product_name = title.get_text(strip=True)
        product_price = price.get_text(strip=True)
        print(f'Title: {product_name}')
        print(f'Price: {product_price}')
        print('-' * 40)
