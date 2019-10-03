from pandas import DataFrame
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
driver = webdriver.Chrome(executable_path="C:/Users/shravyp/Downloads/chromedriver_win32/chromedriver.exe")
products = []  # List to store name of the product
prices = []  # List to store price of the product
ratings = []  # List to store rating of the product
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")
content = driver.page_source
soup = BeautifulSoup(content,'html.parser')
for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
    me = a.find('div', attrs={'class': '_3wU53n'})
    price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
    rating = a.find('div', attrs={'class': 'hGSR34'})
    products.append(me.text)
    print(me.text)
    prices.append(price.text)
    print(price.text)
    ratings.append(rating.text)
df: DataFrame = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})
print(df)
df.to_csv('products.csv', index=False, encoding='utf-8')
