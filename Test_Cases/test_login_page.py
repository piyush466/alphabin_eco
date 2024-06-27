from selenium import webdriver
from selenium.webdriver.common.by import By

from Page_Object.login_page import Login


class Test_Login:

    def test_login_page(self,setup):
        self.driver = setup
        self.login = Login(self.driver)
        self.login.user_email("piyush.alphabin@gmail.com")
        self.login.user_password("Piyush@123")


