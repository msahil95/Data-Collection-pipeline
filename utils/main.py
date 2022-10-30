from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.myprotein.com/')