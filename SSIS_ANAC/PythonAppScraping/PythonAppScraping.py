
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

# Instanciando o navegador
driver = webdriver.Chrome(executable_path=os.getcwd() + os.sep + 'chromedriver.exe')
