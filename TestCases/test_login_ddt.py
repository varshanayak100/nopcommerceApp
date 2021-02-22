import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


# class name will be Test Case Id
class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData//LoginData.xlsx"
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("********************test_login_ddt*********************")
        self.logger.info("********************Verifying Test Login title*********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)    # when created an object, the constructor will be invoked

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        self.logger.info("Number of rows in the excel " + str(self.rows))
        lst_status=[]  # Empty List Variable
        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.logger.info(self.user)
            self.logger.info(self.password)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            if act_title == "Dashboard / nopCommerce administration" :
                if self.exp=="Pass":
                    self.logger.info("******************** test_login is PASSED *********************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("******************** test_login is FAILED *********************")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != "Dashboard / nopCommerce administration" :
                if self.exp=="Pass":
                    self.logger.info("******************** test_login is FAILED *********************")
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("******************** test_login is PASSED *********************")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Login DDT Test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT Test Failed")
            self.driver.close()
            assert False

        self.logger.info("******************** End of Test_002_DDT_Login *********************")
