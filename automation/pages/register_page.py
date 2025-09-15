from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.name = (By.NAME, "name")
        self.email = (By.NAME, "email")
        self.password = (By.NAME, "password")
        self.confirm_password = (By.NAME, "confirm_password")
        self.submit_btn = (By.CSS_SELECTOR, "button[type='submit']")

    def register(self, name, email, password, confirm_password):
        self.driver.find_element(*self.name).send_keys(name)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.confirm_password).send_keys(confirm_password)
        self.driver.find_element(*self.submit_btn).click()
