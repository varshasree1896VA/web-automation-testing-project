#  Day 4 next step: Create Test — tests/test_signup.py

import random
import string
from pages.homepage import HomePage
from pages.signup_page import SignupPage
from pages.AccountInfoPage import AccountInformationPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def generate_random_email():
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"testUser_{random_part}@example.com"

def test_user_signup(browser):
    browser.get("https://automationexercise.com")

    # Step 1: Click Signup/Login
    home_page = HomePage(browser)
    home_page.click_signup_login()

    # Step 2: Fill signup form with name & email
    signup_page = SignupPage(browser)
    signup_page.enter_name("Test User")
    email = generate_random_email()  # email I gave: projecttest@gmail.com
    print("✅ Email entered:", email)  # ✅ Add this line for debugging
    signup_page.enter_email(email)
    signup_page.click_signup_button()
    browser.save_screenshot("after_click_signup.png")
    print(browser.page_source)

    # Optional: Fail early if email exists
    if "Email Address already exist!" in browser.page_source:
        raise Exception("Signup failed: Email already exists.")

    # Step 3: Wait for Account Information page to load
    WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.XPATH, "//b[text()='Enter Account Information']"))
    )

    # Step 4: Fill the account information form
    account_info = AccountInformationPage(browser)
    account_info.select_title("Mr")
    account_info.enter_password("Test@1234")
    account_info.select_dob(day=10, month=5, year=1990)
    account_info.check_newsletter(subscribe=True)
    account_info.check_offers(subscribe=True)
    account_info.enter_first_name("Test")
    account_info.enter_last_name("User")
    account_info.enter_company("My Company")
    account_info.enter_address1("123 Test St")
    account_info.enter_address2("Suite 100")
    account_info.select_country("United States")
    account_info.enter_state("California")
    account_info.enter_city("Los Angeles")
    account_info.enter_zipcode("90001")
    account_info.enter_mobile_number("+1234567890")

    # Step 5: Submit form
    account_info.click_create_account()

    # Step 6: Debug info (if something fails)
    browser.save_screenshot("debug_after_create_account.png")
    print(browser.page_source)

    # Step 7: Wait for confirmation page or home page element (adjust as needed)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//b[text()='Account Created!']"))
    )

    # Step 8: Take screenshot
    browser.save_screenshot("signup_complete.png")
