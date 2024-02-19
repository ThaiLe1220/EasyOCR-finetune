import random
from PIL import Image, ImageDraw, ImageFont

# Font configuration
fonts = [
    "/Library/Fonts/Songti.ttc",
    "/Library/Fonts/STHeiti Medium.ttc",
    "/Library/Fonts/PingFang.ttc",
]

# Formatting Options
font_sizes = [32, 40, 48, 56]
styles = ["normal", "bold", "italic"]
backgrounds = ["white", "lightgray", "lightyellow", "black", "blue", "red"]

# Read text lines from source.txt
with open("source.txt", "r", encoding="utf-8") as file:
    text_lines = file.readlines()

# Process each text line as a separate image
for index, line in enumerate(text_lines):
    line = line.strip()

    if line:
        # Random Formatting Choices
        font_path = random.choice(fonts)
        font_size = random.choice(font_sizes)
        style = random.choice(styles)
        background_color = random.choice(backgrounds)

        # Determine base color (for choosing a contrasting text color)
        is_background_dark = background_color in ["black", "red", "blue"]

        # Choose contrasting text color
        if is_background_dark:
            text_color = random.choice(["white", "lightgray", "lightyellow"])
        else:
            text_color = random.choice(["black", "red", "blue"])

        img_height = font_size + 10
        img_width = font_size * len(line) + 20
        img = Image.new("RGB", (img_width, img_height), color=background_color)
        draw = ImageDraw.Draw(img)

        # Configure font object with style
        if style == "bold":
            font = ImageFont.truetype(font_path, font_size)
        elif style == "italic":
            font = ImageFont.truetype(font_path, font_size)
        else:
            font = ImageFont.truetype(font_path, font_size)

        draw.text((10, 0), line, font=font, fill=text_color)

        img.save(f"./img/chinese_text_image_{index+1}.jpeg")
