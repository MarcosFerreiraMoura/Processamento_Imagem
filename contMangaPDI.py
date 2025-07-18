from PIL import Image
from utils import in_file, out_file

def escalaCinza(colored):
    w, h = colored.size
    img = Image.new("RGB",(w, h))

    for x in range(w):
        for y in range (h):
            pxl = colored.getpixel((x,y))
            lum = (pxl[0] + pxl[1] + pxl[2])//3
            img.putpixel((x,y), (lum, lum, lum))

    return img

if __name__ == "__main__":
    img  = Image.open(in_file("imageManga.jpg"))
    print(img.getpixel((200, 200)))
    print(img.getpixel((100, 100)))
    print(img.getpixel((300, 300)))


    manga = Image.open(in_file("imageManga.jpg"))
    pbManga = escalaCinza(manga)
    pbManga.save(out_file("pbManga.jpg"))

