from Helpers.Corrector import correct_msg
from Helpers.Creator_and_Saver import create_save_gif_or_png, create_save_png_to_png
from PIL import Image, ImageFont
import os

FONT_NAME = "Leto Text Sans Defect.otf"

if __name__ == "__main__":
    folders = [
            r"Here",
            r"Are",
            r"Your",
            r"Folders",
        ]

    for folder in folders:

        # create an output folder
        output_folder = folder + r"\Output"
        # if there is no output folder then create it
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)
        all_files = os.listdir(folder)

        for file in [x for x in all_files if x.split(".")[-1] == "gif" or x.split(".")[-1] == "png"]:
            print(f"---------------\n[LOG]: {file}\n---------------\n")

            img_name = file
            unit_folder = output_folder + fr"/{img_name.split('.')[0]}"
            if not os.path.exists(unit_folder):
                os.mkdir(unit_folder)

            # if there is no output unit folder then create it
            filename_txt = "".join(
                [x for x in all_files if x.split(".")[-1] == "txt" and x.split(".")[0] == file.split(".")[0]])

            # if there is no text then we can just skip it
            if not filename_txt: continue
            # otherwise, we read all unit's words
            f = open(f"{folder}/{filename_txt}", "r", encoding='UTF-8').read().strip()
            sentences = f.split(f"\n")

            for sentence in sentences:
                img = Image.open(f"{folder}/{img_name}")

                _msg_above = sentence.split("---")[0].strip()
                _msg_below = ""
                if "---" in sentence: _msg_below = sentence.split("---")[1].strip()
                print(f"[LOG]: \n\tup:{_msg_above}\n\tdown:{_msg_below}\n")

                # standard font sizes
                font_size_msg = 56
                font_size_msg_below = 42

                font_msg = ImageFont.FreeTypeFont(FONT_NAME, size=font_size_msg, encoding='UTF-8')
                font_msg_below = ImageFont.FreeTypeFont(FONT_NAME, size=font_size_msg_below,
                                                        encoding='UTF-8')

                msg_above = correct_msg(_msg_above, x_img=img.size[0], font_size=font_size_msg)
                msg_below = correct_msg(_msg_below, x_img=img.size[0], font_size=font_size_msg_below)

                """ If text appeared to be extremely large than we decrease font size """
                # length of the largest line in wrapped msg_above
                while msg_above == False or \
                        font_msg.getlength(str([s for s in msg_above.split(f"\n") if
                                                len(s) == max(len(x) for x in msg_above.split(f"\n"))][0]))\
                                                    >= img.size[0] - 20:
                    font_size_msg -= 2
                    font_msg = ImageFont.FreeTypeFont(FONT_NAME, size=font_size_msg, encoding='UTF-8')
                    msg_above = correct_msg(_msg_above, x_img=img.size[0], font_size=font_size_msg)
                # length of the largest line in wrapped msg_below
                while msg_below == False or \
                        font_msg_below.getlength(str([s for s in msg_below.split(f"\n") if
                                                      len(s) == max(len(x) for x in msg_below.split(f"\n"))][0])) >= \
                                                            img.size[0] - 20:
                    font_size_msg_below -= 2
                    font_msg_below = ImageFont.FreeTypeFont(FONT_NAME, size=font_size_msg_below,
                                                            encoding='UTF-8')
                    msg_below = correct_msg(_msg_below, x_img=img.size[0], font_size=font_size_msg_below)

                if img_name.split(".")[-1] == "gif":
                    create_save_gif_or_png(folder=unit_folder, img_name=img_name.split(".")[0], img=img, font=font_msg,
                                           font_mb=font_msg_below, msg=msg_above, ident="gif", msg_below=msg_below,
                                           index=sentences.index(sentence))
                    create_save_gif_or_png(folder=unit_folder, img_name=img_name.split(".")[0], img=img, font=font_msg,
                                           font_mb=font_msg_below, msg=msg_above, ident="png", msg_below=msg_below,
                                           index=sentences.index(sentence))
                elif img_name.split(".")[-1] == "png":
                    create_save_png_to_png(folder=unit_folder, img_name=img_name, w_img=img, font=font_msg, font_mb=font_msg_below,
                                           msg=msg_above, index=sentences.index(sentence), msg_below=msg_below)
