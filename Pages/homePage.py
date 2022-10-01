from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Locators.locators import locators
from selenium import webdriver


class homePage():
    def __init__(self, driver):
        #self.username_textbox_id = 'user-name'
       self.driver = driver

    def selectFilterOption(self,filterValue):
        dropdown = Select(self.driver.find_element(By.XPATH,locators.filter_select_xpath))
        dropdown.select_by_visible_text(filterValue)
    def click_LogoutButton(self):
        pass
