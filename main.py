import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

google_form = 'https://docs.google.com/forms/d/e/1FAIpQLSdHzdjWpzD2ySNcFv78s7Sk2Y8ZhgEfKGuMbYkK5jQuhEI06g/viewform?usp=publish-editor'
zillow_url = "https://appbrewery.github.io/Zillow-Clone/"


response = requests.get(url=zillow_url).text
soup = BeautifulSoup(response, "html.parser")
links = []
prices = []
addresses = []

all_addresses = soup.find_all(name='address')
for address in all_addresses:
    addresses.append(address.text.strip())

all_prices = soup.find_all(name="span", class_='PropertyCardWrapper__StyledPriceLine')
for price in all_prices:
    prices.append(price.text.replace("$", "").replace("+", "").replace("1bd", "").replace("/mo", "").replace(" 1 bd", ""))

anchor_tags = soup.find_all(name="a", href=True, class_='StyledPropertyCardDataArea-anchor')
for tag in anchor_tags:
    links.append(tag.get("href"))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(url=google_form)

for _ in range(len(addresses)):

    sleep(2)

    address_input = driver.find_element(By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

    price_input = driver.find_element(By.XPATH,
                                      value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

    link_input = driver.find_element(By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    address_input.click()
    address_input.send_keys(addresses[_])

    price_input.click()
    price_input.send_keys(prices[_])

    link_input.click()
    link_input.send_keys(links[_])

    submit.click()

    try:
        another_response = driver.find_element(By.LINK_TEXT, "Submit another response")
        another_response.click()
        sleep(2)
    except NoSuchElementException:
        break
