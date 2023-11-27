from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='class')
def setupLogin(request):
    service_obj = Service()
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    driver.get(url='https://xprizo-test.azurewebsites.net/#/login')
    request.cls.driver = driver   # In this, we define 'request' as we define driver to class, and when we use
    # this class on other class, then we just use it.  isme return nahi krunga kyuki usse yield statement execute
    # nahi hogi.
    yield
    driver.close()
