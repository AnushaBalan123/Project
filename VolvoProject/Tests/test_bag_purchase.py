import pytest
import logging
from VolvoProject.Pages.bags_page import BagsPage
from VolvoProject.Pages.checkout_page import CheckoutPage
from VolvoProject.Pages.gear_page import GearPage
from VolvoProject.Pages.home_page import HomePage
from VolvoProject.Tests.test_base import BaseTest
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class TestBagPurchase(BaseTest):

    def test_bag_purchase(self):
        driver = self.driver
        logging.info("Navigate to Gear section")
        
        home_page = HomePage(driver)
        home_page.click_on_gear()

        logging.info("Select Bags sub-category")
        gear_page = GearPage(driver)
        gear_page.click_on_bags()

        logging.info("Select the first bag, add to cart, and verify")
        bags_page = BagsPage(driver)
        bags_page.select_first_bag()
        bags_page.add_to_cart()
        bags_page.view_cart()

        logging.info("Verify that the product is available in the cart")
        assert bags_page.get_product_name() in driver.page_source
        