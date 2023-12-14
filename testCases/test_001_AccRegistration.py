import pytest
import time

from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrtionPage
from utilities import randomString
from utilities.readProperties import ReadConfig
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
from utilities.customLogger import LogGen

class Test_001_AccountReg:

    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()      # for logging

    @pytest.mark.regression
    def test_account_reg(self,setup):
        self.logger.debug("***********test_001_accnt_registration is started**********")
        print()
        self.driver=setup
        self.driver.get(self.baseURL)
        self.logger.info("launching application")
        print()
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)   #obj
        self.logger.info("clicking on myaccount....register")
        print()
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.logger.info("provinding customer deatils for registration.....")
        print()
        self.regpage=AccountRegistrtionPage(self.driver)    #obj
        self.regpage.setFirstName("sandy")
        self.regpage.setLastName("mary")
        self.email=randomString.random_string_generator()+"@gmail.com"
        self.regpage.setEmail(self.email)
        self.regpage.setTelephone("12345678")
        self.regpage.setPassword("jy7689hgrooo")
        self.regpage.setConfirmPassword("jy7689hgrooo")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg=self.regpage.check_message()
        msg="Your Account Has Been Created!"

        if self.confmsg=="Your Account Has Been Created!":
            self.logger.info("account registration is passed.....")
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot("E:\\pythonProject2\\screenshots\\" + "test_acc.png")
            self.driver.close()
            assert False
            self.logger.info("account registration is failed.....")

        self.logger.debug("******** test_001 is finished***************")






