import time

from selenium.webdriver.common.by import By
from POM.Base import Base
from selenium.webdriver.support.ui import Select


class HomePage(Base):

    search_box = (By.ID, 'twotabsearchtextbox')
    type_dropdown = (By.ID, 'searchDropdownBox')
    search_button = (By.ID, 'nav-search-submit-button')

    def search_for(self, keyword):
        item = self.find_element(*self.search_box)
        if item is None:
            self.driver.refresh()
        self.send_keys(*self.search_box, keyword)
        element = self.find_element(*self.type_dropdown)
        select = Select(element)
        time.sleep(1)
        select.select_by_visible_text('All Categories')
        self.click_element(*self.search_button)
