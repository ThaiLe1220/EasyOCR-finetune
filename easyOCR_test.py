import easyocr

reader = easyocr.Reader(["en"])  # Load an English language model
result = reader.readtext("my_image.jpg")
print(result)
