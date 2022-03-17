import textwrap


def correct_msg(text, x_img, font_size):
    """"x_img is a width of an image
    font_size is a height(used by default) of a font u use"""
    if not text: return ""
    try:
        corrected_msg = textwrap.wrap(text, width=x_img / (font_size // 2))
        if len(corrected_msg) > 2: return False
    except: return False
    return f"\n".join(corrected_msg)
