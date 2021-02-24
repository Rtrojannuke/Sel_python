from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'/Users/seamlesshr/Documents/Cds/Proj/drvrs/geckodriver')
driver.get('https://letskodeit.teachable.com/p/practice')

use_id = driver.find_element_by_id("name")

if use_id is not None:
    print("ID PRESENT")

use_name = driver.find_element_by_name("enter-name")

if use_name is not None:
    print("NAME PRESENT")


use_xpath = driver.find_element_by_xpath('//*[@id="openwindow"]')
if use_xpath is not None:
    print("XPATH PRESENT")

use_cssSelector = driver.find_element_by_css_selector('#opentab')
if use_cssSelector is not None:
    print("CSS PRESENT")

lnktext = 'Login'
use_LinkText = driver.find_element_by_link_text(lnktext)
if use_LinkText is not None:
    print("LINKTEXT PRESENT")

part_lnktxt = 'Pract'

use_partial_linktext = driver.find_element_by_partial_link_text(part_lnktxt)
if use_partial_linktext is not None:
    print("PARTIAL LINKTEXT CONFIRMED")

use_class = driver.find_element_by_class_name("inputs")
if use_class is not None:
    print("CLASSNAME PRESENT")

use_tagName = driver.find_element_by_tag_name("input")
if use_tagName is not None:
    print("TAGNAME PRESENT")
