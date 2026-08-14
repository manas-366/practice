from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest

class Test1():
    @pytest.fixture()
    def one(self):
        driver=webdriver.Chrome()
        self.driver=driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_one(self,one):
        self.driver.get("https://www.flipkart.com/")
        self.driver.find_element(By.XPATH,'//span[@class="b3wTlE" and text()="✕"]').click()
        self.driver.close()
