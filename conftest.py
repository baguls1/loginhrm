import pytest
import os
from utilities.driver_factory import get_driver
from config.config import URL


@pytest.fixture
def setup():
    driver=get_driver()
    driver.get(URL)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Only when test fails
    if report.when == "call" and report.failed:

        driver = item.funcargs['setup']

        # create folder if not exists
        os.makedirs("reports/screenshots", exist_ok=True)

        file_name = f"reports/screenshots/{item.name}.png"

        driver.save_screenshot(file_name)