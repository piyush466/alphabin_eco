from selenium import webdriver
from selenium.webdriver.common.by import By


class Home_Page:
    shop_now_xpath = "(//button[text()='Shop Now'])[1]"
    all_products_xpath = "//div[@class='mt-[4rem] flex flex-col justify-center items-center']"
    click_on_add_cart_xpath = "//button[text()='ADD TO CART']"
    email_name = "email"
    password_name = "password"
    log_in_btn_xpath = "//button[text()='LOG IN']"
    click_cart_css = ".w-\[24px\] "
    click_on_checkout_xpath = "//button[text()='CHECKOUT']"



    def __init__(self, driver):
        self.driver = driver


    def Click_on_shop(self):
        self.driver.find_element(By.XPATH, self.shop_now_xpath).click()


    def click_on_add_cart(self):
        self.driver.find_element(By.XPATH, self.click_on_add_cart_xpath).click()

    def user_email(self,user_email):
        self.driver.find_element(By.XPATH, self.email_name).send_keys(user_email)

    def user_password(self,user_password):
        self.driver.find_element(By.XPATH, self.password_name).send_keys(user_password)
        self.driver.find_element(By.XPATH, self.log_in_btn_xpath).click()

    def click_on_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_cart_css).click()

    def click_on_checkout(self):
        self.driver.find_element(By.XPATH, self.click_on_checkout_xpath).click()






