from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import allure,os
from time import sleep


class ShuJuLuRuPage():
    
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
        self.error_message_box=(By.XPATH,'/html/body/div[2]/div/span/div/div')
        #当前目录
        self.cur_dir = os.path.dirname(os.path.abspath(__file__))
        #上级目录
        self.parent_dir = os.path.dirname(self.cur_dir)
        #显示等待
        self.wait=WebDriverWait(self.driver,10)

    @allure.step("点击手工添加以选择手工添加的方式录入数据")
    def choose_shougongtianjia(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.shougongtianjia_loc))
            self.driver.find_element(*self.shougongtianjia_loc).click()
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/选择手工添加错误.png')
            allure.attach(f'{self.parent_dir}/logs/选择手工添加错误.png',name="选择手工添加错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("在表单中输入姓名")
    def input_name(self,name):
        try:
            self.wait.until(ec.presence_of_element_located(self.form_input_name))
            self.driver.find_element(*self.form_input_name).send_keys(name)
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/输入姓名错误.png')
            allure.attach(f'{self.parent_dir}/logs/输入姓名错误.png',name="输入姓名错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("在表单中选择性别")
    def input_sex(self,sex):
        try:
            self.wait.until(ec.presence_of_element_located(self.form_seletor_sex))
            self.driver.find_element(*self.form_seletor_sex).click()
            sleep(1)
            if sex == "男":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_sex_male))
                self.driver.find_element(*self.form_seletor_sex_male).click()
            elif sex == "女":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_sex_female))
                self.driver.find_element(*self.form_seletor_sex_female).click()
            else:
                raise ValueError("性别输入不能是除男、女外的其他值")
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/选择性别错误.png')
            allure.attach(f'{self.parent_dir}/logs/选择性别错误.png',name="选择性别错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("在表单中选择优先级")
    def input_priority(self,priority):
        try:
            self.wait.until(ec.presence_of_element_located(self.form_seletor_priority))
            self.driver.find_element(*self.form_seletor_priority).click()
            sleep(1)
            if priority == "高":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_priority_high))
                self.driver.find_element(*self.form_seletor_priority_high).click()
            elif priority == "中":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_priority_medium))
                self.driver.find_element(*self.form_seletor_priority_medium).click()
            elif priority == "低":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_priority_low))
                self.driver.find_element(*self.form_seletor_priority_low).click()
            else:
                raise ValueError("优先级输入不能是除高、中、低外的其他值")
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/选择优先级错误.png')
            allure.attach(f'{self.parent_dir}/logs/选择优先级错误.png',name="选择优先级错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("在表单中选择渠道")
    def input_channel(self,channel):
        try:
            self.wait.until(ec.presence_of_element_located(self.form_seletor_channel))
            self.driver.find_element(*self.form_seletor_channel).click()
            sleep(1)
            if channel == "投递简历":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_channel_toudijianli))
                self.driver.find_element(*self.form_seletor_channel_toudijianli).click()
            elif channel == "下载简历":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_channel_xiazaijianli))
                self.driver.find_element(*self.form_seletor_channel_xiazaijianli).click()
            elif channel == "广告":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_channel_guanggao))
                self.driver.find_element(*self.form_seletor_channel_guanggao).click()
            elif channel == "内推":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_channel_neitui))
                self.driver.find_element(*self.form_seletor_channel_neitui).click()
            elif channel == "高校":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_channel_gaoxiao))
                self.driver.find_element(*self.form_seletor_channel_gaoxiao).click()
            elif channel == "招聘会":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_channel_zhaopinhui))
                self.driver.find_element(*self.form_seletor_channel_zhaopinhui).click()
            else:
                raise ValueError("渠道输入不能是除投递简历、下载简历、广告、内推、高校、招聘会外的其他值")
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/选择渠道错误.png')
            allure.attach(f'{self.parent_dir}/logs/选择渠道错误.png',name="选择渠道错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("在表单中选择来源途径")
    def input_source(self,source):
        try:
            self.wait.until(ec.presence_of_element_located(self.form_seletor_source))
            self.driver.find_element(*self.form_seletor_source).click()
            sleep(1)
            if source == "前程无忧":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_source_qianchengwuyou))
                self.driver.find_element(*self.form_seletor_source_qianchengwuyou).click()
            elif source == "智联招聘网":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_source_zhilianzhaopinwang))
                self.driver.find_element(*self.form_seletor_source_zhilianzhaopinwang).click()
            elif source == "拉勾网":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_source_lagouwang))
                self.driver.find_element(*self.form_seletor_source_lagouwang).click()
            else:
                raise ValueError("来源途径输入不能是除前程无忧、智联招聘网、拉勾网外的其他值")
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/选择来源途径错误.png')
            allure.attach(f'{self.parent_dir}/logs/选择来源途径错误.png',name="选择来源途径错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("在表单中选择产品线")
    def input_traintype(self,traintype):
        try:
            self.wait.until(ec.presence_of_element_located(self.form_seletor_traintype))
            self.driver.find_element(*self.form_seletor_traintype).click()
            sleep(1)
            if traintype == "智慧农业管理系统":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_traintype_zhihuinongye))
                self.driver.find_element(*self.form_seletor_traintype_zhihuinongye).click()
            elif traintype == "智慧社区管理系统":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_traintype_zhihuishequ))
                self.driver.find_element(*self.form_seletor_traintype_zhihuishequ).click()
            elif traintype == "智慧停车场":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_traintype_zhihuitingchechang))
                self.driver.find_element(*self.form_seletor_traintype_zhihuitingchechang).click()
            else:
                raise ValueError("产品线输入不能是除智慧农业管理系统、智慧社区管理系统、智慧停车场外的其他值")
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/选择产品线错误.png')
            allure.attach(f'{self.parent_dir}/logs/选择产品线错误.png',name="选择产品线错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("在表单中输入手机号")
    def input_phone(self,phone):
        try:
            self.wait.until(ec.presence_of_element_located(self.form_input_phone))
            self.driver.find_element(*self.form_input_phone).send_keys(phone)
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/输入手机号错误.png')
            allure.attach(f'{self.parent_dir}/logs/输入手机号错误.png',name="输入手机号错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("在表单中选择学历")
    def input_degree(self,degree):
        try:
            self.wait.until(ec.presence_of_element_located(self.form_seletor_degree))
            self.driver.find_element(*self.form_seletor_degree).click()
            sleep(1)
            if degree == "小学":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_degree_xiaoxue))
                self.driver.find_element(*self.form_seletor_degree_xiaoxue).click()
            elif degree == "初中":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_degree_chuzhong))
                self.driver.find_element(*self.form_seletor_degree_chuzhong).click()
            elif degree == "高中":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_degree_gaozhong))
                self.driver.find_element(*self.form_seletor_degree_gaozhong).click()
            elif degree == "大专":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_degree_dazhuan))
                self.driver.find_element(*self.form_seletor_degree_dazhuan).click()
            elif degree == "本科":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_degree_benke))
                self.driver.find_element(*self.form_seletor_degree_benke).click()
            elif degree == "硕士":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_degree_shuoshi))
                self.driver.find_element(*self.form_seletor_degree_shuoshi).click()
            elif degree == "博士":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_degree_boshi))
                self.driver.find_element(*self.form_seletor_degree_boshi).click()
            else:
                raise ValueError("学历输入不能是除小学、初中、高中、大专、本科、硕士、博士外的其他值")
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/选择学历错误.png')
            allure.attach(f'{self.parent_dir}/logs/选择学历错误.png',name="选择学历错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("在表单中输入年龄")
    def input_age(self,age):
        try:
            self.wait.until(ec.presence_of_element_located(self.form_input_age))
            self.driver.find_element(*self.form_input_age).send_keys(age)
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/输入年龄错误.png')
            allure.attach(f'{self.parent_dir}/logs/输入年龄错误.png',name="输入年龄错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("在表单中输入邮箱")
    def input_email(self,email):
        try:
            self.wait.until(ec.presence_of_element_located(self.form_input_email))
            self.driver.find_element(*self.form_input_email).send_keys(email)
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/输入邮箱错误.png')
            allure.attach(f'{self.parent_dir}/logs/输入邮箱错误.png',name="输入邮箱错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("在表单中选择城市")
    def input_city(self,city):
        try:
            self.wait.until(ec.presence_of_element_located(self.form_seletor_city))
            self.driver.find_element(*self.form_seletor_city).click()
            sleep(1)
            if city == "全部":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_city_all))
                self.driver.find_element(*self.form_seletor_city_all).click()
            elif city == "北京":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_city_beijing))
                self.driver.find_element(*self.form_seletor_city_beijing).click()
            elif city == "杭州":
                self.wait.until(ec.presence_of_element_located(self.form_seletor_city_hangzhou))
                self.driver.find_element(*self.form_seletor_city_hangzhou).click()
            else:
                raise ValueError("城市输入不能是除全部、北京、杭州外的其他值")
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/选择城市错误.png')
            allure.attach(f'{self.parent_dir}/logs/选择城市错误.png',name="选择城市错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("点击确定按钮提交表单")
    def submit_form(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.form_button_submit))
            self.driver.find_element(*self.form_button_submit).click()
            sleep(1)
            # try:
            #     self.driver.find_element(*self.error_message_box)
            #     raise SystemError("数据项缺失或数据格式检查未通过")
            # except Exception:
            #     pass
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/提交表单错误.png')
            allure.attach(f'{self.parent_dir}/logs/提交表单错误.png',name="提交表单错误",attachment_type=allure.attachment_type.PNG)
            raise e