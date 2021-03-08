from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'../drvrs/geckodriver')
driver.get('https://letskodeit.teachable.com/p/practice')

#Making the driver wait
driver.implicitly_wait(10)

#Clciking a button
driver.find_element_by_xpath('//*[@id="bmwcheck"]').click()

#Inputing values into textbox
driver.find_element_by_xpath('//*[@id="name"]').send_keys("MUBY AGBA")

#Clearing the values entered in the textbox above
driver.find_element_by_xpath('//*[@id="name"]').clear()
