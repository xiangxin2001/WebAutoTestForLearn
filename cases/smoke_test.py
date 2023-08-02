import pytest,allure,os
from selenium import webdriver
from time import sleep
from utils.tools import read_csv
from pages.login_page import LoginPage
from pages.main_page import MainPage
#当前目录
cur_dir = os.path.dirname(os.path.abspath(__file__))
#上级目录
parent_dir = os.path.dirname(cur_dir)
@allure.epic("Web自动化测试")
@allure.feature("冒烟测试")
class TestSmoke():
    
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver=webdriver.Chrome(options=options)
        self.driver.maximize_window()
        

    def teardown(self):
        self.driver.quit()

    @allure.title("主流程冒烟测试")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('data',read_csv(url=f"{parent_dir}/data/users.csv"))
    @allure.severity(allure.severity_level.BLOCKER)
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
        main_page.logout()
        sleep(1)
        actual = self.driver.current_url
        excepted="http://192.168.15.129/cloud/#/open/login"
        assert excepted == actual #成功退出登录，返回登录页


if __name__=="__main__":
    import sys
    sys.path.append(os.getcwd())
    pytest.main()