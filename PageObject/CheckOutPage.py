from selenium.webdriver.common.by import By

from PageObject.ConfirmPage import confirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    cardAdd = (By.XPATH, "div/button")
    checkBtn = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    submitBtnChkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def addProduct(self):
        return self.driver.find_element(*CheckOutPage.cardAdd)

    def checkOutBtn(self):
        return self.driver.find_element(*CheckOutPage.checkBtn)


    def submitBtn(self):
        return self.driver.find_element(*CheckOutPage.submitBtnChkOut)

