import time
from automation.pages.login_page import LoginPage
from automation.pages.notes_page import NotesPage

def test_edit_note(driver):
    driver.get("http://localhost:3000/login")
    login = LoginPage(driver)
    login.login("test@mail.com", "1234")
    time.sleep(2)

    notes = NotesPage(driver)
    notes.edit_first_note("Edited Title", "Edited content")
    time.sleep(2)
    assert "Edited Title" in driver.page_source
