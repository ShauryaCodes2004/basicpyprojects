import qrcode as qr
from PIL import Image
img =  qr.make("https://www.youtube.com/")

img=qr.make_image(fill_color="red",back_color="blue")
img.save("Youtubecolor.png")
