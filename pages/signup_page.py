# Day-4 steps and all tasks today
# Step	Feature/Task	Why It Matters	Est. Time
# 1️⃣	🔐 Signup Test	Shows full user lifecycle, creation tested	25 min
# 2️⃣	🧪 Refactor login as fixture	Clean reusable steps via conftest.py	15 min
# 3️⃣	🧾 Generate pytest-html report	Shows professionalism, attachable proof of test results	20 min
# ✅ Step 3: Generate Pytest HTML Report
# 🛠️ 1. Install pytest-html
# In your terminal (inside your virtual env):
#
# bash
# Copy code
# pip install pytest-html
# ✅ This adds the plugin that generates beautiful HTML reports.
#
# 🧪 2. Run your test with --html
# Now run your test like this:
#
# bash
# Copy code
# pytest tests/test_signup.py --html=reports/signup_report.html
# Tip: Create a reports/ folder if you haven’t already, or it will create one automatically.
#
# 📄 3. Open the Report
# After the test runs, open the generated file:
#
# Go to reports/signup_report.html
#
# Double-click to open in browser (or right-click → Open with browser)
#
# 💡 Optional Add-On (Extra)
# If you want to include:
#
# Timestamped reports
#
# Clean naming
#
# You can run this instead:
#
# bash
# Copy code
# pytest tests/test_signup.py --html=reports/signup_$(Get-Date -Format "yyyyMMdd_HHmmss").html
# On Windows CMD, that might not work. In PowerShell, you can use:
#
# powershell
# Copy code
# $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
# pytest tests/test_signup.py --html="reports/signup_$timestamp.html"
# 4️⃣	🧹 Organize files properly	Feature-based test files: test_login.py, test_signup.py	10 min
# 5️⃣	📄 Write README.md	Required for GitHub, resume, and recruiters	25 min
# 6️⃣	🆙 Push to GitHub	Make it publicly viewable — critical for internship outreach	10 min
# 7️⃣	🔗 LinkedIn post (Day 4)	Share your progress and project with the world	15 min
#
# 🟨 Bonus (Advanced, If Time Permits)
# Step	Feature	Why It Helps
# 8️⃣	@pytest.mark.parametrize	Shows deeper Pytest skill, handles multiple test cases easily
# 9️⃣	Cross-browser with fixtures	Demonstrates flexibility and scaling
# 🔟	CI/CD setup with GitHub Actions	Ultimate level: auto-run tests on GitHub push
# Create SignupPage (in pages/signup_page.py)



from selenium.webdriver.common.by import By

class SignupPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, name):
        self.driver.find_element(By.XPATH, "//input[@data-qa='signup-name']").send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(email)

    def click_signup_button(self):
        self.driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()
