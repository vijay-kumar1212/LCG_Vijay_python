import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    ser = Service("C://chromedriver.exe")
    driver = webdriver.Chrome(service=ser)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
    request.cls.driver = driver
    yield
    driver.close()