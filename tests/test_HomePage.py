import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

from PageObject.HomePage import HomePage
from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_submitForm(self, getData):
        homePage = HomePage(self.driver)
        homePage.addName().send_keys(getData["firstname"])
        homePage.putEmail().send_keys(getData["email"])
        homePage.addPassword().send_keys(getData["password"])
        homePage.checkBox().click()
        self.selectOptionByText(homePage.getGender(), getData["gender"])
        homePage.submitBtn().click()
        message = homePage.checkSuccessMessage().text
        print(message)
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("testCase2"))
    def getData(self, request):
        return request.param
