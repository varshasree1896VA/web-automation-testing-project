# 🧪 Web Automation Testing Project – Selenium + PyTest

A real-world automation project built from scratch to showcase end-to-end functional testing using **Selenium WebDriver**, **PyTest**, and **HTML Reporting** — with real interview-useful practices like **screenshot capture**, **page object model**, **modular tests**, and **GitHub-ready documentation**.

---

## ✅ Project Overview

This project automates user flows on the [Automation Exercise website](https://automationexercise.com). It includes:

- ✅ Sign-up test (account creation)
- ✅ Login test (with valid & invalid scenarios)
- ✅ Logout test
- ✅ Screenshot capture on test failures
- ✅ Reusable browser fixture via `conftest.py`
- ✅ Modular code using Page Object Model (POM)
- ✅ HTML reports with `pytest-html`
- ✅ Clean file structure following industry standards

---

## 📅 Day-Wise Progress

---

### 🔹 **Day 1 – Project Setup**

📁 _Goals: Environment + First Automation Script_

- ✅ Installed:
  - Python 3.13.x
  - PyCharm (IDE)
  - Google Chrome & ChromeDriver
  - Selenium
  - PyTest

- ✅ Project Structure:
```text
web-automation-testing-project/
├── pages/
├── tests/
├── conftest.py
├── requirements.txt
└── README.md
```

✅ First test:

Opened site, clicked “Signup/Login”

### 🔹 **Day 2 – Page Object Model (POM)**
📁 _Goals: Clean code structure using POM_

✅ Created `home_page.py`, `signup_page.py`, `login_page.py` `in pages/`

✅ Separated element locators + logic from test code

✅ Created `test_signup.py`

✅ Created `utils.py` for helper functions

###  🔹 **Day 3 – Fixtures & Error Handling**
📁 *Goals: Reusable setup + stability*

✅ Created `conftest.py` with browser setup/teardown fixture

✅ Used `WebDriverWait` to avoid flaky tests

✅ Handled "Email already exists" and other edge cases

### 🔹 **Day 4 – Reporting**
📁 _Goals: Generate test execution reports_

✅ Used pytest-html to generate reports:
```bash
pytest tests/ --html=reports/report_<timestamp>.html

```
✅ Structured test folders & modularized page classes

###  🔹 **Day 5 – New Tests + Screenshot Capture**
📁 _Goals: Add more _real_-world scenarios_

✅ ✅ Invalid Login Test (user enters wrong credentials)

✅ ✅ Logout Test (verify session ends)

✅ ✅ Screenshot on Failure — any failed test now saves a screenshot with a timestamped filename in /screenshots/ folder:
`/screenshots/` folder:
```bash
screenshots/
├── test_invalid_login_20250707_131536.png
```
🔧 Screenshot logic is placed in `conftest.py` via `pytest_runtest_makereport` hook:
```python
if report.when == "call" and report.failed:
    screenshot_name = ...
    driver.save_screenshot(...)
```
🔬 Technologies Used
| Tool              | Purpose                       |
| ----------------- | ----------------------------- |
| Python            | Programming language          |
| Selenium          | Browser automation            |
| PyTest            | Test runner                   |
| pytest-html       | HTML reporting                |
| webdriver-manager | Automatic driver download     |
| Git/GitHub        | Version control & CI/CD ready |

🗂️ Project Structure
```text
web-automation-testing-project/
├── pages/
│   ├── home_page.py
│   ├── signup_page.py
│   └── login_page.py
├── tests/
│   ├── test_signup.py
│   ├── test_login.py
│   ├── test_logout.py
│   └── test_homepage.py   # includes invalid login
├── utils/
│   └── utils.py
├── screenshots/
│   └── test_invalid_login_<timestamp>.png
├── reports/
│   └── report_<timestamp>.html
├── conftest.py
├── requirements.txt
└── README.md
```
🚀 How to Run the Tests
```bash
# Step 1: Install all dependencies
pip install -r requirements.txt

# Step 2: Run all tests and generate report
pytest tests/ --html=reports/test_report.html

# Optional: Run only a specific test file
pytest tests/test_signup.py --html=reports/signup_report.html
```
📸 Screenshot Handling
Screenshots are automatically taken on test failures

They are saved in the `/screenshots/` folder with test name + timestamp

Example:
```bash
/screenshots/test_invalid_login_20250707_131536.png
```
✅ All Tests Covered So Far
| Test Name       | File              | Status |
| --------------- | ----------------- | ------ |
| HomePage Load   | test\_homepage.py | ✅      |
| Sign Up (Valid) | test\_signup.py   | ✅      |
| Login (Valid)   | test\_login.py    | ✅      |
| Login (Invalid) | test\_homepage.py | ✅      |
| Logout          | test\_logout.py   | ✅      |

🛠️ Future Enhancements
⏳ Data-driven tests with `@pytest.mark.parametrize`

⏳ Docker container for isolated testing

✅ GitHub Actions for CI/CD (🔜 Next Step)

⏳ Add screenshots to HTML report

⏳ Cross-browser testing (Firefox, Edge)

🙋‍♀️ Author
Varsha Sree Mirdoddi:

🔗 LinkedIn: https://www.linkedin.com/in/varshasreemirdoddi/
