from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

    def _verify_page(self):
        return

    def get_list_of_products(self, products_count, locator):
        products_list = []
        products = WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located(locator))
        products = [product for product in products if product.is_displayed()]

        count = 1
        for product in products:
            product_info = dict()

            name = self.driver.execute_script(
                "return arguments[0].querySelector('.name a').text.trim();", product)
            product_info["name"] = name

            link = self.driver.execute_script(
                "return arguments[0].querySelector('.name a').href;", product)
            product_info["link"] = link

            price_string = self.driver.execute_script(
                "return arguments[0].querySelector('.price span').innerHTML;", product)
            price_string = price_string.replace(",", ".")
            price = float(price_string)
            product_info["price"] = price

            basket_element = self.driver.execute_script(
                "return arguments[0].querySelector('.st_button-basket-submit-enabled');", product)
            product_info["add_to_basket_element"] = basket_element

            if basket_element.is_displayed():
                products_list.append(product_info)

                if count == products_count:
                    break

                count += 1

        return products_list
