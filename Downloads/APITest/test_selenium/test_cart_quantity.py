import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestCartQuantity:

    driver = webdriver.Chrome()
    log = logging.getLogger(__name__)
    url = "https://www.amazon.in/"
    product_xpath = '(//div[@class="a-image-container a-dynamic-image-container _quad-multi-asin-card-v2_style_quadrantImageContainer__2QeUm"])[1]'
    add_to_cart = "add-to-cart-button"
    go_to_cart = "//a[@href='/cart?ref_=sw_gtc']"
    add_element = '//span[@class="a-icon a-icon-small-add"]'


    def wait_for_element(self, locators, timeout, condition):

        try:
            WebDriverWait(self.driver, timeout).until(
                condition(locators)
            )
            return True

        except TimeoutException:
            return False

    def select_element(self, locator, value, select=False):
        try:
            element = self.driver.find_element(locator, value)
            if select:
                element.click()
        except NoSuchElementException:
            return "No Such Element found Exception"


    def test_steps(self):
        self.driver.get(self.url)
        self.select_element(locator=By.XPATH, value=self.product_xpath, select=True)
        self.select_element(By.ID, self.add_to_cart, select=True)
        self.select_element(By.XPATH, self.go_to_cart, select=True)
        self.select_element(By.XPATH, self.add_element, select=True)



