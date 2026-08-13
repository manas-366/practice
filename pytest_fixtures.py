import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Test():

    @pytest.fixture
    def init(self):
        global driver
        driver=webdriver.Chrome()
        self.driver=driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    @pytest.fixture

    def f1_test(self,init):
        print('hello')

    @pytest.mark.run(order=1)
    def test_one(self,init,f1_test):
        self.driver.get('https://www.flipkart.com/')
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//span[@class="b3wTlE" and text()="✕"]').click()
       
        a=self.driver.find_element(By.XPATH,"//span[@class='v1zwn27' and text()='Login']").is_displayed()
        if a==True:
            print('enabled')
        else:
            print('Not Enabled')
        self. driver.close()