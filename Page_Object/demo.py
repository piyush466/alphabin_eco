import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
driver.get("https://demo.alphabin.co/")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "(//button[text()='Shop Now'])[1]").click()
all_product = driver.find_elements(By.XPATH, "//div[@class='mt-[4rem] flex flex-col justify-center items-center']/div/h1")

for product in all_product:
    print(product.text)
    if product.text == "Router":
        product.click()
        break
time.sleep(4)



