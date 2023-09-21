import time

import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'launch browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()


@when(u'Open URL')
def open_url(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


# behave -f allure_behave.formatter:AllureFormatter -o reports/ features
@then(u'compare if the URL has been opened')
def get_title(context):
    context.driver.implicitly_wait(3)
    a = context.driver.title
    if a == 'OrangeHM':
        assert True
    else:
        time.sleep(5)
        allure.attach(context.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
        assert False


@then(u'check if user can login')
def user_login_check(context):
    context.driver.find_element(By.XPATH, '//*[@placeholder="Username"]').send_keys('Admin')
    context.driver.find_element(By.XPATH, '//*[@placeholder="Username"]').send_keys('admin123')
    context.driver.find_element(By.XPATH, '//*[@type="submit"]').click()
    time.sleep(2)


@then(u'close')
def close_browser(context):
    context.driver.close()
