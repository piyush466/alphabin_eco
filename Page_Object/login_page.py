from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    email_name = "email"
    password_name = "password"
    log_in_btn_xpath = "//button[text()='LOG IN']"

    def __init__(self, driver):
        self.driver = driver

    def user_email(self, user_email):
        self.driver.find_element(By.XPATH, self.email_name).send_keys(user_email)

    def user_password(self, user_password):
        self.driver.find_element(By.XPATH, self.password_name).send_keys(user_password)
        self.driver.find_element(By.XPATH, self.log_in_btn_xpath).click()



