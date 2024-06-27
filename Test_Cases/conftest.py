import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get("https://demo.alphabin.co/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()




