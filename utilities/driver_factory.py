from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#This function initializes the Chrome WebDriver, maximizes the browser window, and returns the driver instance for use in test scripts.
def get_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

# The `get_driver` function initializes the Chrome WebDriver using the `webdriver_manager` library, which automatically manages the browser driver. It then maximizes the browser window and returns the driver instance for use in test scripts. This function can be imported and called in test setup to create a browser instance for testing.
# Note: Ensure that the `webdriver_manager` library is installed in your Python environment to use this function. You can install it using pip:
# pip install webdriver_manager
# Additionally, make sure to have the appropriate version of Chrome installed on your machine for compatibility with the WebDriver.

