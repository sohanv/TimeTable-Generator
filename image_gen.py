from PIL import Image, ImageFont, ImageDraw

def gen_img(table):     #function to draw the table on the blank image
    img = Image.open("blank.jpg")
    font = ImageFont.truetype("font/Anonymous_Pro/AnonymousPro-Regular.ttf", 34)

    draw = ImageDraw.Draw(img)

    text = table

    draw.multiline_text((50,50), text,fill = "black", font=font)

    img.save("tt-new.jpg")