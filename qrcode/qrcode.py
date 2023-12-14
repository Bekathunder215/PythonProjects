#we install qrcode library and Image library
import qrcode

def makeqr(url):
    image = qrcode.make(url)
    type(img)
    image.save("QRimage.png")

makeqr("https://www.youtube.com/watch?v=xvFZjo5PgG0")