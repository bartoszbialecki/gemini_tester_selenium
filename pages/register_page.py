from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import RegisterPageLocators
from variables import Variables


class RegisterPage(BasePage):
    def _verify_page(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(RegisterPageLocators.FORM))
        assert Variables.REGISTER_FORM_TITLE in self.driver.page_source

    def enter_email(self, email):
        self.driver.find_element(
            *RegisterPageLocators.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(
            *RegisterPageLocators.PASSWORD_INPUT).send_keys(password)

    def enter_password_confirm(self, password):
        self.driver.find_element(
            *RegisterPageLocators.PASSWORD_CONFIRM_INPUT).send_keys(password)

    def accept_privacy_policy(self):
        self.driver.find_element(
            *RegisterPageLocators.PRIVACY_CHECKBOX).click()

    def click_register_button(self):
        self.driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    def is_email_required(self):
        email_input = self.driver.find_element(
            *RegisterPageLocators.EMAIL_INPUT)
        value = email_input.get_attribute("required")
        # valid = self.driver.execute_script(
        #     "return arguments[0].validity.valid;", email_input)

        return value != None
