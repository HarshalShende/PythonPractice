from PIL import Image
img = Image.open("color-to-bw/mycartoon.png")
contobw = img.convert("L")
contobw.save("color-to-bw/mycartoon-b.png")
contobw.show()