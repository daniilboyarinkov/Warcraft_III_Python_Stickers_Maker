from PIL import Image
import os

def resize_img(img, img_name, folder, height=512, width=512):
    """img should be a PIL.Image object"""
    resized_img = img.resize((width, height), Image.ANTIALIAS)

    # Saves an img - u may just return it if u want to
    if not os.path.exists(f"{folder}/Resized"):
        os.mkdir(f"{folder}/Resized")
    resized_img.save(f"{folder}/Resized/{img_name} - resized.png")


if __name__ == "__main__":
    # folder = r"C:\Users\BitDittoWit\Desktop\Wc3 Stickers\NE\Stickers"
    # folder = r"C:\Users\BitDittoWit\PycharmProjects\BittoCheat_Warcraft3_bot\wc3_gifs\Night Elf\refactor\Output"
    # folder = r"C:\Users\BitDittoWit\Desktop\Wc3 Stickers\Orc\Stickers"
    # folder = r"C:\Users\BitDittoWit\Desktop\Wc3 Stickers\UD\Stickers"
    folder = r"C:\Users\BitDittoWit\Desktop\Wc3 Stickers\Human\Stickers"

    for sticker in os.listdir(folder):
        img = Image.open(fr"{folder}\{sticker}")
        img_name = sticker.split(".")[0]

        resize_img(img, img_name,folder)
