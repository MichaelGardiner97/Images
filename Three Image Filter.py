import cImage as image
img = image.Image("TreeSmall.gif")
win = image.ImageWin(img.getWidth(), img.getHeight())

def main():

    answer = input("Would you like to Red Channel, Grayscale, or Invert the images pixels?    red/gray/invert:    ")

    for row in range (img.getHeight()):
        for col in range(img.getWidth()):

            p = img.getPixel(col, row)

            if answer.lower() == 'red':
                R = p.getRed()
                noG = (p.getRed() * 0 + p.getGreen() * 0 + p.getBlue() * 0)
                noB = (p.getRed() * 0 + p.getGreen() * 0 + p.getBlue() * 0)
                newpixel = image.Pixel(R, noG, noB)


            elif answer.lower() == 'gray':
                grayR = ((p.getRed() + p.getGreen() + p.getBlue()) /3)
                grayG = ((p.getRed() + p.getGreen() + p.getBlue()) /3)
                grayB = ((p.getRed() + p.getGreen() + p.getBlue()) /3)
                newpixel = image.Pixel(grayR, grayG, grayB)


            else:
                invR = (255 - p.getRed())
                invG = (255 - p.getGreen())
                invB = (255 - p.getBlue())
                newpixel = image.Pixel(invR, invG, invB)

            img.setPixel(col, row, newpixel)

main()
    
img.draw(win)
win.exitonclick()
