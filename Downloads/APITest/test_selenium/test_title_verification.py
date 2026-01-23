from selenium import webdriver
import logging

class TestTitleVerification:

    driver = webdriver.Chrome()
    log = logging.getLogger(__name__)
    flipkart = 'https://www.flipkart.com/'
    expected_title = '@ Flipkart.com'

    def test_steps(self):
        self.log.info("Launching to Flipkart website")
        self.driver.get(self.flipkart)
        self.driver.maximize_window()
        title = self.driver.title
        self.log.info(title)
        assert self.expected_title in title

    def teardown(self):
        self.driver.quit()