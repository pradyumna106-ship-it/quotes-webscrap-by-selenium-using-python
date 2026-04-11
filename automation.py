# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 17:34:34 2026

@author: prady
"""

import selenium
print(selenium.__version__)
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
driver.get("https://quotes.toscrape.com/login")
username = driver.find_element(By.ID,'username')
password = driver.find_element(By.ID,'password')
#login = driver.find_element(By.CLASS_NAME,'btn')
#login = driver.find_element(By.CSS_SELECTOR,'input.btn.btn-primary')
login = driver.find_element(By.XPATH,'/html/body/div/form/input[2]')

username.send_keys('username')
password.send_keys('password123')
login.click()

quotes = driver.find_elements(By.CLASS_NAME,'quote')
quote_list = []
author_list = []
for entry in quotes:
    quote = entry.find_element(By.CLASS_NAME, 'text').text
    author = entry.find_element(By.CLASS_NAME, 'author').text
    quote_list.append(quote)
    author_list.append(author)
df = pd.DataFrame({'Author':author_list,'Quote':quote_list})
df['Quote'] = df['Quote'].str.lstrip('“').str.rstrip('”')
print(df)
df.to_csv('quote.csv',index=False)
driver.quit()