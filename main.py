from bs4 import BeautifulSoup
import requests
from selenium import webdriver

response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
response.raise_for_status
zillow_clone_website = response.text

soup = BeautifulSoup(zillow_clone_website, "html.parser")
driver = webdriver.Chrome()

listing = soup.find_all(name="a", class_="property-card-link")
listing_links = [link.get("href") for link in listing]
print(f"Listing of Links : {listing_links}")
addresses = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
address_list = [address.text.replace(" | ", "").strip() for address in addresses]
print(f"Address List: {address_list}")
prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
price_list = [price.text[:6] for price in prices]
print(f"Price list: {price_list}")
