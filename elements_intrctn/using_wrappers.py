from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By
import wrappers

driver = webdriver.Firefox(executable_path=r'../drvrs/geckodriver')

jkl = wrappers.UsingWrappers(driver)

driver.get('https://letskodeit.teachable.com/p/practice')
driver.implicitly_wait(10)

fld = jkl.getElement("opentab")
#sh = fld.text
#print("TEXT IS: ", sh)



fg = jkl.getElement("//*[@id='name']",locatorType="xpath")
fg.send_keys("DONE")
