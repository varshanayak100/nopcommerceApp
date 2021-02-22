import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


# class name will be Test Case Id
class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("********************test_homePageTitle*********************")
        self.logger.info("********************Verifying Home Page Title*********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.driver.close()
            assert True
            self.logger.info("******************** test_homePageTitle is passed *********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_homePageTitle.png")
            self.driver.close()
            self.logger.error("******************** test_homePageTitle is FAILED *********************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("********************test_login*********************")
        self.logger.info("********************Verifying Test Login title*********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)    # when created an object, the constructor will be invoked
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration" :
            self.driver.close()
            assert True
            self.logger.info("******************** test_login is PASSED *********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_login.png")
            self.driver.close()
            self.logger.error("******************** test_login is FAILED *********************")
            assert False
