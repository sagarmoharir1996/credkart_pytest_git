import time

import pytest
from selenium import webdriver
chrome_option=webdriver.ChromeOptions()
chrome_option.add_argument("--headless")

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def setup(request):
    browser=request.config.getoption("--browser")
    if browser == "chrome":
        driver=webdriver.Chrome()
    elif browser == "firefox":
        driver=webdriver.Firefox()
    elif browser == "edge":
        driver=webdriver.Edge()
    else:
        driver=webdriver.Chrome(options=chrome_option)



    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(10)

    yield driver
    driver.quit()












