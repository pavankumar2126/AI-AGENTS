from PIL import Image

def load_image(path):
    try:
        img = Image.open(path)
        return img
    except Exception as e:
        print("Image load error:", e)
        return None