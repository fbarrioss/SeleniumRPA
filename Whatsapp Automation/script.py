from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome("C:/Users/Frank/Documents/GitHub/SeleniumRPA/Selenium Tutorial/chromedriver.exe")
browser.get("https://google.com.pe")
wait = WebDriverWait(browser,600)

buscador=browser.find_element_by_name('q');
buscador.send_keys('kefir')
wait = WebDriverWait(browser,600)
busquedas=browser.find_elements_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/ul')
for items in busquedas:
    print (items.text)
btn=browser.find_element_by_name('btnK')
btn.click()
wait = WebDriverWait(browser,600)
busquedas=browser.find_elements_by_xpath('/html/body/div[7]/div/div[10]/div[1]/div/div[4]/div/div[1]/div/div/div/div/div/div[1]/div[1]')    
wait = WebDriverWait(browser,600)
for items in busquedas:
    print (items.text)