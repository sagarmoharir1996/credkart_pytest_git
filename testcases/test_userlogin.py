import time

import allure
import pytest
from allure_commons.types import AttachmentType

from pageobject.Loginpage import LoginClass
from utilities.config import Readconfig
from utilities.logger import LoggenClass


@pytest.mark.usefixtures("setup")
class Test_Userlogin:
    username=Readconfig.getuseremail()
    userpassword=Readconfig.getpasword()
    log=LoggenClass.logen()


    @allure.feature("Testing Url")
    @allure.title("verify the Url")
    @allure.tag("ABC112")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link("https://www.example.com")
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",link_type="orange Hrm login websit",name="orangehrm")
    @allure.story("valid credentials")
    @allure.description("mytest descrobetion")

    def test_verify_url(self,setup):
        self.driver=setup
        self.log.info("testing started")
        Page_titles=self.driver.title
        print(Page_titles)
        self.log.info("Checking url")

        if Page_titles == "OrangeHRM":
            self.log.info("Url correct")
            self.driver.save_screenshot("..\\Screenshots\\test_verify_url.png");
            allure.attach(self.driver.get_screenshot_as_png(),name=" URl test verify test pass")

            assert True
        else:
            self.log.info("Url incorrect")
            self.driver.save_screenshot("..\\Screenshots\\test_verify_url.png");
            allure.attach(self.driver.get_screenshot_as_png(),name=" URl test verify test Fail")


            assert False



    def test_userlogin_001(self,setup):
        self.driver=setup
        self.lp=LoginClass(self.driver)
        self.log.info("user login testing start")

        self.lp.enter_username(self.username)
        self.log.info("Enter username")
        self.lp.enter_password(self.userpassword)
        self.log.info("enter password")
        self.lp.click_login()
        self.log.info("click on login")
        time.sleep(5)
        # print(self.lp.varify_login())

        self.lp.click_menu()
        if self.lp.varify_login()=="Login Pass":
            self.log.info("Login pass")
            self.driver.save_screenshot("..\\Screenshots\\test_userlogin_001.png");
            allure.attach(self.driver.get_screenshot_as_png(),name="login verify test pass")
            assert True
        else:
            self.log.info("Login Fail")
            self.driver.save_screenshot("..\\Screenshots\\test_userlogin_001.png");
            allure.attach(self.driver.get_screenshot_as_png(),name=" login verify test fail")

            assert False


        self.lp.click_logout()
        self.log.info("user logout")
        self.log.info("test complete")
