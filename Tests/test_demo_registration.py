import os
import time

from Pages.demo_registration_page import DemoRegistrationPage

PASSWORD = os.getenv("DEMO_SHOP_PASSWORD", "test123456")


def unique_email():
    return f"nicole_{int(time.time())}@example.com"


def test_successful_registration(driver):
    page = DemoRegistrationPage(driver)
    page.open_registration_page()
    page.fill_first_name("Nicole")
    page.fill_last_name("Test")
    page.fill_email(unique_email())
    page.fill_password(PASSWORD)
    page.fill_confirm_password(PASSWORD)
    page.click_register_button()
    result = page.get_result_text()
    print(repr(result))
    assert "registration completed" in result.lower()

