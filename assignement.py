import qrcode

img = qrcode.make("Hello sir! This is Gelai!")
img.save("mycode.png")
