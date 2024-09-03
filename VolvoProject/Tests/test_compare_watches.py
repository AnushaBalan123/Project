import logging
from VolvoProject.Pages.compare_page import ComparePage
from VolvoProject.Pages.home_page import HomePage
from VolvoProject.Pages.watches_page import WatchesPage
from VolvoProject.Tests.test_base import BaseTest

class TestCompareWatches(BaseTest):

    def test_compare_two_watches(self):
        driver = self.driver
        
        logging.info("Navigate to Gear -> Watches section")
        home_page = HomePage(driver)
        home_page.click_on_gear()

        watches_page = WatchesPage(driver)
        
        logging.info("Add the first watch to compare")
        watches_page.add_first_watch_to_compare()

        logging.info("Add the second watch to compare")
        watches_page.add_second_watch_to_compare()

        logging.info("Proceed to compare the selected watches")
        compare_page = ComparePage(driver)
        compare_page.click_compare_button()

        logging.info("Verify that the comparison is successful")
        assert compare_page.is_comparison_successful(), "Comparison failed"