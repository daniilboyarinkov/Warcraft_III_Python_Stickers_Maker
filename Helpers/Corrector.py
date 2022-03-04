import textwrap


def manual_center_anchor(corrected_msg):
    """"corrected_msg should be list of str"""
    max_len = max(len(x) for x in corrected_msg)
    for i in range(len(corrected_msg)):
        if not len(corrected_msg[i]) == max_len:
            corrected_msg[i] = " " * ((max_len - len(corrected_msg[i])) // 4) + corrected_msg[i]
    if any(len(x) < 2 for x in corrected_msg):
        return False
    return f"\n".join(corrected_msg)


def correct_msg(text, x_img, font_size):
    """"x_img is a width of an image
    font_size is a height(used by default) of a font u use"""
    if not text: return ""
    try:
        corrected_msg = textwrap.wrap(text, width=x_img / (font_size // 2))
        if len(corrected_msg) > 3: return False
    except: return False
    return manual_center_anchor(corrected_msg)
