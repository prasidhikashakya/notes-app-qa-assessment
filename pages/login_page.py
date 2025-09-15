from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email = (By.NAME, "email")
        self.password = (By.NAME, "password")
        self.submit_btn = (By.CSS_SELECTOR, "button[type='submit']")

    def login(self, email, password):
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.submit_btn).click()
