from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button_locator = (By.XPATH, "//button[@id='top-cart-btn-checkout']")

    def proceed_to_checkout(self):
        checkout_button = self.driver.find_element(*self.checkout_button_locator)
        self.driver.execute_script("arguments[0].click();", checkout_button)
        assert "Checkout" in self.driver.title