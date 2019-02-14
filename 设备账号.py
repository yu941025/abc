__author__ = 'Administrator'
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest
class jifan_list(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.get_url='http://192.168.1.200:8080/web/device2/#/login'
        self.driver.implicitly_wait(30)
        self.verificationErrors=[]
        self.accept_next_alert=True#是否继续接受下一下警告
    def test_add_number(self):
        driver=self.driver
        driver.get(self.get_url)
        driver.maximize_window()
        driver.find_element_by_css_selector('#app > div > form > div:nth-child(2) > div > div > input').send_keys('device')
        driver.find_element_by_css_selector('#app > div > form > div:nth-child(3) > div > div > input').send_keys('abc123')
        driver.find_element_by_css_selector('#app > div > form > button').click()
        sleep(2)
        driver.get('http://192.168.1.200:8080/web/device2/#/sip')
        sleep(2)
        #搜索框
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div/div/input').send_keys('19941993')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div/button').click()
        sleep(2)
        driver.refresh()
        sleep(2)
        #添加账号
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[1]/div/button').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[1]/div/div/div/div[1]/input').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div/div/input').send_keys('10011101')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[3]/div/div/div/input').send_keys('shenzhi2018')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[4]/div/div/div/input').send_keys('11')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/span/button[2]').click()
        sleep(2)
        #修改账号
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[13]/div/button[2]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[5]/div/div/div/input').send_keys('12')
        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[7]/div/div/div/textarea').send_keys('测试')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/span/button[2]').click()
        sleep(4)
        #删除
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[13]/div/button[1]').click()
        sleep(3)
        driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/button[2]').click()
        sleep(2)

    def tearDown(self):
        self.assertEqual([],self.verificationErrors)
if __name__=='__main__':
    unittest.main()