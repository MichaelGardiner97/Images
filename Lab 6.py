# Michael Gardiner
# Due Date: 10-13-15
# Convert a normal, color picture into a picture of 4 colors

'''
Get total Pixel ranges and set each color for 4 different ranges of total Pixels to replace the pixels already there
'''

import cImage as image
img = image.Image("starwars.gif")
win = image.ImageWin(img.getWidth(), img.getHeight())

  
#cyan: 0, 255, 155

def cyan(col, row, p, img):
    p.setRed(0)
    p.setGreen(255)
    p.setBlue(155)

#blue: 30, 145, 200

def blue(col, row, p, img):
    p.setRed(30)
    p.setGreen(145)
    p.setBlue(200)

#seagreen: 84, 255, 159

def seagreen(col, row, p, img):
    p.setRed(184)
    p.setGreen(255)
    p.setBlue(159)

#aquamarine: 125, 255, 212
    
def aquamarine(col, row, p, img):
    p.setRed(125)
    p.setGreen(255)
    p.setBlue(212)

def main():
   
    for row in range (img.getHeight()):
        for col in range(img.getWidth()):

            p = img.getPixel(col, row)
    
    #Find total of RBG values to pinpoint Pixels and replace later on
            total = p.getRed() + p.getGreen() + p.getBlue()

       #Set RGB Values to one of four colors above based on the total RBG value of the pixels already

            if total <= 75:
                cyan(col, row, p, img)
                
            elif total <=  250:
                blue(col, row, p, img)
                
            elif total <= 400:
                seagreen(col, row, p, img)
                
            else:
                aquamarine(col, row, p, img)

            img.setPixel(col, row, p)

    img.draw(win)

main()
