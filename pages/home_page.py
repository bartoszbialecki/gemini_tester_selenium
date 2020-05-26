from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import HomePageLocators
from time import sleep

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

    def add_procuts_to_basket(self, products_count, same_products=False):
        buttons = WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located(HomePageLocators.ADD_PRODUCT_TO_BASKET_BUTTON))
        buttons = [button for button in buttons if button.is_displayed()]

        if same_products:
            for i in range(products_count):
                buttons[0].click()
                sleep(1)
        else:
            count = 1
            for button in buttons:
                button.click()
                sleep(1)

                if count == products_count:
                    break

                count += 1

    def add_products_to_basket_and_compute_total_price(self, count):
        products_list = self.get_list_of_products(
            count, HomePageLocators.PRODUCTS)
        expected_total_price = 0

        for product in products_list:
            price = product["price"]
            expected_total_price += price
            add_to_basket = product["add_to_basket_element"]
            self.driver.execute_script("arguments[0].click();", add_to_basket)
            sleep(2)

        return (products_list, expected_total_price)

    def basket_quantity_should_be_equal(self, count):
        basket_quantity = self.driver.find_element(
            *HomePageLocators.HEADER_BASKET_QUANTITY)

        assert int(basket_quantity.text) == count

    def open_basket(self):
        button = self.driver.find_element(*HomePageLocators.BASKET_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)

    def login_suggestion_dialog_should_be_visible(self):
        dialog = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(HomePageLocators.LOGIN_SUGGESTION_DIALOG))

        assert dialog.is_displayed() == True
