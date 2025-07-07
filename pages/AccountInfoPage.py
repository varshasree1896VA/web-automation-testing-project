# steps next Create AccountInfoPage.py
# Create a new file in pages/:

# pages/account_info_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AccountInformationPage:
    def __init__(self, browser):
        self.browser = browser

    def select_title(self, title="Mr"):
        if title.lower() == "mr":
            self.browser.find_element(By.ID, "id_gender1").click()
        else:
            self.browser.find_element(By.ID, "id_gender2").click()

    def enter_password(self, password):
        self.browser.find_element(By.ID, "password").send_keys(password)

    def select_dob(self, day, month, year):
        Select(self.browser.find_element(By.ID, "days")).select_by_value(str(day))
        Select(self.browser.find_element(By.ID, "months")).select_by_value(str(month))
        Select(self.browser.find_element(By.ID, "years")).select_by_value(str(year))

    def check_newsletter(self, subscribe=True):
        checkbox = self.browser.find_element(By.ID, "newsletter")
        if subscribe and not checkbox.is_selected():
            checkbox.click()
        elif not subscribe and checkbox.is_selected():
            checkbox.click()

    def check_offers(self, subscribe=True):
        checkbox = self.browser.find_element(By.ID, "optin")
        if subscribe and not checkbox.is_selected():
            checkbox.click()
        elif not subscribe and checkbox.is_selected():
            checkbox.click()

    def enter_first_name(self, first_name):
        self.browser.find_element(By.ID, "first_name").send_keys(first_name)

    def enter_last_name(self, last_name):
        self.browser.find_element(By.ID, "last_name").send_keys(last_name)

    def enter_company(self, company):
        self.browser.find_element(By.ID, "company").send_keys(company)

    def enter_address1(self, address1):
        self.browser.find_element(By.ID, "address1").send_keys(address1)

    def enter_address2(self, address2):
        self.browser.find_element(By.ID, "address2").send_keys(address2)

    def select_country(self, country):
        Select(self.browser.find_element(By.ID, "country")).select_by_visible_text(country)

    def enter_state(self, state):
        self.browser.find_element(By.ID, "state").send_keys(state)

    def enter_city(self, city):
        self.browser.find_element(By.ID, "city").send_keys(city)

    def enter_zipcode(self, zipcode):
        self.browser.find_element(By.ID, "zipcode").send_keys(zipcode)

    def enter_mobile_number(self, mobile_number):
        self.browser.find_element(By.ID, "mobile_number").send_keys(mobile_number)

    def click_create_account(self):
        self.browser.find_element(By.XPATH, "//button[contains(text(),'Create Account')]").click()
