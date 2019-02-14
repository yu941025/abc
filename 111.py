__author__ = 'Administrator'
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains



driver=webdriver.Chrome()
driver.get('http://192.168.1.200:8080/web/device2/#/login')
driver.maximize_window()
driver.find_element_by_css_selector('#app > div > form > div:nth-child(2) > div > div > input').send_keys('device')
driver.find_element_by_css_selector('#app > div > form > div:nth-child(3) > div > div > input').send_keys('abc123')
driver.find_element_by_css_selector('#app > div > form > button').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[21]/div/div/button[4]').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[21]/div/div/button[3]').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
sleep(2)