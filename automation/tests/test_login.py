import time
from automation.pages.login_page import LoginPage

def test_valid_login(driver):
    driver.get("http://localhost:3000/login")
    login = LoginPage(driver)
    login.login("test@mail.com", "1234")
    time.sleep(2)
    assert "Dashboard" in driver.page_source

