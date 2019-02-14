__author__ = 'Administrator'
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep
import unittest
class sheb_Type(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.get_url='http://192.168.1.200:8080/web/device2'
        self.driver.implicitly_wait(30)
        self.verificationErrors=[]


    def test_chaxun(self):
        driver=self.driver
        driver.get(self.get_url)
        driver.maximize_window()
        #登录
        driver.find_element_by_css_selector('#app > div > form > div:nth-child(2) > div > div > input').send_keys('device')
        driver.find_element_by_css_selector('#app > div > form > div:nth-child(3) > div > div > input').send_keys('abc123')
        driver.find_element_by_css_selector('#app > div > form > button').click()
        sleep(2)
        #切换到设备类型
        driver.get('http://192.168.1.200:8080/web/device2/#/device_type')

        sleep(2)
        #s搜索框
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div/div/input').send_keys('七耳科技ip线路')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div/button').click()
        sleep(2)
        driver.refresh()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div/div/input').send_keys('32口')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div/button').click()
        sleep(2)
        driver.refresh()
        sleep(2)
        #添加
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[1]/div/button').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/form/div[1]/div/div/div/input').send_keys('32口')
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/form/div[2]/div/div/div/input').send_keys('鼎信32口')
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/form/div[3]/div/div/div/input').send_keys('32')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/form/div[4]/div/div/div/div/input').send_keys('32')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[3]/span/button[2]').click()
        sleep(2)
        #修改
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[8]/div/button[2]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/form/div[3]/div/div/div/input').send_keys('1234')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[3]/span/button[2]').click()
        sleep(2)
        #删除
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[8]/div/button[1]').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
        sleep(2)



    def tearDown(self):
        self.assertEqual([],self.verificationErrors)