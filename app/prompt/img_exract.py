import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    
def img2md(image_path):
    prompt =f"""\
    Convert the picture to LaTeX
"""
    base64_image = encode_image(image_path)
    return [prompt,base64_image]

def img2txt(image_path):
    base64_image = encode_image(image_path)

def img2latex(image_path):
    base64_image = encode_image(image_path)