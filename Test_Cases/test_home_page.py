import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from Page_Object.home_page import Home_Page

class Test_Home_page:
    all_product_text = "//div[@class='mt-[4rem] flex flex-col justify-center items-center']/div/h1"
    price_of_product = "//p[@class='font-dmsans font-[400] text-[20px] leading-[24px] tracking-[1px] mb-[15px]']"


    def test_home_page(self,setup):
        self.driver = setup
        self.home_page = Home_Page(self.driver)
        self.home_page.Click_on_shop()
        self.all_products = self.driver.find_elements(By.XPATH, self.all_product_text)

        for self.product in self.all_products:
            print(self.product.text)
            if self.product.text == "Router":
                self.product.click()
                break

        self.price = self.driver.find_element(By.XPATH, self.price_of_product).text
        print("Your total product price on cart page:- ", self.price)
        self.home_page.click_on_add_cart()
        self.home_page.click_on_cart()
        self.home_page.click_on_checkout()

        time.sleep(15)






#https://github.com/orgs/alphabin1/repositories?type=all



















        time.sleep(3)

