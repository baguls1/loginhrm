from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:  #represent login page of the application
    #locators
    #onc class =one web page
    #constructor
    def __init__(self,driver):
        self.driver=driver
        #This stores the browser instance
#why we need constructor in page class? =All methods need driver
#We pass driver to the page class so all methods can interact with the browser.
        self.wait = WebDriverWait(driver, 10)
#locators
    username= (By.NAME,"username")
    password= (By.NAME,'password')
    login_button= (By.XPATH,"//button[@type='submit']")


    def enter_username(self, user):
        element = self.wait.until(EC.visibility_of_element_located(self.username))
        element.clear()
        element.send_keys(user)

    def enter_password(self, pwd):
        element = self.wait.until(EC.visibility_of_element_located(self.password))
        element.clear()
        element.send_keys(pwd)

    def click_login(self):
        element = self.wait.until(EC.element_to_be_clickable(self.login_button))
        element.click()
