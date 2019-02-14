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


    def test_login(self):
            driver=self.driver
            driver.get(self.get_url)
            driver.maximize_window()

            driver.find_element_by_css_selector('#app > div > form > div:nth-child(2) > div > div > input').send_keys('device')
            driver.find_element_by_css_selector('#app > div > form > div:nth-child(3) > div > div > input').send_keys('abc123')
            driver.find_element_by_css_selector('#app > div > form > button').click()
            sleep(2)
            #搜索框
            #设备编号
            driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div:nth-child(1) > div > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input').send_keys('0010302')
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div/button').click()

            sleep(2)
            driver.refresh()
            #设备名称
            driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div:nth-child(1) > div > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input').send_keys('测试小余04号设备')
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div/button').click()
            sleep(2)
            driver.refresh()
            #机房名称
            driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div:nth-child(1) > div > form > div:nth-child(1) > div:nth-child(3) > div > div > div > div.el-input.el-input--medium.el-input--suffix > input').send_keys('测试')

            #driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[1]').click()
            sleep(2)
            ActionChains(driver).click(driver.find_element_by_css_selector('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)')).perform()

            sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div/button').click()
            sleep(2)
            driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div:nth-child(1) > div > form > div:nth-child(1) > div:nth-child(3) > div > div > div > div.el-input.el-input--medium.el-input--suffix > span > span > i').click()
            sleep(2)
            #节点名称
            driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div:nth-child(1) > div > form > div:nth-child(2) > div:nth-child(1) > div > div > div > div.el-input.el-input--medium.el-input--suffix > input').send_keys('sip')
            sleep(1)
            ActionChains(driver).click(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]')).perform()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div/button').click()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div[1]/div/div/div/div[1]/span/span/i').click()
            sleep(2)
            #设备类型
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div[2]/div/div/div/div[1]/input').send_keys('鼎信')
            sleep(1)
            ActionChains(driver).click(driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[4]')).perform()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div/button').click()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div[2]/div/div/div/div[1]/span/span/i').click()
            sleep(2)
            #设备状态
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div[3]/div/div/div/div[1]/span/span/i').click()
            sleep(2)
            driver.find_element_by_css_selector('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()
            sleep(2)
            driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div:nth-child(1) > div > div > div > button').click()
            sleep(2)
            driver.refresh()
            sleep(2)
            #注册状态
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div[4]/div/div/div/div[1]/span/span/i').click()
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[1]').click()
            sleep(2)
            driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div:nth-child(1) > div > div > div > button').click()
            sleep(2)
            driver.refresh()
            #在线状态
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div[5]/div/div/div/div[1]/span/span/i').click()
            sleep(2)
            driver.find_element_by_css_selector('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()
            sleep(2)
            driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div:nth-child(1) > div > div > div > button').click()
            sleep(2)
            driver.refresh()
            sleep(2)

            #选择地域
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div[6]/div/div/span/span').click()
            sleep(2)
            driver.find_element_by_class_name('el-cascader-menu').find_element_by_xpath('li[1]').click()
            sleep(2)
            driver.find_elements_by_class_name('el-cascader-menu')[1].find_element_by_xpath('li[1]').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div/button').click()
            sleep(2)
            driver.refresh()
            #设备sn
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[3]/div/div/input').send_keys('DB27-4200-0440-0002')
            sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/div/button').click()
            sleep(1)
            driver.refresh()
            sleep(2)
            #编辑设备
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[21]/div/div/button[1]').click()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[11]/div/div/div/textarea').send_keys('测试')
            sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[12]/div/button[2]').click()
            sleep(3)

            #暂停

            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[21]/div/div/button[2]').click()
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[21]/div/div/button[2]').click()
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
            #停用
            sleep(2)

            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[21]/div/div/button[3]').click()
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[21]/div/div/button[2]').click()
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
            #锁定
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[21]/div/div/button[4]').click()
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[21]/div/div/button[3]').click()
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()

    def test_tongdao(self):
            driver=self.driver
            driver.get(self.get_url)
            driver.maximize_window()

            driver.find_element_by_css_selector('#app > div > form > div:nth-child(2) > div > div > input').send_keys('device')
            driver.find_element_by_css_selector('#app > div > form > div:nth-child(3) > div > div > input').send_keys('abc123')
            driver.find_element_by_css_selector('#app > div > form > button').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[21]/div/div/button[6]').click()
            sleep(2)
            #批量修改
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/button[2]').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div/div/div/div/div[1]/input').click()
            sleep(1)
            driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/span/button[2]').click()
            #导出
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/button[1]').click()
            sleep(2)
            #修改
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div/div[3]/table/tbody/tr/td[10]/div/button[1]').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/form/div/div/div/div/div[1]/input').click()
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[3]/span/button[2]').click()
            #暂停
            for  i in range(2):
                driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div/div[3]/table/tbody/tr/td[10]/div/button[2]').click()
                sleep(2)
                driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
                sleep(2)
            #停用
            for j in range(2):
                driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div/div[3]/table/tbody/tr/td[10]/div/button[3]').click()
                sleep(2)
                driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
                sleep(2)
            #锁定
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[21]/div/div/button[4]').click()
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[21]/div/div/button[3]').click()
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
            sleep(2)
            #端口信息查询
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div/div/div[3]/table/tbody/tr/td[10]/div/button[5]').click()




    def tearDown(self):
            self.assertEqual([],self.verificationError)


if __name__=='__main__':
    unittest.main()