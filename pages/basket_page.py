from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import BasketPageLocators
from variables import Variables


class BasketPage(BasePage):
    def _verify_page(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(BasketPageLocators.BASKET_BOX))
        assert Variables.BASKET_EMPTY_MESSAGE in self.driver.page_source or Variables.BASKET_MESSAGE in self.driver.page_source

    def click_account_button(self):
        self.driver.find_element(*BasketPageLocators.ACCOUNT_BUTTON).click()

    def check_user_is_logged_in(self, user):
        self.click_account_button()
        user_link = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(BasketPageLocators.USER_EMAIL_LINK))

        assert user == user_link.text

    def logout(self):
        self.click_account_button()
        self.driver.find_element(*BasketPageLocators.LOGOUT_LINK).click()
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(BasketPageLocators.LOGOUT_FORM))

        assert Variables.LOGOUT_MESSAGE in self.driver.page_source
