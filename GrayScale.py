import cImage as image

img = image.Image("Cool_converted.gif")
win = image.ImageWin(img.getWidth(), img.getHeight())

img.draw(win)
    
for row in range (img.getHeight()):
    for col in range(img.getWidth()):

        p = img.getPixel(col, row)

        newR = ((p.getRed() + p.getGreen() + p.getBlue()) /3)
        newG = ((p.getRed() + p.getGreen() + p.getBlue()) /3)
        newB = ((p.getRed() + p.getGreen() + p.getBlue()) /3)

        newpixel = image.Pixel(newR, newG, newB)
        
        img.setPixel(col, row, newpixel)

img.draw(win)
wn.exitonclick
