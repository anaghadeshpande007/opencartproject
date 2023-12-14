from selenium.webdriver.common.by import By

class MyAccountPage:

    def __init__(self,driver):
        self.driver=driver

    def clickLogout(self):
        self.driver.find_element(by=By.LINK_TEXT,value="Logout").click()