import os
from selenium import webdriver
import sys
print(os.path.dirname(sys.executable))

dlocation = '../drvrs/chromedriver'
os.environ["webdriver.chrome.driver"] = dlocation
driver = webdriver.Chrome(dlocation)
driver.get('http://inventwithpython.com')
print(os.getcwd())
