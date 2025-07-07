# conftest.py


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from datetime import datetime

from selenium.webdriver.remote.webdriver import WebDriver
from _pytest.runner import TestReport
from _pytest.nodes import Item

# ✅ Add Type Hints (Optional, to reduce warnings)the above three are for warnings

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


# ✅ Pytest hook: Take screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browser")
        if driver:
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name
            screenshot_path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")

            driver.save_screenshot(screenshot_path)
            print(f"\n📸 Screenshot taken: {screenshot_path}")
