# 📉 Shakalizer

> A lightweight Python library for quickly "deep frying" images: reducing bitrate, adding heavy JPEG artifacts, and scaling down resolution in the style of classic internet memes.

[![PyPI version](https://img.shields.io/pypi/v/shakalizer.svg)](https://pypi.org/project/shakalizer/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📦 Installation

Install the library using `pip`:

```bash
pip install shakalizer

```

## 🚀 Quick Start

Just one line of code to turn a crisp image into a compressed masterpiece:

```python
from shakalizer import deep_fry

deep_fry("input.jpg", output_path="output.jpg", quality=5, scale=0.3)

```

## 🛠️ Script Example

```python
from shakalizer import deep_fry

deep_fry(
    image_path="meme.jpg", 
    output_path="meme_shakal.jpg", 
    quality=2, 
    scale=0.2
)

print("Image successfully deep-fried!")

```
