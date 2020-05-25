import unittest
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from variables import Variables
from time import sleep


class RegisterTest(BaseTest):
    def setUp(self):
        super().setUp()
        home_page = HomePage(self.driver)
        home_page.click_account_button()
        home_page.click_register_button()

    def test_existing_email(self):
        register_page = RegisterPage(self.driver)

        register_page.enter_email(Variables.VALID_EMAIL)
        register_page.enter_password(Variables.VALID_PASSWORD)
        register_page.enter_password_confirm(Variables.VALID_PASSWORD)
        register_page.accept_privacy_policy()
        register_page.click_register_button()

        assert Variables.USER_ALREADY_EXISTS_MESSAGE in self.driver.page_source

    def test_empty_email(self):
        register_page = RegisterPage(self.driver)

        register_page.enter_password(Variables.VALID_PASSWORD)
        register_page.enter_password_confirm(Variables.VALID_PASSWORD)
        register_page.accept_privacy_policy()
        register_page.click_register_button()

        assert register_page.is_email_required() == True

    def test_short_password(self):
        register_page = RegisterPage(self.driver)

        register_page.enter_email(Variables.VALID_EMAIL)
        register_page.enter_password(Variables.SHORT_PASSWORD)
        register_page.enter_password_confirm(Variables.SHORT_PASSWORD)
        register_page.accept_privacy_policy()
        register_page.click_register_button()

        assert Variables.PASSWORD_TOO_SHORT_MESSAGE in self.driver.page_source

    def test_empty_password(self):
        register_page = RegisterPage(self.driver)

        register_page.enter_email(Variables.VALID_EMAIL)
        register_page.accept_privacy_policy()
        register_page.click_register_button()

        assert Variables.NO_PASSWORD_MESSAGE in self.driver.page_source

    def test_different_passwords(self):
        register_page = RegisterPage(self.driver)

        register_page.enter_email(Variables.VALID_EMAIL)
        register_page.enter_password_confirm(Variables.VALID_PASSWORD)
        register_page.enter_password_confirm(Variables.OTHER_PASSWORD)
        register_page.accept_privacy_policy()
        register_page.click_register_button()

        assert Variables.PASSWORD_NOT_MATCH_MESSAGE in self.driver.page_source

    def test_not_checked_privacy_policy(self):
        register_page = RegisterPage(self.driver)

        register_page.enter_email(Variables.VALID_EMAIL)
        register_page.enter_password_confirm(Variables.VALID_PASSWORD)
        register_page.enter_password_confirm(Variables.VALID_PASSWORD)
        register_page.click_register_button()

        assert Variables.ACCEPT_PRIVACY_MESSAGE in self.driver.page_source


if __name__ == "__main__":
    unittest.main(verbosity=2)
