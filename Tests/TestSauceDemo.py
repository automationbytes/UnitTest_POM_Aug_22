import unittest
import time
from pyunitreport import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from Pages.loginPage import loginPage
from Pages.homePage import homePage

class sauceLabsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get("https://www.saucedemo.com/")


    def test_1_login(self):
        login = loginPage(self.driver)
        login.enterUserName("standard_user")
        login.enterPassWord("secret_sauce")
        login.click_LoginButton()

    def test_2_filterOption(self):
        home = homePage(self.driver)
        home.selectFilterOption("Price (low to high)")

    @classmethod
    def tearDownClass(cls):
        pass
        # cls.driver.close()
        # cls.driver.quit()

if __name__ == '__main__':
    HTMLTestRunner.main()