__author__ = 'Administrator'
from selenium import webdriver
from time import sleep
import unittest

class kaiguanji(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.get_url='http://192.168.1.200:8080/web/device2/'
        self.driver.implicitly_wait(30)
        self.verificationError=[]
    def test_kaiguanji(self):
        driver=self.driver
        driver.get(self.get_url)
        driver.maximize_window()
        driver.find_element_by_css_selector('#app > div > form > div:nth-child(2) > div > div > input').send_keys('device')
        driver.find_element_by_css_selector('#app > div > form > div:nth-child(3) > div > div > input').send_keys('abc123')
        driver.find_element_by_css_selector('#app > div > form > button').click()
        sleep(2)
        #切换到设备类型
        driver.get('http://192.168.1.200:8080/web/device2/#/log')
        sleep(3)
        #   设备名称搜索
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div[1]/div/div/div/div[1]/input').send_keys('测试小余03号设备')
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div/button').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div[1]/div/div/div/div[1]/span/span/i').click()
        #序列号
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div[2]/div/div/div/input').send_keys('db38-0614-5054-0061')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div/button').click()
        sleep(2)
        driver.refresh()
        sleep(2)
        #事件类型
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div[3]/div/div/div/div[1]/span/span/i').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[2]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div/button').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div[3]/div/div/div/div[1]/span/span/i').click()
        sleep(2)
        #时间
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div[1]/div/div/div/input').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[2]/button[2]').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/button[2]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div[2]/div/div/div/input').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/button[2]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div/button').click()
        sleep(2)
        driver.refresh()
        sleep(1)
        #开机状态
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div[3]/div/div/div/div[1]/input').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div/button').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div[3]/div/div/div/div[1]/input').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div/button').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div[3]/div/div/div/div[1]/span/span/i').click()
        sleep(2)
        #       拔插卡日志
        driver.get('http://192.168.1.200:8080/web/device2/#/card_log')
        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div[1]/div/div/div/div[1]/input').send_keys('测试小余03号设备')
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div/button').click()#搜索按钮
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div[1]/div/div/div/div[1]/span/span/i').click()
        sleep(1)
        #sn号
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div[2]/div/div/div/input').send_keys('db38-0614-5054-0061')
        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div/button').click()
        sleep(2)
        driver.refresh()
        sleep(1)
        #口类型
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div[3]/div/div/div/div[1]/span/span/i').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div/button').click()#搜索按钮
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div[3]/div/div/div/div[1]/span/span/i').click()
        sleep(1)
        #时间
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div[1]/div/div/div/input').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[2]/button[2]').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/button[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div[2]/div/div/div/input').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/button[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div/button').click()#搜索按钮
        sleep(2)
        driver.refresh()
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div[3]/div/div/div/div[1]/input').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[1]').click()

        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div/button').click()
        sleep(2)


    def tearDown(self):
        self.assertEqual([],self.verificationError)
if __name__=='__main__':
    unittest.main(verbosity=2)

