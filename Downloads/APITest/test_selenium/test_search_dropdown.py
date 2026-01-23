import logging
from operator import contains

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestSearchDropdown():
    driver = webdriver.Chrome()
    log = logging.getLogger(__name__)
    url = 'https://www.amazon.in/'
    search_query = "shoes"
    wait = WebDriverWait(driver, 10)
    exepected_list = '//span[contains(@class, "s-heavy")]'
    expected_text = "samsung 5g mobile phone"

    def test_steps(self):
        self.log.info("Launching to Flipkart website")
        #self.driver.implicitly_wait(10)
        if not isinstance(self.url, str):
            raise TypeError("\nInvalid url \nPlease enter a valid url \n\n")
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.wait.until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox')))
        search = self.driver.find_element(By.ID, 'twotabsearchtextbox')
        search.send_keys(self.search_query)
        suggestion = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.exepected_list)))
        lst_text = ['shoes '+x.text for x in suggestion]
        self.log.info("The Actual Text: {}".format(lst_text))
        xpath = f"{self.exepected_list}[contains(., 'for woman')]"
        target = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        target.click()
        assert "for woman" in self.driver.title, "Expected title is not found"


    def teardown(self):
        self.driver.quit()


