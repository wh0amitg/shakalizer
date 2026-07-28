import cv2
import numpy as np
from PIL import Image

def deep_fry(input_path, output_path, level=5):
    level = max(1, min(10, int(level)))
    quality_map = {
        1: 95, 2: 80, 3: 60, 4: 40, 5: 25,
        6: 15, 7: 10, 8: 5, 9: 2, 10: 1
    }
    img = Image.open(input_path).convert("RGB")
    img.save(output_path, "JPEG", quality=quality_map[level])

def zhmykh(input_path, output_path, intensity=1.5):
    img = cv2.imread(input_path)
    if img is None:
        raise ValueError("cant read pic for zhmykh")

    rows, cols = img.shape[:2]
    x, y = np.meshgrid(np.arange(cols), np.arange(rows))

    x_norm = 2.0 * x / cols - 1.0
    y_norm = 2.0 * y / rows - 1.0

    r = np.sqrt(x_norm**2 + y_norm**2)
    theta = np.arctan2(y_norm, x_norm)
    r_zhmykh = r ** (1.0 + (intensity * 0.5))
    theta_zhmykh = theta + (r * intensity * 0.8)
    wave_x = np.sin(y_norm * 10) * (0.05 * intensity)
    wave_y = np.cos(x_norm * 10) * (0.05 * intensity)

    x_new = (r_zhmykh * np.cos(theta_zhmykh) + wave_x + 1.0) * cols / 2.0
    y_new = (r_zhmykh * np.sin(theta_zhmykh) + wave_y + 1.0) * rows / 2.0

    map_x = np.float32(x_new)
    map_y = np.float32(y_new)

    zhmykh_img = cv2.remap(img, map_x, map_y, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT_101)

    cv2.imwrite(output_path, zhmykh_img)