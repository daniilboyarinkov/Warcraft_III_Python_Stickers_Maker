from PIL import Image
from Helpers.ImgMaker import img_maker
import os

if __name__ == "__main__":
    # Initializing evrth
    folders = [r"The/Root/Folder"]
    for folder in folders:

        # create an output folder
        output_folder = folder + r"\Output"
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)
        all_files = os.listdir(folder)

        for file in [x for x in all_files if x.split(".")[-1] == "gif"]:
            print(f"---------------\n[LOG]: {file}\n---------------\n")

            img_name = file
            unit_folder = output_folder + fr"/{img_name.split('.')[0]}"
            if not os.path.exists(unit_folder):
                os.mkdir(unit_folder)

            filename_txt = "".join(
                [x for x in all_files if x.split(".")[-1] == "txt" and x.split(".")[0] == file.split(".")[0]])

            img = Image.open(f"{folder}/{img_name}")

            if not filename_txt: continue
            f = open(f"{folder}/{filename_txt}", "r", encoding='UTF-8').read().strip()
            sentences = f.split(f"\n")

            img_maker(sentences=sentences, img=img, folder=unit_folder, img_name=img_name)
