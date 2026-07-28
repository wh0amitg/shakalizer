# 📉 Shakalizer

> A lightweight Python library for quickly "deep frying" images (adding heavy JPEG artifacts) and applying cursed "zhmykh" (liquify/warp distortions) in the style of classic internet memes.

[![PyPI version](https://img.shields.io/pypi/v/shakalizer.svg)](https://pypi.org/project/shakalizer/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📦 Installation

Install the library using `pip`:

```bash
pip install shakalizer

```

*(Note: Requires `Pillow`, `opencv-python`, and `numpy`)*

## 🚀 Quick Start

The library includes two main features: **Deep Frying** (compression) and **Warping** (zhmykh).

### 1. Deep Frying

Turn a crisp image into a compressed masterpiece using levels from 1 (light) to 10 (maximum pixelation):

```python
from shakalizer import deep_fry

deep_fry("input.jpg", "output.jpg", level=10)

```

### 2. Warping

Twist, inflate, and distort the image space for that cursed liquify effect:

```python
from shakalizer import zhmykh

zhmykh("input.jpg", "output_zhmykh.jpg", intensity=2.0)

```

## 🛠️ Script Example

You can use both functions independently or combine them for the ultimate cursed image!

```python
from shakalizer import deep_fry, zhmykh

# 1. Pure Zhmykh effect
zhmykh(
    input_path="meme.jpg", 
    output_path="meme_warped.jpg", 
    intensity=2.5
)
print("Image successfully warped! 🌀")

# 2. Classic Deep Fry
deep_fry(
    input_path="meme.jpg", 
    output_path="meme_shakal.jpg", 
    level=8
)
print("Image successfully deep-fried! 🐕")

```
