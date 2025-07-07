# Next step Write Valid Login Test
# In your tests/test_homepage.py (or better, create a new tests/test_login.py file for login-specific tests to keep things organized)

from pages.homepage import HomePage
from pages.login_page import LoginPage
from utils import config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_valid_login(browser):
    browser.get(config.BASE_URL)

    # Go to login page
    home_page = HomePage(browser)
    home_page.click_signup_login()

    # Enter credentials and log in
    login_page = LoginPage(browser)
    login_page.enter_email(config.VALID_EMAIL)
    login_page.enter_password(config.VALID_PASSWORD)
    login_page.click_login()

    # Save screenshot for verification
    browser.save_screenshot("after_login.png")

    # Final check with bold username
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f"//a[contains(., 'Logged in as') and .//b[text()='{config.EXPECTED_USERNAME}']]")
        )
    )

    # Assert final state
    #expected_text = f"Logged in as {config.EXPECTED_USERNAME}"
    #assert expected_text in browser.page_source
