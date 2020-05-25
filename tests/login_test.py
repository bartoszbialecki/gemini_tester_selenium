import unittest
import os
import csv
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from variables import Variables
from time import sleep
from utils.utils import get_data
from ddt import ddt, data, unpack

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(
    CURRENT_DIR, '..', 'test_data/invalid_login_credentials.csv')


@ddt
class LoginTest(BaseTest):
    def setUp(self):
        super().setUp()
        home_page = HomePage(self.driver)
        home_page.click_account_button()
        home_page.click_login_button()

    @data(*get_data(DATA_PATH))
    @unpack
    def test_invalid_credentials(self, email, password, error_message):
        if email == "VALID_EMAIL":
            email = Variables.VALID_EMAIL

        if password == "VALID_PASSWORD":
            password = Variables.VALID_PASSWORD

        login_page = LoginPage(self.driver)

        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login_button()

        login_page.verify_error(error_message)

    def test_valid_credentials(self):
        login_page = LoginPage(self.driver)

        login_page.enter_email(Variables.VALID_EMAIL)
        login_page.enter_password(Variables.VALID_PASSWORD)
        login_page.click_login_button()

        basket_page = BasketPage(self.driver)

        basket_page.check_user_is_logged_in(Variables.VALID_EMAIL)

        basket_page.logout()


if __name__ == "__main__":
    unittest.main(verbosity=2)
