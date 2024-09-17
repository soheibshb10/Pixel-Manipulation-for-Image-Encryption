from PIL import Image
import numpy as np
import base64
import argparse
import sys


def transferToBase64(img):
    image_array = np.array(img)
    image_bytes = image_array.tobytes()
    base64_encoded = base64.b64encode(image_bytes)
    print("encode base64:",base64_encoded)
    # return base64_encoded  # This returns the Base64 encoded data as bytes

def transertoBytes(img):
    image_array=np.array(img)
    image_bytes=image_array.tobytes()
    base64_string=base64.b64decode(image_bytes)
    print("decoded base64:",base64_string)

    




def encrypt_image(input_path, output_path, key):
    # Open the image file
    img = Image.open(input_path)
    
    img = img.convert('RGBA')
    
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            pixel = pixels[i, j]  # Get the pixel value (a tuple)
            
            if len(pixel) == 3:  # RGB
                r, g, b = pixel
                swapped_pixel = (b, g, r)  # Swap red and blue channels
            elif len(pixel) == 4:  # RGBA
                r, g, b, a = pixel
                swapped_pixel = (b, g, r, a)  # Swap red and blue channels, keep alpha
            
            # Assign the new pixel value back
            pixels[i, j] = swapped_pixel
    transferToBase64(img)
    # Save the modified image
    print("image:",img.load())
    img.save(output_path)
    print("Image encrypted successfully")


def decrypt_image(input_path, output_path, key):
    # Open the image file
    img = Image.open(input_path)
    
    img = img.convert('RGBA')
    
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            pixel = pixels[i, j]  # Get the pixel value (a tuple)
            
            if len(pixel) == 3:  # RGB
                r, g, b = pixel
                swapped_pixel = (b, g, r)  # Swap red and blue channels
            elif len(pixel) == 4:  # RGBA
                r, g, b, a = pixel
                swapped_pixel = (b, g, r, a)  # Swap red and blue channels, keep alpha
            
            # Assign the new pixel value back
            pixels[i, j] = swapped_pixel
    transertoBytes(img)
    # Save the modified image
    print("image:",img.load())
    img.save(output_path)
    print("Image decrypted successfully")


def main():
    parser = argparse.ArgumentParser(description='Image Encryption using Pixel Manipulation')
    parser.add_argument('--input_path', required=True, help='image path')
    parser.add_argument('--output_path', required=True, help='encrypted image path')
    parser.add_argument('--option', required=True, help='encrypted image path')

    try:
        args = parser.parse_args()
    except SystemExit as e:
        print("Error: Missing required arguments.")
        parser.print_help()
        sys.exit(2)
    if args.option=='1':
       encrypt_image(args.input_path, args.output_path, None)
    elif args.option=='2':
        decrypt_image(args.input_path,args.output_path,None)
        

if __name__ == '__main__':
    main()




# encrypt_image("images/test.png","images/encrypted.png",None)




