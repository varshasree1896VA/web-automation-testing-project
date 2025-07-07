# Next step after login
# Here’s a quick logout test example you can add to your tests/test_login.py or a new file tests/test_logout.py:

from pages.homepage import HomePage
from pages.login_page import LoginPage
from utils import config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_logout(browser):
    browser.get(config.BASE_URL)

    # Login first
    home_page = HomePage(browser)
    home_page.click_signup_login()

    login_page = LoginPage(browser)
    login_page.enter_email(config.VALID_EMAIL)
    login_page.enter_password(config.VALID_PASSWORD)
    login_page.click_login()

    # Wait for login success confirmation
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f"//a[contains(., 'Logged in as') and .//b[text()='{config.EXPECTED_USERNAME}']]")
        )
    )

    # Click logout
    home_page.click_logout()  # Make sure you have this method in your HomePage class

    # Wait for logout confirmation, e.g., login/signup button visible again
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.LINK_TEXT, "Signup / Login")
        )
    )

    # Optionally, assert that login/signup button is visible on page
    assert "Signup / Login" in browser.page_source
