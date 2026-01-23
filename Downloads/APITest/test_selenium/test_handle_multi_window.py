import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TestHandleMultiWindow:
    driver = webdriver.Chrome()
    log = logging.getLogger(__name__)
    url = "https://www.amazon.in/"
    wait = WebDriverWait(driver, 10)
    search_id = "twotabsearchtextbox"
    search_text = "Iphone"
    search_button = "nav-search-submit-button"
    search_result = '(//a[@class="a-link-normal s-line-clamp-2 s-line-clamp-3-for-col-12 s-link-style a-text-normal"])[1]'
    add_to_cart = 'add-to-cart-button'
    buy_now = 'buy-now-button'

    def wait_for_element(self, locator, timeout, condition=EC.visibility_of_element_located):
        try:
            WebDriverWait(self.driver, timeout).until(
                    condition(locator)
                )
            return True
        except TimeoutException:
            return False


    def test_steps(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.wait.until(EC.presence_of_element_located((By.ID, self.search_id)))
        element = self.driver.find_element(By.ID, self.search_id)
        element.send_keys(self.search_text)
        button = self.driver.find_element(By.ID, self.search_button)
        button.click()
        search = self.driver.find_element(By.XPATH, self.search_result)
        search.click()
        windows = self.driver.window_handles
        current_window = self.driver.current_window_handle
        for window in windows:
            if not current_window:
                self.driver.switch_to.window(window)
        assert "Iphone" in self.driver.title, "Expected title is not found"
        
    def teardown(self):
        self.driver.quit()



