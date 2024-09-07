from pathlib import Path
from typing import Optional, Tuple

import cv2
import numpy as np


def get_images_diff_coordinates(screenshot, template, threshold=0.6) -> Optional[Tuple[np.ndarray]]:
    res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    return loc if len(loc[0]) > 0 else None


def load_image(image_path: Path) -> cv2.typing.MatLike:
    return cv2.imread(str(image_path), cv2.COLOR_BGR2GRAY)
