from PIL import Image, ImageSequence
import os
import io
import shutil

def resize_img(img, img_name, folder, height=512, width=512):
    """img should be a PIL.Image object"""
    resized_img = img.resize((width, height), Image.ANTIALIAS)

    # Saves an img - u may just return it if u want to
    if not os.path.exists(f"{folder}/Resized"):
        os.mkdir(f"{folder}/Resized")
    resized_img.save(f"{folder}/Resized/{img_name}.png")


def resize_gif(img, img_name, folder, height=512, width=512):
    frames = []

    for frame in ImageSequence.Iterator(img):
        frame = frame.convert('RGBA')

        frame = frame.resize((width, height))

        b = io.BytesIO()
        frame.save(b, format="GIF")
        frame = Image.open(b)
        frames.append(frame)

    if not os.path.exists(f"{folder}/Resized"):
        os.mkdir(f"{folder}/Resized")
    frames[0].save(f"{folder}/Resized/{img_name}.gif", save_all=True, append_images=frames[1:])


if __name__ == "__main__":\

    gif_folders = [
        r"Human_Folder",
        r"NE_Folder",
        r"Orc_Folder",
        r"UD_Folder",
    ]

    folders = gif_folders

    for folder in folders:
        for sticker in os.listdir(folder):
            # if .png then resize it
            if sticker.split(".")[-1] == "png":
                img = Image.open(fr"{folder}\{sticker}")
                img_name = sticker.split(".")[0]

                resize_img(img, img_name, folder, height=512, width=512)

            # If file is .txt we just copy it to new destination
            if sticker.split(".")[-1] == "txt":
                shutil.copyfile(fr"{folder}\{sticker}", f"{folder}/Resized/{sticker}")

            # if .gif then resize it
            if sticker.split(".")[-1].lower() == "gif":
                img = Image.open(fr"{folder}\{sticker}")
                img_name = sticker.split(".")[0]
                resize_gif(img, img_name, folder)
