from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import BasketPageLocators
from variables import Variables
import re


class BasketPage(BasePage):
    def _verify_page(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(BasketPageLocators.BASKET_BOX))
        assert Variables.BASKET_EMPTY_MESSAGE in self.driver.page_source or Variables.BASKET_MESSAGE in self.driver.page_source

    def click_account_button(self):
        self.driver.find_element(*BasketPageLocators.ACCOUNT_BUTTON).click()

    def user_should_be_logged_in(self, user):
        self.click_account_button()
        user_link = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(BasketPageLocators.USER_EMAIL_LINK))

        assert user == user_link.text

    def logout_user(self):
        self.click_account_button()
        self.driver.find_element(*BasketPageLocators.LOGOUT_LINK).click()
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(BasketPageLocators.LOGOUT_FORM))

        assert Variables.LOGOUT_MESSAGE in self.driver.page_source

    def quantity_of_same_product_should_be_equal(self, count):
        quantity_input = self.driver.find_element(
            *BasketPageLocators.BASKET_PRODUCT_QUANTITY_INPUT)

        assert int(quantity_input.get_attribute("value")) == count

    def total_price_of_the_products_should_be_equal_to(self, price):
        total_price_element = self.driver.find_element(
            *BasketPageLocators.BASKET_FIRST_STEP_TOTAL_PRICE)
        total_price_string = total_price_element.text
        total_price_string = total_price_string.replace(",", ".")
        total_price_string = re.sub(r'[^0-9.]', '', total_price_string)
        total_price = float(total_price_string)

        assert total_price == price
