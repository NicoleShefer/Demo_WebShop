# Demo Web Shop UI Tests 🛒

UI test automation for the login form of the [Demo Web Shop](https://demowebshop.tricentis.com/) web application. Built as homework (HW12), with the focus on automating negative test scenarios.

## 🛠 Tech Stack
- **Language:** Python 3
- **Test framework:** pytest
- **Browser automation:** Selenium WebDriver
- **Secrets management:** python-dotenv
- **Design pattern:** Page Object Model (POM)

## 📁 Project Structure
- `pages/base_page.py`: base page class that wraps explicit waits (`WebDriverWait`)
- `pages/login_page.py`: login page class with locators and interaction methods
- `test_login.py`: test cases with assertions
- `conftest.py`: pytest configuration and fixtures (WebDriver setup)

## 🧪 Test Scenarios
1. **Login form availability:** checks that the login link and form elements are visible
2. **Valid login (positive):** logs in successfully with valid credentials
3. **Invalid email format (negative):** attempts to log in with a malformed email
4. **Unregistered email (negative):** attempts to log in with an email that has no account
5. **Wrong password (negative):** attempts to log in with a valid email and an incorrect password

## 🚀 Running the Tests Locally

1. **Clone the repository**
   ```bash
   git clone <your_repository_link>
   cd <repository_folder_name>
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv

   # macOS / Linux
   source venv/bin/activate

   # Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install pytest selenium python-dotenv
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root with the following values:
   ```env
   TEST_USER_PASSWORD=your_valid_password
   TEST_USER_WRONG_PASSWORD=any_wrong_password
   ```

5. **Run the tests**
   ```bash
   pytest -v
   ```
