from calendar import c
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
categories = ["Icones","Images","Illustrations","Framework","CMS","Challenges","WebDesign","Challenges","WebDesign","Editeur","Hebergements","Outils","React","Colors","Fonts","Shape","Shape","Background"]
for categori in categories:
  url = "https://creative-ressources.fr/"+categori
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
      'class':'card'})
  #print(container)
  items = []
  for content in container:
    #print(content)
    img = content.find('div', attrs={
          'class':'img_box'})
    categories = content.find_all("li")
    for categorie in categories:
      print(categorie.text)


    page = {}
    
    
    page["title"] = content.p.text
    page["img"] = img.a.get('href')
    page["link"] = img.img.get('src')
    count = 0
    for categorie in categories:
      if count == 0:

        page["cate0"]  = categorie.text
      page["cate1"]  = categorie.text 
      count+=1
    
    
    
    #print(categories.li.text)
    
      #page["f"][i] = categories.li[i].text


    

    items.append(page)

  print(items)
