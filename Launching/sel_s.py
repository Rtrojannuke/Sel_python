from selenium import webdriver
import os

drivlocation = "/Users/seamlesshr/Documents/Cds/Proj/selenium-safari-driver-3.14.0.jar"
os.environ["SELENIUM_SERVER_JAR"] = drivlocation

driver = webdriver.Safari()

driver.get("https://pypi.org/project/selenium/")
