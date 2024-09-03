from selenium.webdriver.common.by import By

class BagsPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_locator = (By.XPATH, "//li[@class='item product product-item']//a[@class='product-item-link']")
        self.add_to_cart_button_locator = (By.ID, "product-addtocart-button")
        self.cart_link_locator = (By.XPATH, "//a[@class='action showcart']")

    def select_first_bag(self):
        product = self.driver.find_element(*self.product_locator)
        self.product_name = product.text
        product.click()

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button_locator).click()

    def view_cart(self):
        self.driver.find_element(*self.cart_link_locator).click()

    def get_product_name(self):
        return self.product_name