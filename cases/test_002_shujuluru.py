import pytest,allure,os
import sys
sys.path.append(os.getcwd())
from selenium import webdriver
from time import sleep
from utils.tools import read_csv
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.shujuluru_page import ShuJuLuRuPage
#当前目录
cur_dir = os.path.dirname(os.path.abspath(__file__))
#上级目录
parent_dir = os.path.dirname(cur_dir)
@allure.epic("Web自动化测试")
@allure.feature("功能测试")
class TestShuJuLuRu():
    
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver=webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.candidates=read_csv(url=f"{parent_dir}/data/candidates.csv")

    def teardown(self):
        self.driver.quit()

    @allure.title("不同角色的数据录入功能测试")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('data',read_csv(url=f"{parent_dir}/data/users.csv"))
    @allure.severity(allure.severity_level.CRITICAL)
    def test_smoke(self,data):
        self.driver.get("http://192.168.15.129/cloud/#/open/login")
        login=LoginPage(driver=self.driver)
        login.input_username(username=data[0])
        sleep(1)
        login.input_userpwd(userpwd=data[1])
        sleep(1)
        login.input_valcode(valcode="8888")
        sleep(1)
        login.check_pwd_remember_checkbox()
        sleep(1)
        login.click_login_button()
        sleep(2)
        actual = self.driver.current_url  
        expected = "http://192.168.15.129/cloud/#/my" 
        assert expected == actual  #成功登录，进入欢迎页
        main_page=MainPage(driver=self.driver)
        shujuluru_page=ShuJuLuRuPage(driver=self.driver)
        for candidate in self.candidates:
            main_page.goto_shujuluru_page()
            sleep(2)
            shujuluru_page.choose_shougongtianjia()
            shujuluru_page.input_name(name=candidate[0])
            shujuluru_page.input_sex(sex=candidate[1])
            shujuluru_page.input_priority(priority=candidate[2])
            shujuluru_page.input_channel(channel=candidate[3])
            shujuluru_page.input_source(source=candidate[4])
            shujuluru_page.input_traintype(traintype=candidate[5])
            shujuluru_page.input_phone(phone=candidate[6])
            shujuluru_page.input_degree(degree=candidate[7])
            shujuluru_page.input_age(age=candidate[8])
            shujuluru_page.input_email(email=candidate[9])
            if data[2] != "人事经理" and data[2] != "人事专员":
                shujuluru_page.input_city(city=candidate[10])
            shujuluru_page.submit_form()
            main_page.goto_welcome_page()
        main_page.logout()
        sleep(1)
        actual = self.driver.current_url
        excepted="http://192.168.15.129/cloud/#/open/login"
        assert excepted == actual #成功退出登录，返回登录页


if __name__=="__main__":
    pytest.main()