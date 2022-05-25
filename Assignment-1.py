from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def fun1():
    UserName= input("What is your name: ")
    img = Image.open("name.png")
    I1 = ImageDraw.Draw(img)
    myFont=ImageFont.truetype("helvetica-bold.ttf",27)
    (x,y) = (460,260)
    color = 'rgb(0,0,0)'
    I1.text((x,y), UserName, fill=color, font=myFont )
    img.show
    img.save("output.png") 


fun1()
