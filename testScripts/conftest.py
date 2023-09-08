import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def pytest_addoption(parser): # This will get the value from CLI / Hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   # This will return the Browser value to setup method
    return request.config.getoption("--browser")