import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class AccountRegistrtionPage:

    txt_firstname_name="firstname"
    txt_lastname_name="lastname"
    txt_email_name = "email"
    txt_telephone_name="telephone"
    txt_password_name = "password"
    txt_passwordconfirm_name="confirm"
    chk_policy_name="agree"
    btn_continue_xpath="//input[@value='Continue']"
    text_msg_conf_xpath="//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self,driver):
        self.driver=driver


    def setFirstName(self,fname):
        self.driver.find_element(by=By.NAME,value=self.txt_firstname_name).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(by=By.NAME,value=self.txt_lastname_name).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(by=By.NAME,value=self.txt_email_name).send_keys(email)

    def setTelephone(self,telephone):
        self.driver.find_element(by=By.NAME,value=self.txt_telephone_name).send_keys(telephone)

    def setPassword(self, pwd):
        self.driver.find_element(by=By.NAME, value=self.txt_password_name).send_keys(pwd)

    def setConfirmPassword(self, cpwd):
        self.driver.find_element(by=By.NAME, value=self.txt_passwordconfirm_name).send_keys(cpwd)

    def setPrivacyPolicy(self):
        self.driver.find_element(by=By.NAME,value=self.chk_policy_name).click()
        #self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        time.sleep(3)

    def clickContinue(self):
        self.driver.find_element(by=By.XPATH,value=self.btn_continue_xpath).click()
        #self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        #self.driver.execute_script("arguments[0].click()", element)

    def check_message(self):
        try:
            return self.driver.find_element(by=By.XPATH,value=self.text_msg_conf_xpath).text

        except:
            None














