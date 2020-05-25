import unittest
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from time import sleep

VALID_EMAIL = "tajiye2268@hubopss.com"
VALID_PASSWORD = "test1234"
SHORT_PASSWORD = "1234"
OTHER_PASSWORD = "test1235"
USER_ALREADY_EXISTS_MESSAGE = "Taki użytkownik już istnieje."
PASSWORD_TOO_SHORT_MESSAGE = "Podane hasło jest za krótkie min. 6 znaków."
NO_PASSWORD_MESSAGE = "Brak hasła."
PASSWORD_NOT_MATCH_MESSAGE = "Hasła nie są takie same."
ACCEPT_PRIVACY_MESSAGE = "Zaakceptuj regulamin"


class RegisterTest(BaseTest):
    def setUp(self):
        super().setUp()
        home_page = HomePage(self.driver)
        home_page.click_account_button()

    def test_existing_email(self):
        register_page = RegisterPage(self.driver)

        register_page.enter_email(VALID_EMAIL)
        register_page.enter_password(VALID_PASSWORD)
        register_page.enter_password_confirm(VALID_PASSWORD)
        register_page.accept_privacy_policy()
        register_page.click_register_button()

        assert USER_ALREADY_EXISTS_MESSAGE in self.driver.page_source

    def test_empty_email(self):
        register_page = RegisterPage(self.driver)

        register_page.enter_password(VALID_PASSWORD)
        register_page.enter_password_confirm(VALID_PASSWORD)
        register_page.accept_privacy_policy()
        register_page.click_register_button()

        assert register_page.is_email_required() == True

    def test_short_password(self):
        register_page = RegisterPage(self.driver)

        register_page.enter_email(VALID_EMAIL)
        register_page.enter_password(SHORT_PASSWORD)
        register_page.enter_password_confirm(SHORT_PASSWORD)
        register_page.accept_privacy_policy()
        register_page.click_register_button()

        assert PASSWORD_TOO_SHORT_MESSAGE in self.driver.page_source

    def test_empty_password(self):
        register_page = RegisterPage(self.driver)

        register_page.enter_email(VALID_EMAIL)
        register_page.accept_privacy_policy()
        register_page.click_register_button()

        assert NO_PASSWORD_MESSAGE in self.driver.page_source

    def test_different_passwords(self):
        register_page = RegisterPage(self.driver)

        register_page.enter_email(VALID_EMAIL)
        register_page.enter_password_confirm(VALID_PASSWORD)
        register_page.enter_password_confirm(OTHER_PASSWORD)
        register_page.accept_privacy_policy()
        register_page.click_register_button()

        assert PASSWORD_NOT_MATCH_MESSAGE in self.driver.page_source

    def test_not_checked_privacy_policy(self):
        register_page = RegisterPage(self.driver)

        register_page.enter_email(VALID_EMAIL)
        register_page.enter_password_confirm(VALID_PASSWORD)
        register_page.enter_password_confirm(VALID_PASSWORD)
        register_page.click_register_button()

        assert ACCEPT_PRIVACY_MESSAGE in self.driver.page_source


if __name__ == "__main__":
    unittest.main(verbosity=2)
