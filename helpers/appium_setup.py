from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.webdriver import WebDriver


def init_driver() -> WebDriver:
    capabilities = {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'Android',
        'appPackage': 'com.playrix.gardenscapes',
        'appActivity': '.StoreActivity',
    }
    appium_server_url = 'http://localhost:4723'
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    return driver
