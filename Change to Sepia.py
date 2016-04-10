import cImage as image
img = image.Image("TreeSmall.gif")
win = image.ImageWin(img.getWidth(), img.getHeight())

img.draw(win)
img.setDelay(0)

for row in range (img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        newR = (p.getRed()*0.393 + p.getGreen()*0.769 + p.getBlue()*0.189)
        newG = (p.getRed()*0.349 + p.getGreen()*0.686 + p.getBlue()*0.168)
        newB = (p.getRed()*0.272 + p.getGreen()*0.534 + p.getBlue()*0.131)

        newpixel = image.Pixel(newR, newG, newB)

        img.setPixel(col, row, newpixel)
    
img.draw(win)
win.exitonclick()


