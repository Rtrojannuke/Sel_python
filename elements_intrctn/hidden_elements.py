from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox(executable_path=r'../drvrs/geckodriver')
driver.get('https://letskodeit.teachable.com/p/practice')
driver.implicitly_wait(10)

#Finding the textbox before clicking the hide button
tbx = driver.find_element_by_id("displayed-text")

#Finding the state of the textbox before clicking hide button
tSt = tbx.is_displayed()
print("TEXTBOX IS DISPLAYED IS: ", tSt)#Gives true or False answer

#Clicking the hide button
driver.find_element_by_id("hide-textbox").click()
#ff
tSts = tbx.is_displayed()
print("TEXTBOX IS DISPLAYED: ", tSts)
