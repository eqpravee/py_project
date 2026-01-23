import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestScrolling:

    driver = webdriver.Chrome()
    url = "https://www.flipkart.com/"

    def test_steps(self):

        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        self.driver.quit()



