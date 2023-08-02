from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import allure,os
from time import sleep


class shujuluru_page():
    
    def __init__(self,driver:webdriver.Chrome) -> None:
        self.driver=driver
        #页面元素
        self.shougongtianjia_loc=(By.XPATH,'//*[@id="root"]/section/section/main/div/div[2]/div/div[1]/div[1]')
        self.form_input_name=(By.XPATH,'//*[@id="name"]')
        self.form_seletor_sex=(By.XPATH,'//*[@id="sex"]')
        self.form_seletor_sex_male=(By.XPATH,'//li[text()="男"]')
        self.form_seletor_sex_female=(By.XPATH,'//li[text()="女"]')
        self.form_seletor_priority=(By.XPATH,'//*[@id="priority"]')
        self.form_seletor_priority_high=(By.XPATH,'//li[text()="高"]')
        self.form_seletor_priority_medium=(By.XPATH,'//li[text()="中"]')
        self.form_seletor_priority_low=(By.XPATH,'//li[text()="低"]')
        self.form_seletor_channel=(By.XPATH,'//*[@id="channelId"]')
        self.form_seletor_channel_toudijianli=(By.XPATH,'//li[text()="投递简历"]')
        self.form_seletor_channel_xiazaijianli=(By.XPATH,'//li[text()="下载简历"]')
        self.form_seletor_channel_guanggao=(By.XPATH,'//li[text()="广告"]')
        self.form_seletor_channel_neitui=(By.XPATH,'//li[text()="内推"]')
        self.form_seletor_channel_gaoxiao=(By.XPATH,'//li[text()="高校"]')
        self.form_seletor_channel_zhaopinhui=(By.XPATH,'//li[text()="招聘会"]')
        self.form_seletor_source=(By.XPATH,'//*[@id="sourceId"]')
        self.form_seletor_source_qianchengwuyou=(By.XPATH,'//li[text()="前程无忧"]')
        self.form_seletor_source_zhilianzhaopinwang=(By.XPATH,'//li[text()="智联招聘网"]')
        self.form_seletor_source_lagouwang=(By.XPATH,'//li[text()="拉勾网"]')
        self.form_seletor_traintype=(By.XPATH,'//*[@id="trainType"]')
        self.form_seletor_traintype_zhihuinongye=(By.XPATH,'//li[text()="智慧农业管理系统"]')
        self.form_seletor_traintype_zhihuishequ=(By.XPATH,'//li[text()="智慧社区管理系统"]')
        self.form_seletor_traintype_zhihuitingchechang=(By.XPATH,'//li[text()="智慧停车场"]')
        self.form_input_phone=(By.XPATH,'//*[@id="phone"]')
        self.form_seletor_degree=(By.XPATH,'//*[@id="degree"]')
        self.form_seletor_degree_xiaoxue=(By.XPATH,'//li[text()="小学"]')
        self.form_seletor_degree_chuzhong=(By.XPATH,'//li[text()="初中"]')
        self.form_seletor_degree_gaozhong=(By.XPATH,'//li[text()="高中"]')
        self.form_seletor_degree_dazhuan=(By.XPATH,'//li[text()="大专"]')
        self.form_seletor_degree_benke=(By.XPATH,'//li[text()="本科"]')
        self.form_seletor_degree_shuoshi=(By.XPATH,'//li[text()="硕士"]')
        self.form_seletor_degree_boshi=(By.XPATH,'//li[text()="博士"]')
        self.form_input_age=(By.XPATH,'//*[@id="age"]')
        self.form_input_email=(By.XPATH,'//*[@id="email"]')
        self.form_seletor_city=(By.XPATH,'//*[@id="root"]/section/section/main/div/div[1]/div/div[1]/div/div')
        self.form_seletor_city_all=(By.XPATH,'//li[text()="全部"]')
        self.form_seletor_city_beijing=(By.XPATH,'//li[text()="北京"]')
        self.form_seletor_city_hangzhou=(By.XPATH,'//li[text()="杭州"]')
        self.form_button_submit=(By.XPATH,'//*[@id="root"]/section/section/main/div/div[2]/div/div[2]/button')
        #当前目录
        self.cur_dir = os.path.dirname(os.path.abspath(__file__))
        #上级目录
        self.parent_dir = os.path.dirname(self.cur_dir)
        #显示等待
        self.wait=WebDriverWait(self.driver,10)