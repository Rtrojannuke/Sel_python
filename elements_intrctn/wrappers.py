from selenium.webdriver.common.by import By

class UsingWrappers():

    def __init__(self,driver):
        self.driver = driver
    def getbytype(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH

    def getElement(self, locator, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.drver.find_element(byType,locator)
            print("ELEMENT PRESENT")
        except:
            print("ELEMENT NOT FOUND")
        return 1
        
