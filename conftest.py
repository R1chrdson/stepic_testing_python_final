import pytest 
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
	
def pytest_addoption(parser):
	parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: firefox or chrome")
	parser.addoption('--language', action='store', default=None, help="Say language name to select")
	

@pytest.fixture(scope="function")
def browser(request):
	choosen_language = request.config.getoption("language")
	browser_name = request.config.getoption("browser_name")
	if browser_name == "chrome":
		opts = Options()
		opts.add_experimental_option('prefs', {'intl.accept_languages': choosen_language})
		opts.add_experimental_option('w3c', False)
		browser = webdriver.Chrome(options=opts)
	
	yield browser

	sleep(10)
	browser.quit()
