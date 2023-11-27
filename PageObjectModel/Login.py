from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By


# username = self.driver.find_element(By.ID, "mat-input-0").send_keys("myself")
class Login():

    def __int__(self, driver):
        self.driver = driver

    userName = (By.ID, "mat-input-0")

    def getUserName(self):
        return self.driver.find_elements(*Login.userName)
