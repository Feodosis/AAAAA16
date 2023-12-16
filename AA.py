from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

with Image.open("images.jfif") as pic_original:
    print("Розмір картинки:", pic_original.size)
    print("Формат:", pic_original.format)
    print("Тип:", pic_original.mode)
    pic_original.show()

    pic_gray = pic_original.convert("L")
    pic_gray.save("gray.jfif")
    pic_gray.show()

    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_blured.save("blured.jfif")
    pic_blured.show()

    pic_up = pic_original.transpose(Image.ROTATE_180)
    pic_up.save("up.jfif")
    pic_up.show()

    pic_mirrow = pic_original.transpose(Image.FLIP_LEFT_RIGHT)
    pic_mirrow.save("mirrow.jfif")
    pic_mirrow.show()

    pic_contrast = ImageEnhance.Contrast(pic_original)
    pic_contrast = pic_contrast.enhance(1.5)
    pic_contrast.save("contrast.jfif")
    pic_contrast.show()

    pic_gray_smooth = pic_original.filter(ImageFilter.SMOOTH)
    pic_gray_smooth = pic_gray_smooth.filter(ImageFilter.FIND_EDGES)
    pic_gray_smooth.save("smooth.jfif")
    pic_gray_smooth.show()

    pic_rotated = pic_original.rotate(30, expand=True)
    pic_rotated.save("rotated.jfif")
    pic_rotated.show()