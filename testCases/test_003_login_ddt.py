import time

import pytest
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtilities
import os

class Test_Login_DDT:
    baseURL=ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    path=os.path.abspath(os.curdir)+"\\testdata\\opencart_LoginData.xlsx"


    def test_login_ddt(self,setup):
        self.logger.info("**********started test_003_login_datadriven******")
        self.rows=XLUtilities.getRowCount(self.path,'Sheet1')    #gives total no of rows in excel file
        lst_status=[]

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        #page object class onbjects
        self.hp=HomePage(self.driver)
        self.lp=LoginPage(self.driver)
        self.ma=MyAccountPage(self.driver)

        for r in range(2,self.rows+1):
            self.hp.clickMyAccount()
            self.hp.clickLogin()

            self.email=XLUtilities.readdata(self.path,"Sheet1",r,1)
            self.password=XLUtilities.readdata(self.path,"Sheet1",r,2)
            self.exp=XLUtilities.readdata(self.path,"Sheet1",r,3)

            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)
            self.targetpage=self.lp.isMyAccountPageExsists()

            if self.exp=='Valid':
                if self.targetpage==True:
                    lst_status.append('Pass')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Fail')
            elif self.exp=='Invalid':
                if self.targetpage==True:
                    lst_status.append('Fail')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Pass')
        self.driver.close()

        #final validation
        if 'Fail' not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("**********End of test_003_login_datadriven**************************")
