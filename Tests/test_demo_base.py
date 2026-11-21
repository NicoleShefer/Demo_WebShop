import pytest

from Pages.demo_login_page import LoginPage
from Pages.demo_registration_page import DemoRegistrationPage
from Pages.demo_shop_page import ShopPage
from Tests.data import VALID_EMAIL, VALID_PASSWORD


class BaseTest:
    """Parent class: common preconditions for all tests."""

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.registration_page = DemoRegistrationPage(driver)
        self.shop_page = ShopPage(driver)

    @pytest.fixture
    def login_form_opened(self, setup):
        self.login_page.open_login_page()

    @pytest.fixture
    def logged_in(self, login_form_opened):
        self.login_page.login(VALID_EMAIL, VALID_PASSWORD)
        assert self.login_page.is_log_out_displayed(), "Precondition failed: login"