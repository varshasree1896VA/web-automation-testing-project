# ✅ Step 2: Create login_page.py in pages/
# 📝 File: pages/login_page.py
# pages/login_page.py

from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='login-email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(text(),'Your email or password is incorrect!')]")

        # Page Actions
    def enter_email(self, email):
            self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
            self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
            self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):
            return self.driver.find_element(*self.ERROR_MESSAGE).text

    def get_login_heading(self):
        return self.driver.find_element(By.XPATH, "//h2[text()='Login to your account']").text
