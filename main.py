from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
response.raise_for_status
zillow_clone_website = response.text

soup = BeautifulSoup(zillow_clone_website, "html.parser")

# Get list of links from the listing.
listing = soup.find_all(name="a", class_="property-card-link")
listing_links = [link.get("href") for link in listing]

# Get list of addresses from the listing.
addresses = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
address_list = [address.text.replace(" | ", "").strip() for address in addresses]

# Get list of prices from the listing.
prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
price_list = [price.text[:6] for price in prices]

# Keep Browser opened
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Loop through each listing and apply to the respectice form field and submit.
for index, entry in enumerate(listing_links):
    # Open google forms using selenium webdriver
    driver.get(url="google_form_link")
    # Locate address form field
    add_address = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")

    # Locate price form field
    add_price = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")

    # Locate link form field
    add_link = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")

    # Locate submit button
    submit_button = driver.find_element(By.CLASS_NAME, value="NPEfkd")
    
    add_address.send_keys(address_list[index])
    add_price.send_keys(price_list[index])
    add_link.send_keys(entry)
    submit_button.click()
    
    driver.implicitly_wait(3)
