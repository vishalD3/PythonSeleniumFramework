from selenium.webdriver.common.by import By

from PageObject.CheckOutPage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[@href='/angularpractice/shop']")
    enterEmail = (By.NAME, "email")
    enterPassword = (By.ID, "exampleInputPassword1")
    clickCheckBox = (By.ID, "exampleCheck1")
    enterName = (By.CSS_SELECTOR, "input[name='name']")
    clickSubmitBtn = (By.XPATH, "//input[@type='submit']")
    successMessage = (By.CLASS_NAME, "alert-success")
    selectGender = (By.ID, "exampleFormControlSelect1")

    def shopItem(self):
        self.driver.find_element(*HomePage.shop).click()
        productList = CheckOutPage(self.driver)
        return productList

    def putEmail(self):
        return self.driver.find_element(*HomePage.enterEmail)

    def addPassword(self):
        return self.driver.find_element(*HomePage.enterPassword)

    def checkBox(self):
        return self.driver.find_element(*HomePage.clickCheckBox)

    def addName(self):
        return self.driver.find_element(*HomePage.enterName)

    def getGender(self):
        return self.driver.find_element(*HomePage.selectGender)

    def submitBtn(self):
        return self.driver.find_element(*HomePage.clickSubmitBtn)

    def checkSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)



