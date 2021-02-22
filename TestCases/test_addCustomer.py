from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

import string
import random
import pytest

class Test_003_AddCustomer:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("********************Test_003_AddCustomer*********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)  # when created an object, the constructor will be invoked
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********************Login Successful*********************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.click_CustomerLink()
        self.addcust.clickCustomersLink()
        self.addcust.clickAddNew()

        self.logger.info("********************Providing Cutomer INfo*********************")

        self.email = random_generator() + "@gmail.com"
        self.addcust.enterEmail(self.email)
        self.addcust.enterPassword("test123")
        self.addcust.enterFirstName("Test1")
        self.addcust.enterLastName("Last1")
        self.addcust.selectGender("Male")
        self.addcust.enterDOB("07/03/1992")
        self.addcust.enterCompanyID("company123")
        self.addcust.selectIsTaxExtempt()
        self.addcust.selectNewLetter()
        self.addcust.selectCustomerRoles()
        self.addcust.selectManagerOfVendor()
        self.addcust.enterAdminComment("Testing")
        self.addcust.clickOnSave()

        self.logger.info("********************Entered all the customer INfo*********************")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)

        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("*************Added the customer successfully*************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_addCust.png")
            self.logger.error("**************Add Customer Test failed***************")
            assert True == False

        self.driver.close()
        self.logger.info("Ending Add Customer TestCase")



def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

