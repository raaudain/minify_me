import os, sys, glob
from PIL import Image

cwd = os.getcwd()
image_types = (".png", ".jpg", ".jpeg", ".gif", ".tif", ".tiff", ".bmp", ".ico")

def minify(file, verbose=False):
    image = Image.open(file)

    if os.path.splitext(file)[1].lower() == ".png":
        # Change from 24-bit to 8-bit
        image = image.convert(mode="P", palette=Image.ADAPTIVE)
        # image = image.quantize(method=1)
        image.save(file, optimize=True, quality=100)
    else:
        image = image.convert("RGB")
        image.save(file, optimize=True, quality=75)

def main():
    verbose = False

    if len(sys.argv) > 1 and sys.argv[1].lower() == "-v":
        verbose = True
    
    for file in glob.glob(os.path.join(cwd, "**/*"), recursive=True):
        if os.path.splitext(file)[1].lower() in image_types:
            minify(file, verbose)
            print("Compressing", os.path.basename(file), "in", os.path.dirname(file))
    
    print("Done")

main()
sys.exit(0)