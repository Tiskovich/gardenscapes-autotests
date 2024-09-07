from typing import Generator

import pytest
from appium.webdriver.webdriver import WebDriver

from helpers.appium_setup import init_driver


@pytest.fixture
def driver() -> Generator[WebDriver, None, None]:
    driver = init_driver()
    yield driver
    driver.quit()
