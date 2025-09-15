import time
from automation.pages.login_page import LoginPage
from automation.pages.notes_page import NotesPage

def test_create_note(driver):
    driver.get("http://localhost:3000/login")
    login = LoginPage(driver)
    login.login("test@mail.com", "1234")
    time.sleep(2)

    notes = NotesPage(driver)
    notes.create_note("Automation Test Note", "This note was created by Selenium.")
    time.sleep(2)
    assert "Automation Test Note" in driver.page_source

