import logging
import pytest
from VolvoProject.Pages.bags_page import BagsPage
from VolvoProject.Pages.checkout_page import CheckoutPage
from VolvoProject.Pages.gear_page import GearPage
from VolvoProject.Pages.home_page import HomePage
from VolvoProject.Tests.test_base import BaseTest

class TestBrowserSale(BaseTest):

    def test_browser_sale(self):
        driver = self.driver
        
        logging.info("Scrolldown through sales page")
        home_page = HomePage(driver)
        home_page.go_to_sale_page()
        home_page.scroll_down(1000)