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

    small_cols = max(32, int(cols / (intensity * 4)))
    small_rows = max(32, int(rows / (intensity * 4)))
    img_small = cv2.resize(img, (small_cols, small_rows), interpolation=cv2.INTER_LINEAR)
    img_pixelated = cv2.resize(img_small, (cols, rows), interpolation=cv2.INTER_NEAREST)

    x, y = np.meshgrid(np.arange(cols), np.arange(rows))
    
    x_norm = x.astype(np.float32)
    y_norm = y.astype(np.float32)

    freq = 0.015 * intensity
    phase_x = np.sin(y_norm * freq) * (15 * intensity)
    phase_y = np.cos(x_norm * freq) * (15 * intensity)

    map_x = x_norm + phase_x
    map_y = y_norm + phase_y

    zhmykh_img = cv2.remap(img_pixelated, map_x, map_y, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT_101)

    cv2.imwrite(output_path, zhmykh_img)