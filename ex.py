import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Test_page:
    @pytest.fixture
    def test_one(self):
        driver=webdriver.Chrome()
        self.driver=driver
        self.driver.maximize_window()

    def test_title(self,test_one):
        self.driver.get('https://www.flipkart.com/')
        self.driver.find_element(By.XPATH,'//span[@class="b3wTlE" and text()="✕"]').click()
        assert ('Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!') in self. driver.title
        self.driver.quit()