from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'/Users/seamlesshr/Documents/Cds/Proj/drvrs/geckodriver')
driver.get('https://letskodeit.teachable.com/p/practice')

#Maximizing window
driver.maximize_window()

#Getting the website url
title = driver.title
print("title is: ",title)

currentUrl = driver.current_url
print("url is: ",currentUrl)

driver.refresh()

driver.get("https://dhtmlx.com/docs/products/dhtmlxGrid/")

print(driver.page_source)

driver.back()

driver.forward()

driver.quit()
