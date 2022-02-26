import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
categories = ["Icones","Images","Illustrations","Framework","CMS","Challenges","WebDesign","Challenges","WebDesign","Editeur","Hebergements","Outils","React","Colors","Fonts","Shape","Shape","Background"]

url = "https://creative-ressources.fr/Background"
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome("chromedriver.exe")
driver.get(url)
time.sleep(3)
page = driver.page_source
driver.quit()
soup = BeautifulSoup(page, 'html.parser')
print(soup)
container = soup.find_all('div', attrs={
    'class':'card'})
print(container)
