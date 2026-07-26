from io import BytesIO
from PIL import Image

def deep_fry(
    image_path: str,
    output_path: str = None,
    quality: int = 10,
    scale: float = 0.5,
) -> Image.Image:

  img = Image.open(image_path)

  if img.mode in ("RGBA", "P"):
    img = img.convert("RGB")

  new_width = int(img.width * scale)
  new_height = int(img.height * scale)
  img_resized = img.resize((new_width, new_height), Image.Resampling.NEAREST)

  buffer = BytesIO()
  img_resized.save(buffer, format="JPEG", quality=quality)
  buffer.seek(0)
  shakled_img = Image.open(buffer)

  if output_path:
    shakled_img.save(output_path, "JPEG")

  return shakled_img