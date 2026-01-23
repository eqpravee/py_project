import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestMouseScrolling:
    driver = webdriver.Chrome()
    actions = ActionChains(driver)
    url = "https://www.flipkart.com/"
    element_xpath = '//a[@class="u4vC36 yBSM00"]//img[@class="HmRjOS"]'
    def test_steps(self):
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)
        self.driver.maximize_window()
        element = self.driver.find_element(By.XPATH, self.element_xpath)
        element.click()



    def teardown(self):
        self.driver.quit()

