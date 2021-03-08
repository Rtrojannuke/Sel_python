from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'../drvrs/geckodriver')
driver.get('https://letskodeit.teachable.com/p/practice')

#Making the driver wait
driver.implicitly_wait(10)

#finding Element
tbox = driver.find_element_by_xpath('//*[@id="name"]')
#Returning true or false when checking state of the element 
j = tbox.is_enabled()
print("IS ENABLED IS: ", j)

