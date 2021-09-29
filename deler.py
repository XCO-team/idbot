from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from colorama import Fore
link = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"XCO"+Fore.BLUE+"~"+Fore.WHITE+Fore.LIGHTYELLOW_EX+"Enter Instagram Image URL"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")

driver = webdriver.Chrome('chromedriver')
driver.get(link)
soup = BeautifulSoup(driver.page_source, 'lxml')
img = soup.find('img', class_='FFVAD')
img_url = img['src']
r = requests.get(img_url)
with open("instagram"+str(time.time())+".png",'wb') as f: 
    f.write(r.content)
print('success')