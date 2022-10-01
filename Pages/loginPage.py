from selenium.webdriver.common.by import By

from Locators.locators import locators
from selenium import webdriver


class loginPage():
    def __init__(self, driver):
        #self.username_textbox_id = 'user-name'
       self.driver = driver

    def enterUserName(self,userName):
        self.driver.find_element(By.ID,locators.username_textbox_id).send_keys(userName)

    def enterPassWord(self, passWord):
        self.driver.find_element(By.ID, locators.password_textbox_name).send_keys(passWord)


    def click_LoginButton(self):
        self.driver.find_element(By.ID, locators.login_button_id).click()

