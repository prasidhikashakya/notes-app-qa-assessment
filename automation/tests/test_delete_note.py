import time
from automation.pages.login_page import LoginPage
from automation.pages.notes_page import NotesPage

def test_delete_note(driver):
    driver.get("http://localhost:3000/login")
    login = LoginPage(driver)
    login.login("test@mail.com", "1234")
    time.sleep(2)

    notes = NotesPage(driver)
    notes.delete_first_note()
    time.sleep(2)
    assert True
