from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'/Users/seamlesshr/Documents/Cds/Proj/drvrs/geckodriver')
driver.get('https://letskodeit.teachable.com/p/practice')

driver.find_element_by_xpath('//*[@id="bmwcheck"]').click()

driver.find_element_by_xpath('//*[@id="name"]').send_keys("MUBY AGBA")
