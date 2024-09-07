from pathlib import Path

from conftest import driver
from helpers.element_handlers import tap_element, wait_for_img_element
from helpers.image_handlers import load_image


class TestSmoke:
    def test_game_started(self, driver):
        project_root = Path(__file__).resolve().parents[1]
        images_dir = project_root / 'images'
        play_button_path = images_dir / 'play_button.png'
        game_started_path = images_dir / 'game_started.png'

        location = wait_for_img_element(driver, play_button_path)
        assert location, "Button 'play' is not present on the screen"

        play_button_img = load_image(play_button_path)
        w, h = play_button_img.shape[1], play_button_img.shape[0]
        elem_start_coordinates = (location[1][0], location[0][0])
        center_x = elem_start_coordinates[0] + w // 2
        center_y = elem_start_coordinates[1] + h // 2
        tap_element(driver, center_x, center_y)

        location = wait_for_img_element(driver, game_started_path)
        assert location, "Game has not opened after pressing the play button"
