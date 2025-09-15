import time
from automation.pages.register_page import RegisterPage

def test_valid_register(driver):
    driver.get("http://localhost:3000/register")
    register = RegisterPage(driver)
    register.register("Test User", "newuser@mail.com", "1234", "1234")
    time.sleep(2)
    assert "Dashboard" in driver.page_source
