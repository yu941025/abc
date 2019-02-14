__author__ = 'Administrator'
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import unittest
#登录
class login(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.get_url='http://192.168.1.200:8080/web/device2/#/login'
        self.driver.implicitly_wait(30)#设置等待超时时间
        self.verificationErrors = [] #脚本运行时，错误的信息将被打印到这个列表中。


    def test_add_sheb(self):
            driver=self.driver
            driver.get(self.get_url)
            driver.maximize_window()
            driver.get('http://192.168.1.200:8080/web/device2/#/sip')
            sleep(2)
            #添加账号
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[1]/div/button').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[1]/div/div/div/div[1]/input').click()
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div/div/input').send_keys('123321123')
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[3]/div/div/div/input').send_keys('shenzhi2018')
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[4]/div/div/div/input').send_keys('11')
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/span/button[2]').click()
            sleep(2)
            #添加设备
            driver.get('http://192.168.1.200:8080/web/device2/#/dashboard')
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[1]/div/button[1]').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[1]/div/div/div/div[1]/input').click()
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[3]').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[2]/div/div/span/span').click()
            sleep(2)
            driver.find_element_by_class_name('el-cascader-menu').find_element_by_xpath('li[1]').click()
            sleep(2)
            driver.find_elements_by_class_name('el-cascader-menu')[1].find_element_by_xpath('li[1]').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[3]/div/div/div/div[1]/input').click()
            sleep(2)
            driver.find_element_by_class_name('resize-triggers').find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/button[2]').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[5]/div/div/div/div[1]/input').send_keys('1')
            sleep(1)
            driver.find_element_by_class_name('resize-triggers').find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[1]').click()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[6]/div/div/div/div[1]/input').click()
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/ul/li[1]').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[7]/div/div[1]/div/input').send_keys('234')
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[12]/div/div[1]/div/textarea').send_keys('测试')
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[13]/div/button[2]').click()



    def tearDown(self):
            self.assertEqual([],self.verificationErrors)


if __name__=='__main__':
    unittest.main()