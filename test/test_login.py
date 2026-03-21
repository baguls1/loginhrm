from pages.login_page import LoginPage
import pytest
#from config.config import username,password

@pytest.mark.parametrize("username,password", [("Admin", "admin123"),("admin1","wrongpass")])
def test_valid_login(setup,username,password):
    driver=setup
    login =LoginPage(driver) #create an object of login page class

    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    # added assertion to verify successful login
    assert "dashboard" in driver.current_url, "Login failed, dashboard not found in URL"
#swith to new branch