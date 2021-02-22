from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

class AddCustomer:

    linkCustomer_link_path = "//a[@href='#']//span[text()='Customers']"
    linkCustomer_link_path1 = "//a[contains(@href,'Admin')]//span[text()='Customers']"
    linkAddNew_path = "//a[contains(@href,'Create')]"
    textbox_email = "//input[@id='Email']"
    textbox_password = "//input[@id='Password']"
    textbox_FirstName = "//input[@id='FirstName']"
    textbox_LastName = "//input[@id='LastName']"
    radio_GenderMale = "//input[@id='Gender_Male']"
    radio_GenderFemale = "//input[@id='Gender_Female']"
    textbox_dateOfBirth_Id = "//input[@id='DateOfBirth']"
    textbox_company_id = "//input[@id='Company']"
    checkbox_IsTaxExtempt_id = "//input[@id='IsTaxExempt']"
    NewsLetter_xpath = "//div[@role='listbox']"
    newsLetter_YourStoreName_xpath = "//li[text()='Your store name']"
    xpath_Customer_Roles = '(//div[@class="k-multiselect-wrap k-floatwrap"])[2]'
    xpath_ForumModerators = "//li[text()='Forum Moderators']"
    select_Manager_Of_Vendor = "//select[@id='VendorId']"
    textArea_AdminComment = "//textarea[@id='AdminComment']"
    button_save = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def click_CustomerLink(self):
        #time.sleep(5)
        self.driver.find_element_by_xpath(self.linkCustomer_link_path).click()

    def clickCustomersLink(self):
        self.driver.find_element_by_xpath(self.linkCustomer_link_path1).click()

    def clickAddNew(self):
        self.driver.find_element_by_xpath(self.linkAddNew_path).click()

    def enterEmail(self,email):
        print("**********Email******* " + str(email))
        self.driver.find_element_by_xpath(self.textbox_email).send_keys(email)

    def enterPassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password).send_keys(password)

    def enterFirstName(self, firstName):
        self.driver.find_element_by_xpath(self.textbox_FirstName).send_keys(firstName)

    def enterLastName(self, lastName):
        self.driver.find_element_by_xpath(self.textbox_LastName).send_keys(lastName)

    def selectGender(self, gender):
        if gender=="Male":
            self.driver.find_element_by_xpath(self.radio_GenderMale).click()
        elif gender=="Female":
            self.driver.find_element_by_xpath(self.radio_GenderMale).click()

    def enterDOB(self, dob):
        self.driver.find_element_by_xpath(self.textbox_dateOfBirth_Id).send_keys(dob)

    def enterCompanyID(self, companyId):
        self.driver.find_element_by_xpath(self.textbox_company_id).send_keys(companyId)

    def selectIsTaxExtempt(self):
        self.driver.find_element_by_xpath(self.checkbox_IsTaxExtempt_id).click()

    def selectNewLetter(self):
        self.driver.find_element_by_xpath(self.NewsLetter_xpath).click()
        self.driver.find_element_by_xpath(self.newsLetter_YourStoreName_xpath).click()

    def selectCustomerRoles(self):
        self.driver.find_element_by_xpath(self.xpath_Customer_Roles).click()
        self.customerRoles = self.driver.find_element_by_xpath(self.xpath_ForumModerators)
        self.driver.execute_script("arguments[0].click();", self.customerRoles)

    def selectManagerOfVendor(self):
        select = Select(self.driver.find_element_by_xpath(self.select_Manager_Of_Vendor))
        select.select_by_visible_text("Vendor 1")

    def enterAdminComment(self, comment):
        self.driver.find_element_by_xpath(self.textArea_AdminComment).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.button_save).click()






