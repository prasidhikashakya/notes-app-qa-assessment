from selenium.webdriver.common.by import By

class NotesPage:
    def __init__(self, driver):
        self.driver = driver
        self.create_note_btn = (By.ID, "create-note")
        self.title = (By.NAME, "title")
        self.content = (By.NAME, "content")
        self.save_btn = (By.CSS_SELECTOR, "button.save")
        self.first_note_delete = (By.CSS_SELECTOR, ".note-item:first-child .delete-btn")

    def create_note(self, title, content):
        self.driver.find_element(*self.create_note_btn).click()
        self.driver.find_element(*self.title).send_keys(title)
        self.driver.find_element(*self.content).send_keys(content)
        self.driver.find_element(*self.save_btn).click()

    def delete_first_note(self):
        self.driver.find_element(*self.first_note_delete).click()

    def edit_first_note(self, title, content):
        edit_btn = self.driver.find_element(By.CSS_SELECTOR, ".note-item:first-child .edit-btn")
        edit_btn.click()
        self.driver.find_element(By.NAME, "title").clear()
        self.driver.find_element(By.NAME, "title").send_keys(title)
        self.driver.find_element(By.NAME, "content").clear()
        self.driver.find_element(By.NAME, "content").send_keys(content)
        self.driver.find_element(By.CSS_SELECTOR, "button.save").click()