from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path=r'../drvrs/geckodriver')
driver.get('https://letskodeit.teachable.com/p/practice')
driver.implicitly_wait(10)
