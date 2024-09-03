from VolvoProject.Config.config import TestData
from VolvoProject.Pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    sign_in = (By.LINK_TEXT, "Sign In")
    email = (By.ID , "email")
    password = (By.ID , "pass")
    login_button = (By.ID , "send2")

    def __init__(self, driver) :
        # self.driver = driver
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def login(self, email, password):
        print("Anusha")
        self.click(self.sign_in)
        self.send_keys(self.email, email)
        self.send_keys(self.password, password)
        self.click(self.login_button)
