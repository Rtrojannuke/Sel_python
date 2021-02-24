import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path=r'/Users/seamlesshr/Documents/Cds/Proj/geckodriver')
driver.get('https://letskodeit.teachable.com/p/practice')
"""
Selenium provides a class which is the By class which is utilized in the .find_element() method 
"""
use_by_id = driver.find_element(By.ID, "name")
if use_by_id is not None:
    print("ID PRESENT")

use_by_name = driver.find_element(By.NAME, "enter-name")
if use_by_name is not None:
    print("NAME PRESENT")

use_by_xpath = driver.find_element(By.XPATH, '//*[@id="openwindow"]')
if use_by_xpath is not None:
    print("XPATH PRESENT")
