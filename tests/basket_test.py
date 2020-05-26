import unittest
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.basket_page import BasketPage
from variables import Variables
from time import sleep


class BasketTest(BaseTest):
    def test_add_2_different_products(self):
        home_page = HomePage(self.driver)
        home_page.add_procuts_to_basket(2)

        home_page.basket_quantity_should_be_equal(2)

    def test_add_2_same_products(self):
        home_page = HomePage(self.driver)
        home_page.add_procuts_to_basket(2, True)
        home_page.open_basket()

        basket_page = BasketPage(self.driver)

        basket_page.quantity_of_same_product_should_be_equal(2)

    def test_add_3_products(self):
        home_page = HomePage(self.driver)
        home_page.add_procuts_to_basket(3)

        home_page.login_suggestion_dialog_should_be_visible()

    def test_add_correct_products_to_basket(self):
        home_page = HomePage(self.driver)
        products, expected_total_price = home_page.add_products_to_basket_and_compute_total_price(
            2)
        home_page.open_basket()

        basket_page = BasketPage(self.driver)

        basket_page.total_price_of_the_products_should_be_equal_to(
            expected_total_price)


if __name__ == "__main__":
    unittest.main(verbosity=2)
