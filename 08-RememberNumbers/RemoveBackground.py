import rembg
from PIL import Image

olderPicture = Image.open("SajjadSaljoghi.jpg")
newerPicture = rembg.remove(olderPicture)
newerPicture.save("SajjadSaljoghi.png")