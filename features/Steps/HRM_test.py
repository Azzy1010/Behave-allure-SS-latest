import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from page.HRM_test import Login_page


@given(u'launch_browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when(u'Open_URL')
def open_URL(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    time.sleep(5)


@then(u'check_if user can login')
def check_if_user_can_login(context):
    login_locators = Login_page()
    context.driver.find_element(By.XPATH,login_locators.username).send_keys('Admin')
    context.driver.find_element(By.XPATH,login_locators.password).send_keys('admin123')
    context.driver.find_element(By.XPATH,login_locators.click).click()
    context.driver.implicitly_wait(5)
    flag_check = context.driver.title
    if flag_check == 'OrangeHRM':
        assert True
    else:
        assert False

@then(u'close_browser')
def then_close_browser(context):
    context.driver.close()
