import qrcode
a = qrcode.make("https://www.youtube.com/")
a.save("see.png")