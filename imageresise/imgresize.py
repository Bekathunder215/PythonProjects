from PIL import Image
image = Image.open("imageresise/issokbirdie.jpeg")
rgbimg = image.convert("RGB")

smallerimg = image.resize((360, 407))
biggerimg = image.resize((1280, 1446))

smallerimg.convert("RGB").save("imageresise/smallissokbirdie.jpeg")
biggerimg.convert("RGB").save("imageresise/bigissokbirdie.jpeg")
