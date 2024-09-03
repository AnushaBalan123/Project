from selenium.webdriver.common.by import By

class WatchesPage:
    def __init__(self, driver):
        self.driver = driver
        self.clamber_watch_locator = (By.XPATH, "//a[@class='product-item-link' and contains(text(),'Clamber Watch')]")
        self.didi_sport_watch_locator = (By.XPATH, "//a[@class='product-item-link' and contains(text(),'Didi Sport Watch')]")

        self.add_to_compare_locator = (By.XPATH, "//a[@class='action tocompare']")

    def select_first_watch(self):
        self.driver.find_element(*self.clamber_watch_locator).click()

    def select_second_watch(self):
        self.driver.find_element(*self.didi_sport_watch_locator).click()

    def add_first_watch_to_compare(self):
        self.driver.find_element(*self.clamber_watch_locator).click()

    def add_second_watch_to_compare(self):
        self.driver.find_element(*self.didi_sport_watch_locator).click()
