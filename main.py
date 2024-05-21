#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


# In[ ]:


driver = webdriver.Chrome()
driver.get('http://localhost:3000/')
driver.implicitly_wait(5)


# In[ ]:


df = pd.read_excel('data.xlsx')

products = driver.find_element(by=By.XPATH, value='//*[@id="navbarSupportedContent"]/ul/li[2]/a')
products.click()
time.sleep(0.5)

for indice, linha in df.iterrows(): 
    create = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/button[1]')
    create.click()
    time.sleep(0.5)

    text_box = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div/form/div[1]/div/input')
    name = df.loc[indice, 'Nome']
    text_box.send_keys(name)
        
    text_box = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div/form/div[2]/div/input')
    description = df.loc[indice, 'Descrição']
    text_box.send_keys(description)
    
    text_box = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div/form/div[3]/div/input')
    category = df.loc[indice, 'Categoria']
    text_box.send_keys(category)
    
    text_box = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div/form/div[4]/div/input')
    price = df.loc[indice, 'Preço']
    price = price.replace('R$', '')
    price = price.replace(',', '.')
    text_box.send_keys(price)
   
    text_box = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div/form/div[5]/div/input')
    amount = df.loc[indice, 'Quantidade']
    text_box.send_keys(str(amount))
    
    text_box = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div/form/div[6]/div/input')
    supplier = df.loc[indice, 'Fornecedor']
    text_box.send_keys(supplier)
    
    text_box = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div/form/div[7]/div/input')
    brand = df.loc[indice, 'Marca']
    text_box.send_keys(brand)
    
    save = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div/form/div[8]/div[1]/button')
    save.click()
    time.sleep(0.5)
    
driver.quit()

