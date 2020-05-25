from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import LoginPageLocators
from variables import Variables


class LoginPage(BasePage):
    def _verify_page(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(LoginPageLocators.FORM))
        assert Variables.LOGIN_FORM_TITLE in self.driver.page_source

    def enter_email(self, email):
        self.driver.find_element(
            *LoginPageLocators.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(
            *LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def verify_error(self, error):
        tooltip = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(LoginPageLocators.ERROR_TOOLTIP))
        message = tooltip.get_attribute(
            LoginPageLocators.ERROR_TOOLTIP_MESSAGE_ATTRIBUTE)

        assert error == message
