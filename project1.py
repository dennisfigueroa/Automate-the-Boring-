import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import time

#Dynamically scraping requires opening up Chrome because the JS has to load to enter the HTML to be scrapped


#Opens up my local webdriver and launches Chrome
browser = webdriver.Chrome("/Users/dennisfigueroa/Downloads/chromedriver")
browser.maximize_window()
time.sleep(3)
website_url = 'https://champion.gg/statistics/#?sortBy=general.winPercent&order=descend&roleSort=ADC'
browser.get(website_url)

#This deals with the Cookie Acceptance in the initial screen, I need to add a conditional statement with a boolean
#that can determine whether or not the cookie acceptance appears, this prevents any issues if the cookie requirement stops being present
browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/button[2]").click()
time.sleep(2)

#Code here to grab the top 5 Champions by Winrate

#Print the name of the 5

#Convert this to JS and add it to Discord Bot








