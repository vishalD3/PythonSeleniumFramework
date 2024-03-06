import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setupBrowser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
       Service_Obj1 = Service("C:/Users/DeshpandeV/PycharmProjects/PythonSelenium/FreshProject/Driver/chrome/chromedriver.exe")
       driver = webdriver.Chrome(service=Service_Obj1)

    elif browser_name == "firefox":
         Service_Obj1 = Service("C:/Users/DeshpandeV/PycharmProjects/PythonSelenium/FreshProject/Driver/firefox/geckodriver.exe")
         driver = webdriver.Firefox(service=Service_Obj1)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()
