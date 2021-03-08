from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path=r'../drvrs/geckodriver')
driver.get('https://www.airbnb.com/')
driver.implicitly_wait(10)

loctnbx = driver.find_element_by_id("bigsearch-query-detached-query")
loctnbx.send_keys("India")


chckin = driver.find_element_by_css_selector("div._j8gg2a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)")
chckin.click()
driver.implicitly_wait(10)


dateslct = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[2]/div/div/section/div/div/div/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[7]/div/div")
dateslct.click()

driver.implicitly_wait(10)
chckout = driver.find_element_by_css_selector("div._j8gg2a:nth-child(3) > div:nth-child(1) > div:nth-child(1)")
chckout.click()
driver.implicitly_wait(10)

chkdate = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[4]/div/div/section/div/div/div/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div/table/tbody/tr[1]/td[7]/div/div/div")
chkdate.click()

gstadd = driver.find_element(By.CSS_SELECTOR, "._37ivfdq > div:nth-child(1)")
gstadd.click()

addchd = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[5]/div[2]/div/section/div/div/div[1]/div[2]/button[2]/span")
addchd.click()
