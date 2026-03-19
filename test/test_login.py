from pages.login_page import LoginPage
from config.config import username,password

def test_valid_login(setup):
    driver=setup
    login =LoginPage(driver) #create an object of login page class

    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    # added assertion to verify successful login
    assert "dashboard" in driver.current_url, "Login failed, dashboard not found in URL"
