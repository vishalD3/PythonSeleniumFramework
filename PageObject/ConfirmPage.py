from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class confirmPage:

    def __init__(self, driver):
        self.driver = driver
        #self.wait = WebDriverWait(self.driver,10)

    slectCountry = (By.ID, "country")
    Country_Click = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitCheckPageBtn = (By.XPATH, "//input[@type='submit']")
    SuccessText = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def addCountry(self):
        return  self.driver.find_element(*confirmPage.slectCountry)

    #def wait_for(self):
       # return self.wait.until(expected_conditions.presence_of_element_located(self.Country_Click))

    def selectCountry(self):
        return self.driver.find_element(*confirmPage.Country_Click)

    def click_checkBox(self):
        return self.driver.find_element(*confirmPage.checkBox)

    def submit_btn(self):
        return self.driver.find_element(*confirmPage.submitCheckPageBtn)

    def text_Sucess(self):
        return self.driver.find_element(*confirmPage.SuccessText)



