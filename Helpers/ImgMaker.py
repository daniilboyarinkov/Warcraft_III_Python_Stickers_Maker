from PIL import ImageFont
from Corrector import correct_msg
from Creator_and_Saver import create_save_gif_or_png


def img_maker(sentences, img, folder, img_name):
    for sentence in sentences:
        msg_above = sentence.split("---")[0].strip()
        msg_below = ""
        if "---" in sentence: msg_below = sentence.split("---")[1].strip()
        print(f"[LOG]: \n\tup:{msg_above}\n\tdown:{msg_below}\n")

        font_size_msg = 56
        font_size_msg_below = 42

        font_msg = ImageFont.FreeTypeFont("Font/Ubuntu-Regular.ttf", size=font_size_msg, encoding='UTF-8')
        font_msg_below = ImageFont.FreeTypeFont("Font/Ubuntu-Regular.ttf", size=font_size_msg_below, encoding='UTF-8')

        msg_above = correct_msg(msg_above, x_img=img.size[0], font_size=font_size_msg)
        msg_below = correct_msg(msg_below, x_img=img.size[0], font_size=font_size_msg_below)

        # length of the largest line in wrapped msg_above
        while msg_above == False or \
                font_msg.getlength(str([s for s in msg_above.split(f"\n") if len(s) == max(len(x) for x in msg_above.split(f"\n"))][0])) >= img.size[0] - 20:
            font_size_msg -= 2
            font_msg = ImageFont.FreeTypeFont("Font/Ubuntu-Regular.ttf", size=font_size_msg, encoding='UTF-8')
            msg_above = correct_msg(msg_above, x_img=img.size[0], font_size=font_size_msg)

        # length of the largest line in wrapped msg_below
        while msg_below == False or \
                font_msg_below.getlength(str([s for s in msg_below.split(f"\n") if len(s) == max(len(x) for x in msg_below.split(f"\n"))][0])) >= img.size[0] - 20:
            font_size_msg_below -= 2
            font_msg_below = ImageFont.FreeTypeFont("Font/Ubuntu-Regular.ttf", size=font_size_msg_below, encoding='UTF-8')
            msg_below = correct_msg(msg_below, x_img=img.size[0], font_size=font_size_msg_below)

        create_save_gif_or_png(folder=folder, img_name=img_name.split(".")[0], img=img, font=font_msg,
                               font_mb=font_msg_below, msg=msg_above, ident="gif", msg_below=msg_below,
                               index=sentences.index(sentence))
        create_save_gif_or_png(folder=folder, img_name=img_name.split(".")[0], img=img, font=font_msg,
                               font_mb=font_msg_below, msg=msg_above, ident="png", msg_below=msg_below,
                               index=sentences.index(sentence))
