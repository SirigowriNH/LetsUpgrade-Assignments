# LetsUpgrade-Assignments
Assignments submitted by Sirigowri

Steps followed to get the output : 
1. Open a new file in file editor
2. Import Pillow Library - In order to write text on image we need to have certain functions like Image, ImageFont and ImageDraw. 
                           So in order to get these functions we downloaded the Pillow(PIL) library
3. Take input text from user                            
4. Save the image in a folder on which text is written
5. Then choose the Image using - Image.open("imagename.extension")
6. For font selection use - myfont = ImageFont.truetype("helvetica.ttf",30) 
       where : helvetica is selected font style and 30 is font size
       ImageFont is the function of PIL to define font 
       myfont is the variable to contain the details
7. Next use ImageDraw function to convert our image to editable format
8. Then provide the Cartesian co-ordinates to place the text, text to be displayed, font colour and myfont details 
9. Finally show the image and save it
