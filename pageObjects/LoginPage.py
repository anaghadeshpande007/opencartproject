from selenium.webdriver.common.by import By

class LoginPage:
    txt_email_xpath="//input[@id='input-email']"
    txt_password_xpath="//input[@id='input-password']"
    btn_login_xpath="//input[@value='Login']"
    msg_myaccount_xpath="//h2[normalize-space()='My Account']"


    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element(by=By.XPATH,value=self.txt_email_xpath).send_keys(email)

    def setPassword(self, pwd):
        self.driver.find_element(by=By.XPATH, value=self.txt_password_xpath).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(by=By.XPATH, value=self.btn_login_xpath).click()


    def isMyAccountPageExsists(self):
        try:
            return self.driver.find_element(by=By.XPATH,value=self.msg_myaccount_xpath).is_displayed()
        except:
            return False



