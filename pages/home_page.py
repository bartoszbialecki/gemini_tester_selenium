from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import HomePageLocators

PAGE_TITLE = "Apteka Internetowa – Apteka Gemini"


class HomePage(BasePage):
    def _verify_page(self):
        assert PAGE_TITLE in self.driver.title
        self.close_cookie_dialog()

    def close_cookie_dialog(self):
        dialog = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(HomePageLocators.COOKIES_DIALOG))
        dialog_ok_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(HomePageLocators.COOKIES_DIALOG_OK_BUTTON))
        dialog_ok_button.click()

    def click_account_button(self):
        account_link = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(HomePageLocators.ACCOUNT_LINK))
        account_link.click()

    def click_register_button(self):
        register_link = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(HomePageLocators.REGISTER_LINK))
        register_link.click()

    def click_login_button(self):
        login_link = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(HomePageLocators.LOGIN_LINK))
        login_link.click()
