from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
from selenium.common.exceptions import NoSuchElementException
@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


class Test_sample:
    def test_one(self, setup):
        self.driver.get('https://www.flipkart.com/')
        assert "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!" in setup.title
        if "Online Shopping Site" in self.driver.title:
            print("Done")
        else:
            print("Not Done")


