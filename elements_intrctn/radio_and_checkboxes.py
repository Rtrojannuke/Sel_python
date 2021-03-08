from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'../drvrs/geckodriver')
driver.get('https://letskodeit.teachable.com/p/practice')
driver.implicitly_wait(10)

"""
What makes a radio button different from a checkbox is the type of element in the DOM.
Type of radio button is radio
Type of checkbox is checkbox
"""
#Decalring the element of the checkbox
chckbx1 = driver.find_element_by_id("bmwcheck")
chckbx2 = driver.find_element_by_id("benzcheck")
#Clicking on the above declare element
chckbx1.click()
chckbx2.click()

#Checking clicked checkbox
bmClctd = chckbx1.is_selected()
benClctd = chckbx2.is_selected()

#Printing the selected one
print("BMW CHECK BOX IS SELECTED: ", bmClctd)
print("Benz CHECK BOX IS SELECTED: ", benClctd)

#Declaring elements of the radio buttons
rdbtn1 = driver.find_element_by_id("bmwradio")
rdbtn2 = driver.find_element_by_id("benzradio")

#Clicking the radio buttons
rdbtn1.click()
rdbtn2.click()

#Checking which radio is selected
bmSlctd = rdbtn1.is_selected()
benSlctd = rdbtn2.is_selected()

#Printing the selected radio box
print("BMW RADIO BUTTON IS SELECTED: ", bmSlctd)
print("BENZ RADIO BUTTON IS SELECTED: ", benSlctd)

