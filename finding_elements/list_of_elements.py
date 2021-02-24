import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path=r'/Users/seamlesshr/Documents/Cds/Proj/geckodriver')
driver.get('https://letskodeit.teachable.com/p/practice')

#Working with elements or selectors which share same attribut e.g dropdown,checkbox, readio buttons
list_elment_dropdown = driver.find_elements(By.XPATH, '//*[@id="carselect"]')
if list_elment_dropdown is not None:
    l_lst = len(list_elment_dropdown) 
    print("SIZE OF THE ELEMENT IS: ", l_lst)


use_tagNames = driver.find_elements_by_tag_name("input")
if use_tagNames is not None:
    tag_s = len(use_tagNames)
    print("TAGNAME SIZE IS: ",tag_s)


use_tagNames_td = driver.find_elements_by_tag_name("td")
if use_tagNames_td is not None:
    tag_si = len(use_tagNames_td)
    print("TAGNAME td SIZE IS: ",tag_si)
