import selenium
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('www.way2sms.com')
user_name = driver.find_element_by_id('mobileNo')
password = driver.find_element_by_id('password')

user_name.send_keys('9789913644')
password.send_keys('sri2611997')
login_btn = driver.find_element_by_class('btn-theme-sm btn-ls text-uppercase')
login_btn.click()
