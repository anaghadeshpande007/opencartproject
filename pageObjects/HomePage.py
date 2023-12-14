from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium

class HomePage:
    link_myaccount_xpath="//span[normalize-space()='My Account']"
    link_register_linktext="Register"
    link_login_linktext="Login"

    def __init__(self,driver):
        self.driver=driver

    def clickMyAccount(self):
        self.driver.find_element(by=By.XPATH,value=self.link_myaccount_xpath).click()

    def clickRegister(self):
        self.driver.find_element(by=By.LINK_TEXT,value=self.link_register_linktext).click()

    def clickLogin(self):
        self.driver.find_element(by=By.LINK_TEXT,value=self.link_login_linktext).click()
