from PIL import Image, ImageDraw, ImageSequence
import io
import os

STROKE_WIDTH = 4

# Works only with GIFs
def create_save_gif_or_png(folder, img_name, img, font, font_mb, msg, index, msg_below, ident: str):
	frames = []

	for frame in ImageSequence.Iterator(img):
		frame = frame.convert('RGBA')
		d = ImageDraw.Draw(frame)

		# x and y coords of the place to locate
		text_width = d.multiline_textsize(text=msg, font=font)[0]
		x = (img.size[0] - text_width) / 2
		y = 15

		# x and y coords of the place to locate down below
		text_width_below = d.multiline_textsize(text=msg_below, font=font_mb)[0]
		x_n = (img.size[0] - text_width_below) / 2
		y_n = img.size[1] - d.multiline_textsize(text=msg_below, font=font_mb)[1] - 40

		# Filling the text
		d.multiline_text((x, y), msg, font=font, fill="white", align="center", stroke_width=STROKE_WIDTH, stroke_fill="black")

		# Filling the text down below
		d.multiline_text((x_n, y_n), msg_below, font=font_mb, fill="white", align="center", stroke_width=STROKE_WIDTH,
						 stroke_fill="black")

		del d

		b = io.BytesIO()
		if ident.lower() == "png":
			if not os.path.exists(f"{folder}/Sticker"):
				os.mkdir(f"{folder}/Sticker")
			frame.save(f"{folder}/Sticker/{img_name} ({index}).png")
			return
		elif ident.lower() == "gif":
			frame.save(b, format="GIF")
			frame = Image.open(b)
			frames.append(frame)

	if ident.lower() == "gif":
		if not os.path.exists(f"{folder}/GIF"):
			os.mkdir(f"{folder}/GIF")
		frames[0].save(f"{folder}/GIF/{img_name} ({index}).gif", save_all=True, append_images=frames[1:])

# Works only with IMGs (not GIFs)
# Actually works kinda weird. So, I suggest to use gif whenever u can
def create_save_png_to_png(folder, img_name, w_img, font, font_mb, msg, index, msg_below):
	d = ImageDraw.Draw(w_img)

	# x and y coords of the place to locate
	text_width = d.multiline_textsize(text=msg, font=font)[0]
	x = (w_img.size[0] - text_width) / 2
	y = 15

	# x and y coords of the place to locate down below
	text_width_below = d.multiline_textsize(text=msg_below, font=font_mb)[0]
	x_n = (w_img.size[0] - text_width_below) / 2
	y_n = w_img.size[1] - d.multiline_textsize(text=msg_below, font=font_mb)[1] - 40

	# Filling the text
	d.multiline_text((x, y), msg, font=font, fill="white", align="center", stroke_width=STROKE_WIDTH, stroke_fill="black")

	# Filling the text down below
	d.multiline_text((x_n, y_n), msg_below, font=font_mb, fill="white", align="center", stroke_width=STROKE_WIDTH,
					 stroke_fill="black")

	w_img.save(f"{folder}/{img_name} ({index}).png")

	del w_img

