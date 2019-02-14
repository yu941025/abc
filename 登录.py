__author__ = 'Administrator'
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get('http://192.168.1.200:8080/web/device2/#/login')
driver.find_element_by_css_selector('#app > div > form > div:nth-child(2) > div > div > input').send_keys('device')
driver.find_element_by_css_selector('#app > div > form > div:nth-child(3) > div > div > input').send_keys('abc123')
driver.find_element_by_css_selector('#app > div > form > button').click()
