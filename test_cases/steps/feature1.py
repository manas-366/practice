import behave
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from behave import *
@Given ("i launched flipkart website")
def f1(context):
    context.driver=webdriver.Chrome()
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)

@when ("i enter {uname} and {pwd} and click on login")
def f2(context,uname,pwd):
    context.driver.find_element(By.XPATH,"//input[@name='username']").send_keys(uname)
    context.driver.find_element (By.XPATH,"//input[@name='password']").send_keys(pwd)
    context.driver.find_element(By.XPATH,"//button[@type='submit']").click()

@Then ("i verify user is successfully logged in or not")
def f3(context):
    a=context.driver.find_element(By.XPATH,'//span[text()="PIM"]')
    if a.is_displayed() is True:
        print("passed")
    else:
        print("login failed")



