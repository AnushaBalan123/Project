from selenium.webdriver.common.by import By

class GearPage:
    def __init__(self, driver):
        self.driver = driver
        self.bags_link_locator = (By.XPATH, "//a[@id='ui-id-25']")

    def click_on_bags(self):
        bags_link = self.driver.find_element(*self.bags_link_locator)
        self.driver.execute_script("arguments[0].click();", bags_link)