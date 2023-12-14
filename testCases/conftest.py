import datetime
import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pytest_metadata.plugin import metadata_key
from pytest_html import hooks

@pytest.fixture()
def setup(browser):
    if browser=='edge':
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        print('launching Edge browser.................')
    elif browser=='firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        print('launching firefox browser.................')
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print('launching chrome browser..................')

    return driver

def pytest_addoption(parser):    # this will get value from command line prompt
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   #this will return browser value to setup method
    return request.config.getoption("--browser")

############# pytest html report##################################################
# it is a hook to add environment info to HTML Report

def pytest_configure (config):
    config._metadata['Project Name'] = 'opencart'
    config._metadata['Module Name'] = 'registartion'
    config._metadata['Tester'] = 'anagha'

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config.stash[metadata_key]['Project Name'] = "opencart"
    session.config.stash[metadata_key]['Module Name'] = "registration"
    session.config.stash[metadata_key]['Tester'] = "Anagha"


#It is a hook for delete/modify environment info to HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME',None)  # remove unwanted data from report
    metadata.pop('Plugins',None)

#specifying report folder location and save report with timestamp and because of this hook we dont need to specify location in command promp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath="E:\\pythonProject2\\reports\\"+datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"