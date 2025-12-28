from PIL import Image

def check_transparency(path):
    try:
        im = Image.open(path)
        im = im.convert("RGBA")
        
        # Check top-left corner (0,0)
        pixel = im.getpixel((0, 0))
        print(f"Top-left pixel at (0,0): {pixel}")
        
        if pixel[3] == 0:
            print("Top-left is transparent.")
        else:
            print("Top-left is NOT transparent.")
            
    except Exception as e:
        print(f"Error: {e}")

check_transparency('logo.gif')
