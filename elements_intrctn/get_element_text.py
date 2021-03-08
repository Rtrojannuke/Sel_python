from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path=r'../drvrs/geckodriver')
driver.get('https://letskodeit.teachable.com/p/practice')
driver.implicitly_wait(10)

#Finding element on the webpage whose text is to be confimedd
opntxt = driver.find_element_by_id("opentab")

#Using the text method on the element to get the text
txt = opntxt.text

#printing the element text
print("TEXT ISS:",txt)
