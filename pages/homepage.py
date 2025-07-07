# ✅ STEP 4: Create My First Page Object
# In pages/homepage.py:

# ✅ What to Test on the Homepage:
# Let’s assume we are testing a sample web application like:
# 📎 https://automationexercise.com/
# (this is a  Practice website site for automation testing engineers)
#
# We'll write tests for:
#
# Verifying the homepage title ✅ (you already did).
#
# Verifying Signup/login functionality (we’ll add this next).
#
# Verifying some UI elements like signup/login.

#🔧 Step 1: Create homepage.py inside pages/
# 🔹 load() → loads the home page
# 🔹 click_signup_login() → clicks the "Signup / Login" link

# pages/homepage.py

#from utils import config
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Page Actions

 #   def load(self):
  #      self.driver.get(config.BASE_URL)

    def get_title(self):
        return self.driver.title

    def click_signup_login(self):
        self.driver.find_element(By.XPATH, "//a[@href='/login']").click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()



