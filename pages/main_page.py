from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import allure,os
from time import sleep


class MainPage():
    
    def __init__(self,driver:webdriver.Chrome) -> None:
        self.driver=driver
        #页面元素
        self.logo_loc=(By.XPATH,'//*[@id="root"]/section/aside/div/a/div')
        self.head_icon_span_loc=(By.XPATH,'//*[@id="root"]/section/section/header/div/div[2]/span/span[1]')
        self.logout_li_loc=(By.XPATH,'//li[text()="退出登录"]')
        self.menu_zhaopinguanli_loc=(By.XPATH,'//*[@id="root"]/section/aside/div/ul/li[1]/div')
        self.menu_zhaopinguanli_zhaopingenzong_loc=(By.XPATH,'//*[@id="sale$Menu"]/li[1]/div')
        self.menu_zhaopinguanli_zhaopingenzong_custom_loc=(By.XPATH,'//*[@id="saleRecruitManage$Menu"]/li[1]')
        self.menu_zhaopinguanli_zhaopingenzong_ad_loc=(By.XPATH,'//*[@id="saleRecruitManage$Menu"]/li[2]')
        self.menu_zhaopinguanli_ziyuanfenpei_loc=(By.XPATH,'//*[@id="sale$Menu"]/li[2]/div')
        self.menu_zhaopinguanli_ziyuanfenpei_custom_loc=(By.XPATH,'//*[@id="recruitDistribute$Menu"]/li[1]')
        self.menu_zhaopinguanli_ziyuanfenpei_ad_loc=(By.XPATH,'//*[@id="recruitDistribute$Menu"]/li[2]')
        self.menu_zhaopinguanli_ziyuanguanli_loc=(By.XPATH,'//*[@id="sale$Menu"]/li[3]/div')
        self.menu_zhaopinguanli_ziyuanguanli_custom_loc=(By.XPATH,'//*[@id="resume$Menu"]/li[1]')
        self.menu_zhaopinguanli_ziyuanguanli_ad_loc=(By.XPATH,'//*[@id="resume$Menu"]/li[2]')
        self.menu_zhaopinguanli_biangengrenshizhuanyuan_loc=(By.XPATH,'//*[@id="sale$Menu"]/li[4]')
        self.menu_zhaopinguanli_shujuluru_loc=(By.XPATH,'//*[@id="sale$Menu"]/li[5]')
        self.menu_zhaopinguanli_ziyuanchaxun_loc=(By.XPATH,'//*[@id="sale$Menu"]/li[6]')
        self.menu_dangqianrenwu_loc=(By.XPATH,'//*[@id="root"]/section/aside/div/ul/li[2]/div')
        self.menu_dangqianrenwu_huifangziyuan_loc=(By.XPATH,'//*[@id="today$Menu"]/li[1]')
        self.menu_dangqianrenwu_xinziyuan_loc=(By.XPATH,'//*[@id="today$Menu"]/li[2]')

        #当前目录
        self.cur_dir = os.path.dirname(os.path.abspath(__file__))
        #上级目录
        self.parent_dir = os.path.dirname(self.cur_dir)
        #显示等待
        self.wait=WebDriverWait(self.driver,10)

    @allure.step("点击logo进入欢迎页面")
    def goto_shujuluru_page(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.logo_loc))
            self.driver.find_element(*self.logo_loc).click()
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/进入欢迎页面错误.png')
            allure.attach(f'{self.parent_dir}/logs/进入欢迎页面错误.png',name="进入欢迎页面错误",attachment_type=allure.attachment_type.PNG)
            raise e    

    @allure.step("点击退出登录按钮")
    def logout(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.head_icon_span_loc))
            ActionChains(self.driver).move_to_element(self.driver.find_element(*self.head_icon_span_loc)).perform()
            sleep(1)
            self.wait.until(ec.presence_of_element_located(self.logout_li_loc))
            self.driver.find_element(*self.logout_li_loc).click()
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/退出登录错误.png')
            allure.attach(f'{self.parent_dir}/logs/退出登录错误.png',name="退出登录错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("点击招聘管理/数据录入进入数据录入页面")
    def goto_shujuluru_page(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_loc).click()
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_shujuluru_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_shujuluru_loc).click()
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/进入数据录入页面错误.png')
            allure.attach(f'{self.parent_dir}/logs/进入数据录入页面错误.png',name="进入数据录入页面错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("点击招聘管理/招聘跟踪/传统简历跟踪进入传统简历跟踪页面")
    def goto_chuantongjianli_genzong_page(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_loc).click()
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_zhaopingenzong_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_zhaopingenzong_loc).click()
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_zhaopingenzong_custom_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_zhaopingenzong_custom_loc).click()
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/进入传统简历跟踪页面错误.png')
            allure.attach(f'{self.parent_dir}/logs/进入传统简历跟踪页面错误.png',name="进入传统简历跟踪页面错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("点击招聘管理/资源分配/传统简历分配进入传统简历分配页面")
    def goto_chuantongjianli_fenpei_page(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_loc).click()
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_ziyuanfenpei_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_ziyuanfenpei_loc).click()
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_ziyuanfenpei_custom_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_ziyuanfenpei_custom_loc).click()
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/进入传统简历分配页面错误.png')
            allure.attach(f'{self.parent_dir}/logs/进入传统简历分配页面错误.png',name="进入传统简历分配页面错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("点击招聘管理/资源管理/传统简历管理进入传统简历管理页面")
    def goto_chuantongjianli_guanli_page(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_loc).click()
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_ziyuanguanli_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_ziyuanguanli_loc).click()
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_ziyuanguanli_custom_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_ziyuanguanli_custom_loc).click()
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/进入传统简历管理页面错误.png')
            allure.attach(f'{self.parent_dir}/logs/进入传统简历管理页面错误.png',name="进入传统简历管理页面错误",attachment_type=allure.attachment_type.PNG)
            raise e

    @allure.step("点击招聘管理/招聘跟踪/广告简历跟踪进入广告简历跟踪页面")
    def goto_guanggaojianli_genzong_page(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_loc).click()
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_zhaopingenzong_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_zhaopingenzong_loc).click()
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_zhaopingenzong_ad_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_zhaopingenzong_ad_loc).click()
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/进入广告简历跟踪页面错误.png')
            allure.attach(f'{self.parent_dir}/logs/进入广告简历跟踪页面错误.png',name="进入广告简历跟踪页面错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("点击招聘管理/资源分配/广告简历分配进入广告简历分配页面")
    def goto_guanggaojianli_fenpei_page(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_loc).click()
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_ziyuanfenpei_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_ziyuanfenpei_loc).click()
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_ziyuanfenpei_ad_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_ziyuanfenpei_ad_loc).click()
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/进入广告简历分配页面错误.png')
            allure.attach(f'{self.parent_dir}/logs/进入广告简历分配页面错误.png',name="进入广告简历分配页面错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("点击招聘管理/资源管理/广告简历管理进入广告简历管理页面")
    def goto_guanggaojianli_guanli_page(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_loc).click()
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_ziyuanguanli_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_ziyuanguanli_loc).click()
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_ziyuanguanli_ad_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_ziyuanguanli_ad_loc).click()
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/进入广告简历管理页面错误.png')
            allure.attach(f'{self.parent_dir}/logs/进入广告简历管理页面错误.png',name="进入广告简历管理页面错误",attachment_type=allure.attachment_type.PNG)
            raise e

    @allure.step("点击招聘管理/变更人事专员列表进入变更人事专员列表页面")
    def goto_biangengrenshizhuanyuan_page(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_loc).click()
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_biangengrenshizhuanyuan_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_biangengrenshizhuanyuan_loc).click()
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/进入变更人事专员列表页面错误.png')
            allure.attach(f'{self.parent_dir}/logs/进入变更人事专员列表页面错误.png',name="进入变更人事专员列表页面错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("点击招聘管理/资源查询进入资源查询页面")
    def goto_ziyuanchaxun_page(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_loc).click()
            self.wait.until(ec.presence_of_element_located(self.menu_zhaopinguanli_ziyuanchaxun_loc))
            self.driver.find_element(*self.menu_zhaopinguanli_ziyuanchaxun_loc).click()
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/进入资源查询页面错误.png')
            allure.attach(f'{self.parent_dir}/logs/进入资源查询页面错误.png',name="进入资源查询页面错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("点击当前任务/回访资源进入回访资源页面")
    def goto_huifangziyuan_page(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.menu_dangqianrenwu_loc))
            self.driver.find_element(*self.menu_dangqianrenwu_loc).click()
            self.wait.until(ec.presence_of_element_located(self.menu_dangqianrenwu_huifangziyuan_loc))
            self.driver.find_element(*self.menu_dangqianrenwu_huifangziyuan_loc).click()
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/进入回访资源页面错误.png')
            allure.attach(f'{self.parent_dir}/logs/进入回访资源页面错误.png',name="进入回访资源页面错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("点击当前任务/新资源进入新资源页面")
    def goto_xinziyuan_page(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.menu_dangqianrenwu_loc))
            self.driver.find_element(*self.menu_dangqianrenwu_loc).click()
            self.wait.until(ec.presence_of_element_located(self.menu_dangqianrenwu_xinziyuan_loc))
            self.driver.find_element(*self.menu_dangqianrenwu_xinziyuan_loc).click()
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/进入新资源页面错误.png')
            allure.attach(f'{self.parent_dir}/logs/进入新资源页面错误.png',name="进入新资源页面错误",attachment_type=allure.attachment_type.PNG)
            raise e