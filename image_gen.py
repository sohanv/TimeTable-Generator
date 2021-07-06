from PIL import Image, ImageFont, ImageDraw

def gen_img(table):
    img = Image.open("blank.jpg")
    font = ImageFont.truetype("font/Anonymous_Pro/AnonymousPro-Regular.ttf", 30)

    draw = ImageDraw.Draw(img)

    text = table

    draw.multiline_text((50,50), text,fill = "black", font=font)

    img.save("tt-new.jpg")
    img.show()