import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Test_page:
    @pytest.fixture(scope='class')
    def init(request):
        driver = webdriver.Chrome()
        request.cls.driver = driver
        driver.maximize_window()
        driver.implicitly_wait(5)
        yield driver
        driver.quit()


    def test_one(self, init):
        # driver is provided by the `init` fixture and attached to the test class
        self.driver.maximize_window()

    def test_title(self, init):
        self.driver.get('https://www.flipkart.com/')
        try:
            self.driver.find_element(By.XPATH, '//span[@class="b3wTlE" and text()="✕"]').click()
        except NoSuchElementException:
            # popup not present — continue
            pass
        assert ('Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!') in self.driver.title
