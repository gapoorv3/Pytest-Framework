import time
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PageObjectModel.Login import Login
from Utilities.BaseClass import BaseClass


class Tests(BaseClass):

    def testLogin(self):
        try:
            self.driver.implicitly_wait(5)
            userName = Login(self.driver)
            userName.getUserName().send_keys("myself")
            self.driver.find_element(By.ID, "mat-input-1").send_keys("Apps@5632")
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            log = self.getLogger()
            log.info('Success')
        except Exception as e:
            log = self.getLogger()
            log.error(str(e))
