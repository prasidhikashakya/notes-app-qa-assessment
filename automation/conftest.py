import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)  # Add this line
    yield driver
    driver.quit()