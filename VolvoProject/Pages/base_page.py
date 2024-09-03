from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This class is the parent of all pages"""
class BasePage:
    def __init__(self, driver) :
        self.driver = driver
    
    def click(self, by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def find_element(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def find_elements(self, by_locator):
        return self.wait.until(EC.visibility_of_all_elements_located(by_locator))
    
    def get_title(self):
        return self.driver.title

    def scroll_down(self, pixels=1000):
        self.driver.execute_script(f"window.scrollBy(0,{pixels});")
