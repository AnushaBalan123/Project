from VolvoProject.Config.config import TestData
from VolvoProject.Pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    
    def __init__(self, driver):
        self.driver = driver
        self.gear_menu_locator = (By.XPATH, "//a[@id='ui-id-6']")
        self.sale_link = (By.LINK_TEXT, "Sale")
        self.watches_link_locator = (By.XPATH, "//a[@id='ui-id-27']") 

    def click_on_gear(self):
        self.driver.find_element(*self.gear_menu_locator).click()

    def go_to_sale_page(self):
        self.click(self.sale_link)

    def click_on_watches(self):
        self.driver.find_element(*self.watches_link_locator).click()