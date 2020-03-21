from PIL import Image
import os

input_path = 'F:\Desktop\deme'


def is_color_image(url):
    im = Image.open(url)
    pix = im.convert('RGB')
    width = im.size[0]
    height = im.size[1]
    oimage_color_type = "Grey Image"
    color_type = 1
    is_color = []
    for x in range(width):
        for y in range(height):
            r, g, b = pix.getpixel((x, y))
            r = int(r)
            g = int(g)
            b = int(b)
            if (r == g) and (g == b):
                pass
            else:
                oimage_color_type = 'Color Image'
                color_type = 0
    # print(oimage_color_type)
    return color_type
    # return oimage_color_type


if __name__ == '__main__':
    total_pics = os.listdir(input_path)
    count = 0
    for pic in total_pics:
        real_path = input_path + os.sep + pic
        if is_color_image(real_path):
            count += 1
            print(pic[:-4])
            # 删除xml文件
            # os.remove(xml_path + os.sep + pic[:-4] + '.xml')
            # 删除图片
            # os.remove(real_path)
    print(count)
