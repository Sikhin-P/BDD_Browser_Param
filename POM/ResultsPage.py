import time

from selenium.webdriver.common.by import By
from POM.Base import Base


class ResultsPage(Base):

    def top_results(self, n):
        results = []
        for i in range(1,n+1):
            name = (
                By.XPATH,
                f'//div[@data-component-type = "s-search-result"][{i}]//span[contains(@class, "a-text-normal")]')
            price = (By.XPATH, f'//div[@data-component-type = "s-search-result"][{i}]//span[@class = "a-price-whole"]')
            item = self.wait_element(*name)
            if item is None:
                break
            item_name = item.text

            item = self.wait_element(*price)
            if not item:
                break
            item_price = item.text
            results.append([item_name, item_price])
        return results
