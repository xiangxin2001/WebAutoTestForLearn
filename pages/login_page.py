from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import allure,os


class LoginPage():
    
    def __init__(self,driver:webdriver.Chrome) -> None:
        self.driver=driver
        #页面元素
        self.username_input_loc=(By.XPATH,'//*[@id="account"]/input')
        self.userpwd_input_loc=(By.XPATH,'//*[@id="password"]/input')
        self.valcode_input_loc=(By.XPATH,'//*[@id="authCode"]/div/input')
        self.login_button_loc=(By.XPATH,'//*[@id="root"]/div/div[1]/form/div[5]/div/div/span/button')
        self.valcode_img_loc=(By.XPATH,'//*[@id="authCode"]/img')
        self.pwd_forget_page_a_loc=(By.XPATH,'//*[@id="root"]/div/div[1]/form/div[4]/div/div/span/a')
        self.pwd_remember_checkbox_loc=(By.XPATH,'//*[@id="root"]/div/div[1]/form/div[4]/div/div/span/label/span[1]/input')
        #当前目录
        self.cur_dir = os.path.dirname(os.path.abspath(__file__))
        #上级目录
        self.parent_dir = os.path.dirname(self.cur_dir)
        #显示等待
        self.wait=WebDriverWait(self.driver,10)

    @allure.step("输入用户名")
    def input_username(self,username):
        try:
            self.wait.until(ec.presence_of_element_located(self.username_input_loc))
            self.driver.find_element(*self.username_input_loc).clear()
            self.driver.find_element(*self.username_input_loc).send_keys(username)
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/用户名输入错误.png')
            allure.attach(f'{self.parent_dir}/logs/用户名输入错误.png',name="用户名输入错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("输入密码")
    def input_userpwd(self,userpwd):
        try:
            self.wait.until(ec.presence_of_element_located(self.userpwd_input_loc))
            self.driver.find_element(*self.userpwd_input_loc).clear()
            self.driver.find_element(*self.userpwd_input_loc).send_keys(userpwd)
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/密码输入错误.png')
            allure.attach(f'{self.parent_dir}/logs/密码输入错误.png',name="密码输入错误",attachment_type=allure.attachment_type.PNG)
            raise e

    @allure.step("输入验证码")
    def input_valcode(self,valcode):
        try:
            self.wait.until(ec.presence_of_element_located(self.valcode_input_loc))
            self.driver.find_element(*self.valcode_input_loc).clear()
            self.driver.find_element(*self.valcode_input_loc).send_keys(valcode)
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/验证码输入错误.png')
            allure.attach(f'{self.parent_dir}/logs/验证码输入错误.png',name="验证码输入错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("点击登录按钮")
    def click_login_button(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.login_button_loc))
            self.driver.find_element(*self.login_button_loc).click()
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/点击登录按钮错误.png')
            allure.attach(f'{self.parent_dir}/logs/点击登录按钮错误.png',name="点击登录按钮错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("点击验证码图片")
    def click_valcode_img(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.valcode_img_loc))
            self.driver.find_element(*self.valcode_img_loc).click()
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/点击验证码图片错误.png')
            allure.attach(f'{self.parent_dir}/logs/点击验证码图片错误.png',name="点击验证码图片错误",attachment_type=allure.attachment_type.PNG)
            raise e

    @allure.step("点击忘记密码")
    def click_pwd_forget_page_link(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.pwd_forget_page_a_loc))
            self.driver.find_element(*self.pwd_forget_page_a_loc).click()
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/点击忘记密码错误.png')
            allure.attach(f'{self.parent_dir}/logs/点击忘记密码错误.png',name="点击忘记密码错误",attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("勾选记住密码")
    def check_pwd_remember_checkbox(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.pwd_remember_checkbox_loc))
            self.driver.find_element(*self.pwd_remember_checkbox_loc).click()
        except Exception as e:
            self.driver.save_screenshot(f'{self.parent_dir}/logs/勾选记住密码错误.png')
            allure.attach(f'{self.parent_dir}/logs/勾选记住密码错误.png',name="勾选记住密码错误",attachment_type=allure.attachment_type.PNG)
            raise e