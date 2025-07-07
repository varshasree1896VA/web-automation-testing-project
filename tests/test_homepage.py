# ✅ STEP 5: Write First Test Case
# In tests/test_homepage.py:
# ✅ STEP 6: Run the Test
# In your terminal from the project root folder:
#
# Page Object Model
# 🧪 Step 2: Update test_homepage.py to use this
# Now go to tests/test_homepage.py and update it like this:

# tests/test_homepage.py

from pages.homepage import HomePage
from pages.login_page import LoginPage  # Add this line
from utils import config

def test_homepage_title(browser):
    browser.get(config.BASE_URL)
    home_page = HomePage(browser)
    assert "Automation" in home_page.get_title()

def test_click_signup_login(browser):
    browser.get(config.BASE_URL)  # ✅ ADD THIS LINE to open the page
    homepage = HomePage(browser)
    #homepage.load()
    homepage.click_signup_login()

    assert "login" in browser.current_url.lower()

def test_login_page_heading(browser):  # ✅ Add this new test
    browser.get(config.BASE_URL)
    homepage = HomePage(browser)
    homepage.click_signup_login()

    login_page = LoginPage(browser)
    heading = login_page.get_login_heading()

    assert heading.strip() == "Login to your account"

# next 🚨 Step 4: Add Test for Invalid Login
# This will simulate a user trying to log in with wrong email/password, and make sure the error message is shown.
#
# ✅ Step-by-Step: Add test_invalid_login()
# ✏️ 1.  update by Adding this to test_homepage.py:

def test_invalid_login(browser):
    browser.get(config.BASE_URL)
    homepage = HomePage(browser)
    homepage.click_signup_login()

    login_page = LoginPage(browser)
    login_page.enter_email("wrong@example.com")        # Invalid email
    login_page.enter_password("wrongpassword123")      # Invalid password
    login_page.click_login()

    error = login_page.get_error_message()

    assert "incorrect" in error.lower()  # Error text should contain "incorrect"
    #assert "Successful Login" in error.lower()  # ❌ On purpose wrong
