import argparse
import os
from PIL import Image, ImageEnhance, ImageFilter


def main():

    #ALL  FUNCTIONS
    def pixel(src):
        img = Image.open('%s'%(src))

        # dict_intensity = { 5 : 16, 4 : 32, 3 : 64, 2 : 128, 1 : 256 }

        # small_IMG = img.resize((dict_intensity.get(intensity),dict_intensity.get(intensity)),Image.BILINEAR)
        small_IMG = img.resize((64,64),Image.BILINEAR)
        result = small_IMG.resize(img.size,Image.NEAREST)

        result_path = os.path.dirname(src)
        str(result_path)
        result_path = (result_path+'\\')
        result.save(result_path+'pixelated.png')
        print('Image saved at : '+result_path+'pixelated.png')

    def black_white(src):
        img = Image.open('%s'%(src))
        img = img.convert('1')
        result_path = os.path.dirname(src)
        str(result_path)
        result_path = (result_path+'\\')
        img.save(result_path+'black_white.png')
        print('Image saved at : '+result_path+'black_white.png')

    def blur(src):
        intensity = 4
        img = Image.open('%s'%(src))
        result = img.filter(ImageFilter.MinFilter(intensity))

        result_path = os.path.dirname(src)
        str(result_path)
        result_path = (result_path+'\\')
        result.save(result_path+'blur.png')
        print('Image saved at : '+result_path+'blur.png')

    def blur_edge(src):
        radius, diameter = 20, 30
        
        img = Image.open('%s'%(src))
        
        background_size = (img.size[0] + diameter, img.size[1] + diameter)
        background = Image.new('RGB', background_size, (255, 255, 255))
        background.paste(img, (radius, radius))
        
        mask_size = (img.size[0] + diameter, img.size[1] + diameter)
        mask = Image.new('L', mask_size, 255)
        black_size = (img.size[0] - diameter, img.size[1] - diameter)
        black = Image.new('L', black_size, 0)

        mask.paste(black, (diameter, diameter))
        
        blur = background.filter(ImageFilter.GaussianBlur(radius / 2))
        background.paste(blur, mask=mask)


        # result = background.save("blur_edge.png", quality=100)

        result_path = os.path.dirname(src)
        str(result_path)
        result_path = (result_path+'\\')
        background.save(result_path+'bluredge.png')
        print('Image saved at : '+result_path+'bluredge.png')

    def gen_thumbnail(src):
        width, height = 200,200
        img = Image.open('%s'%(src))
        
        size = (width, height)
        
        img.thumbnail(size)

        result_path = os.path.dirname(src)
        str(result_path)
        result_path = (result_path+'\\')
        img.save(result_path+'thumbnail.png')
        print('Image saved at : '+result_path+'thumbnail.png')

    # Arguments to be passed
    parser = argparse.ArgumentParser(description= 'PIE can help with Imaging Effects')

    parser.add_argument('-pixelate','-p' ,dest= 'pixel', help= 'Pixelates the image!')

    parser.add_argument('-black_white','-bg', dest= 'blackwhite' , help= 'Decolourises the image!')

    parser.add_argument('-blur','-b', dest= 'blur' , help= 'Blurs the image!')

    parser.add_argument('-bluredge','-be', dest= 'bluredge' , help= 'Blurs the edges of the image!')

    parser.add_argument('-thumbnail','-tn', dest= 'thumbnail' , help= 'Creates a Thumbnail of the image!')

    args = parser.parse_args()


    if args.blackwhite:
        black_white(args.blackwhite)
    if  args.pixel:
        pixel(args.pixel)
    if args.blur:
        blur(args.blur)
    if args.bluredge:
        blur_edge(args.bluredge)
    if args.thumbnail:
        gen_thumbnail(args.thumbnail)


if __name__ == "__main__":
    main()