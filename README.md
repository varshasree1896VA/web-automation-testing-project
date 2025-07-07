# 🧪 Web Automation Testing Project – Selenium + PyTest

A real-world automation project built from scratch to showcase end-to-end functional testing using **Selenium WebDriver**, **PyTest**, and **HTML reporting**. Designed with internship/job-readiness in mind.

---

## ✅ Project Overview

This project automates user flows on the [Automation Exercise website](https://automationexercise.com). It includes:

- ✅ Sign-up test (account creation)
- ✅ Login test (login + logout) *(to be added)*
- ✅ Reusable fixtures via `conftest.py`
- ✅ PyTest + HTML reports for professional output
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

- ✅ First test:
- Opened site, clicked “Signup/Login”

---

### 🔹 **Day 2 – Page Object Model (POM)**

📁 _Goals: Clean code structure using POM_

- ✅ Created `HomePage` and `SignupPage` under `pages/`
- ✅ Separated test logic from locators
- ✅ Built `test_signup.py`:
- Filled name, email, clicked sign up
- Validated "Enter Account Info" screen
- ✅ Created `utils.py` for helper function:

```python
def generate_random_email():
    ...
```
### 🔹 Day 3 – Fixtures & Error Handling
📁 Goals: Reusable browser setup + robust test flow

✅ Created conftest.py:

```python
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

```
✅ Used fixture in test:
```python
def test_user_signup(browser):
    ...


```

✅ Error handling:

Checked if “Email already exists” before proceeding
Used WebDriverWait() for stability

### 🔹 Day 4 – Reporting & Polish
📁 Goals: Polish, organize & generate reports

✅ Generated HTML report:
```bash
pytest tests/test_signup.py --html=reports/signup_report.html

```
✅ Structured tests:

```text
    tests/test_signup.py
    pages/home_page.py
    pages/signup_page.py
    utils/utils.py

```
✅ Created this README & ready for GitHub push

🔍 Technologies Used
| Tool         | Purpose                         |
| ------------ | ------------------------------- |
| Python       | Programming language            |
| Selenium     | Browser automation              |
| PyTest       | Test runner                     |
| pytest-html  | Generate beautiful test reports |
| ChromeDriver | Control Chrome for tests        |
| Git/GitHub   | Version control & portfolio     |

🗂️ Folder Structure
```text
web-automation-testing-project/
├── pages/
│   ├── home_page.py
│   └── signup_page.py
├── tests/
│   └── test_signup.py
├── utils/
│   └── utils.py
├── conftest.py
├── reports/
│   └── signup_report.html
├── README.md
└── requirements.txt
``` 

📸 Sample Report
Open any report from the reports/ folder in your browser, e.g.:
```bash
    /reports/signup_20250706_180553.html

```
🚀 How to Run
```bash
    # Install dependencies
pip install -r requirements.txt

# Run test and generate report
pytest tests/test_signup.py --html=reports/signup_report.html

```

💡 Future Enhancements
Add login/logout tests

Use @pytest.mark.parametrize

Cross-browser testing (Firefox, Edge)

CI/CD with GitHub Actions

Dockerize for isolation

🙋‍♀️ Author  
**Varsha Sree Mirdoddi**  
🔗 [LinkedIn](https://www.linkedin.com/in/varshasreemirdoddi/)
