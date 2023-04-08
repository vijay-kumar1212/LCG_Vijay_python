import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

#@pytest.mark.usefixtures("setup")
from utilities.BaseClass import BaseClass


class Testone(BaseClass):

    def test_method(self):
        self.driver.find_element(By.CSS_SELECTOR, '#autosuggest').send_keys('In')
        time.sleep(3)
        Countries = self.driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
        print(Countries)
        print(len(Countries))
        for country in Countries:
            if country.text == "India":  # .text method will retrieve the text value which is loaded default.
                country.click()
                break

        time.sleep(7)
        check = self.driver.find_element(By.CSS_SELECTOR, '#autosuggest').get_attribute('value')
        # get_attribute('value') method we use to retrieve the text value which uploaded dynamically
        assert 'India' in check
        print(""success)
