from calendar import c
from os import link
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://designresourc.es/"
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome("chromedriver.exe")
driver.get(url)
time.sleep(3)
page = driver.page_source
driver.quit()
soup = BeautifulSoup(page, 'html.parser')
#print(soup)
container = soup.find_all('div', attrs={
      'class':'card-block-deal'})
  #print(container)
items = []
for content in container:
  print(content.img.get('src'))
  link = content.find('a', attrs={
      'class':'link-block w-inline-block'})
  tag = content.find('div', attrs={
      'class':'tag'})
  title =  content.find('h3', attrs={
      'class':'heading-10'}) 
  page = {}

  page["img"] =  content.img.get('src')
  page["title"] = title.text
  page["tag"] =  tag.text  
  page["link"] = link.get("href")
  items.append(page)
with open("exemple.txt", "a") as fichier:
	    fichier.write(str(items))   
print(items)

  
