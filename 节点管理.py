__author__ = 'Administrator'
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest
class addNode(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.get_url='http://192.168.1.200:8080/web/device2/#/login'
        self.driver.implicitly_wait(30)
        self.verificationErrors=[]

    def test_addNode(self):
        driver=self.driver
        driver.get(self.get_url)
        driver.maximize_window()
        #登录设备管理系统
        driver.find_element_by_css_selector('#app > div > form > div:nth-child(2) > div > div > input').send_keys('device')
        driver.find_element_by_css_selector('#app > div > form > div:nth-child(3) > div > div > input').send_keys('abc123')
        driver.find_element_by_css_selector('#app > div > form > button').click()
        sleep(2)
        #切换到节点管理添加节点
        driver.get('http://192.168.1.200:8080/web/device2/#/call_node')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div/div/input').send_keys('测试鱼123')
        sleep(2)
        driver.refresh()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div/div/input').send_keys('192.168.1.200')
        sleep(1)
        driver.refresh()
        sleep(2)
        driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div:nth-child(2) > div > div:nth-child(1) > div > button').click()
        sleep(2)
        driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(1) > div > div > div > div.el-input.el-input--medium.el-input--suffix > input').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[7]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/form/div[2]/div/div/span/span').click()
        sleep(2)
        driver.find_element_by_class_name('el-cascader-menu').find_element_by_xpath('li[1]').click()
        sleep(2)
        driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(3) > div > div > div > div.el-input.el-input--medium.el-input--suffix > input').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/form/div[4]/div/div[1]/div/input').send_keys('测试20181116')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/form/div[5]/div/div/div/input').send_keys('192.168.1.2')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/form/div[6]/div/div/div/input').send_keys('5060')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[3]/span/button[2]').click()
        sleep(8)
        #修改节点
        #修改节点
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[16]/div/button[1]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/form/div[7]/div/div/div/textarea').send_keys('测试设备')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[3]/span/button[2]').click()
        sleep(3)
        #禁用启用节点
        for i in range(2):
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[16]/div/button[2]').click()
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
            sleep(2)



    def tearDown(self):
        self.assertEqual([],self.verificationErrors)




if __name__=='__main__':
    unittest.main()