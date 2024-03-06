from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.CheckOutPage import CheckOutPage
from PageObject.ConfirmPage import confirmPage
from PageObject.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class TestCaseOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        productList = homePage.shopItem()
        log.info("Getting all card title")
        cards = productList.getCardTitles()
        i = -1
        for ele in cards:
            i += 1
            product_name = ele.text
            log.info(product_name)
            if product_name == "Blackberry":
                productList.addProduct()[i].click()
        productList.checkOutBtn().click()
        productList.submitBtn().click()
        countrySelection = confirmPage(self.driver)
        log.info("Selecting contry name as IND")
        countrySelection.addCountry().send_keys("ind")
        self.verifyTextPresence("India")
        countrySelection.selectCountry().click()
        countrySelection.click_checkBox().click()
        countrySelection.submit_btn().click()
        Result = countrySelection.text_Sucess().text
        log.info("Message from the application is "+Result)
        assert "Success! Thank you!" in Result
