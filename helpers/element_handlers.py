import time
from pathlib import Path
from typing import Optional, Tuple

import numpy as np
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.pointer_input import PointerInput

from helpers.image_handlers import get_images_diff_coordinates, load_image


def tap_element(driver: WebDriver, x: int, y: int):
    touch_input = PointerInput(POINTER_TOUCH, "touch")
    actions = ActionBuilder(driver, mouse=touch_input)
    actions.pointer_action.move_to_location(x=x, y=y).pointer_down().pointer_up()
    actions.perform()


def wait_for_img_element(driver: WebDriver, element_img_path: Path, timeout: int = 30) -> Optional[Tuple[np.ndarray]]:
    element_img = load_image(element_img_path)
    start_time = time.time()

    while time.time() - start_time < timeout:
        current_screenshot = Path('current_screen.png')
        driver.save_screenshot(current_screenshot)
        screen_img = load_image(current_screenshot)
        if coordinates := get_images_diff_coordinates(screen_img, element_img):
            return coordinates
        else:
            print(f"Element '{element_img_path.name}' not found, continuing to wait...")
            time.sleep(1)
    return None
