from unittest import expectedFailure

from selenium.webdriver.common.by import By



class LoginClass:

    Text_username_Name="username"
    Text_Password_Name="password"
    Click_loginbutton_Xpath="//button[@type='submit']"
    Click_menuButton_Xpath="//p[@class='oxd-userdropdown-name']"
    click_logout_xpath="//a[normalize-space()='Logout']"


    def __init__(self,driver):
        self.driver=driver



    def enter_username(self,username):
        self.driver.find_element(By.NAME,self.Text_username_Name).send_keys(username);


    def enter_password(self,password):
        self.driver.find_element(By.NAME,self.Text_Password_Name).send_keys(password);

    def click_login(self):
        self.driver.find_element(By.XPATH,self.Click_loginbutton_Xpath).click()

    def click_menu(self):
        self.driver.find_element(By.XPATH,self.Click_menuButton_Xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH,self.click_logout_xpath).click()


    def varify_login(self):
        try:
            self.driver.find_element(By.XPATH,self.Click_menuButton_Xpath)
            return "Login Pass"
        except:
            return "Login Fail"






