import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TestAddToCart:
    driver = webdriver.Chrome()
    log = logging.getLogger(__name__)
    url = "https://www.amazon.in/"
    cart = "nav-cart-count"
    cart_class = '//h3[@class="a-size-large a-spacing-top-base sc-your-amazon-cart-is-empty"]'

    def wait_for_element(self, locator, timeout, condition):
        try:
            WebDriverWait(self.driver, timeout).until(
                condition(locator)
            )
            return True
        except TimeoutException:
            return False

    def finding_element(self):
        value = '//span[@class="a-size-base-plus"]'
        xpath = f"{value}[contains(., 'Sign in to your account')]"
        try:
            self.wait_for_element(locator=(By.XPATH, xpath), timeout=10, condition=EC.visibility_of_element_located)
            return True

        except TimeoutException:
            return False

    def test_steps(self):
        self.driver.get(self.url)
        self.wait_for_element(locator=(By.ID, self.cart), timeout=10,
                              condition=EC.presence_of_element_located), "Cart Option is not found"
        cart = self.driver.find_element(By.ID, self.cart)
        cart.click()
        self.wait_for_element(locator=(By.XPATH, self.cart_class), timeout=10,
                              condition=EC.presence_of_element_located), "Empty cart page not found"
        empty_cart = self.driver.find_element(By.XPATH, self.cart_class)
        cart_text = empty_cart.text
        self.log.info("The cart text {}".format(cart_text))
        assert "Cart is empty" in cart_text
        assert self.finding_element(), "Sign in option is not found"
