from selenium.webdriver.common.by import By

class ComparePage:
    def __init__(self, driver):
        self.driver = driver
        self.compare_button_locator = (By.XPATH, "//button[@title='Compare']")

    def click_compare_button(self):
        self.driver.find_element(*self.compare_button_locator).click()

    def is_comparison_successful(self):
        return "Compare Products" in self.driver.page_source