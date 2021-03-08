from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox(executable_path=r'../drvrs/geckodriver')
driver.get('https://letskodeit.teachable.com/p/practice')
driver.implicitly_wait(10)

#Handling when elements have same attribute(e.g.id,name,class e.t.c )
rdbtnlst = driver.find_elements_by_xpath("//*[@type='radio']")
rdbtnS = len(rdbtnlst)
print("SIZE OF RADIOBTN IS: ",rdbtnS)

for rdbtn in rdbtnlst:
    selctd = rdbtn.is_selected()
    if not selctd:
        rdbtn.click()

        
#Handling dropdowns with lists in it
dpdn = driver.find_element_by_xpath('//*[@id="carselect"]')

#Using Select class on list of elements in a dropdown
selct = Select(dpdn)


#Selecting from a dropdown by value attribute
selct.select_by_value("bmw")
time.sleep(3)

#Selecting from a dropdown by index
selct.select_by_index("2") #OR
#selct.select_by_index(2)
time.sleep(3)

#Selecting by text from a dropdown
selct.select_by_visible_text("Benz")
