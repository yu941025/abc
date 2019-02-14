__author__ = 'Administrator'
from selenium import webdriver
from time import sleep
import unittest
class jifan(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.get_url='http://192.168.1.200:8080/web/device2'
        self.driver.implicitly_wait(30)
        self.verificationError=[]
    def test_jifan(self):
        #登录设备管理系统
        driver=self.driver
        driver.get(self.get_url)
        driver.maximize_window()
        driver.find_element_by_css_selector('#app > div > form > div:nth-child(2) > div > div > input').send_keys('device')
        driver.find_element_by_css_selector('#app > div > form > div:nth-child(3) > div > div > input').send_keys('abc123')
        driver.find_element_by_css_selector('#app > div > form > button').click()
        sleep(2)
        #切换到机房列表
        driver.get('http://192.168.1.200:8080/web/device2/#/server')
        sleep(1)
        #搜索框
        '''driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div/div/input').send_keys('鱼')
        sleep(2)
        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div/button').click()
        sleep(2)
        driver.refresh()
        sleep(1)
        #导出
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[1]/div/button[2]').click()
        sleep(2)
        #添加机房
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[1]/div/button[1]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[1]/div/div/div/div[1]/input').send_keys('sip')
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[3]/div/div[1]/div/input').send_keys('测试上线二')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[6]/div/div[1]/div/input').send_keys('与测试')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[7]/div/div/div/input').send_keys('13738736581')
        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[9]/div/div/span/span').click()
        sleep(2)
        driver.find_element_by_class_name('el-cascader-menu').find_element_by_xpath('li[1]').click()
        sleep(2)
        driver.find_elements_by_class_name('el-cascader-menu')[1].find_element_by_xpath('li[1]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/span/button[2]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[21]/div/button[3]').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/button[2]').click()'''

        sleep(3)
        '''#更新测速
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[21]/div/button[1]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/form/div[1]/div/div/div/span[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/form/div[2]/div/div/div/span[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/form/div[3]/div/div/div/input').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/button[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[3]/span/button[2]').click()'''
        #暂停
        for i in range(2):
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[21]/div/button[3]').click()
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
            sleep(2)
        #停用
        for i in range(2):
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[21]/div/button[3]').click()
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
            sleep(2)

        #编辑
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[21]/div/button[2]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[11]/div/div/div/textarea').send_keys('测试')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/span/button[2]').click()

    def tearDown(self):
        self.assertEqual([],self.verificationError)
if __name__=='__main__':
    unittest.main(verbosity=2)