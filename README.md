# Image Encryption and Decryption Script
## Overview

This script performs basic encryption and decryption on image files by manipulating pixel values. The encryption process swaps the red and blue channels of each pixel, while the decryption process reverses this operation. Additionally, the script includes functionality to encode image data to Base64 and decode Base64 data back into bytes, though this part is currently used for demonstration purposes.
Features

    Encrypt images by swapping red and blue color channels.
    Decrypt images by reversing the color channel swap.
    Encode image data to Base64.
    Decode Base64 data back to image bytes.

Requirements

    Python 3.x
    Pillow (PIL) library
    NumPy library

You can install the required libraries using:

bash

pip install pillow numpy

How to Use

    Save the Script

    Save the provided script into a file, e.g., image_encryption.py.

    Run the Script

    Use the command line to execute the script with the necessary arguments. The script requires three arguments:
        --input_path: Path to the input image file.
        --output_path: Path where the encrypted or decrypted image will be saved.
        --option: 1 for encryption or 2 for decryption.

    Example command for encryption:

    bash

python image_encryption.py --input_path path/to/input/image.png --output_path path/to/output/encrypted_image.png --option 1

Example command for decryption:

bash

    python image_encryption.py --input_path path/to/encrypted_image.png --output_path path/to/output/decrypted_image.png --option 2

Example Usage
Encrypting an Image

bash

python image_encryption.py --input_path images/test.png --output_path images/encrypted.png --option 1

Decrypting an Image

bash

python image_encryption.py --input_path images/encrypted.png --output_path images/decrypted.png --option 2

Script Details

    Imports:
        from PIL import Image: For image processing.
        import numpy as np: For converting image to byte array.
        import base64: For encoding and decoding Base64 data.
        import argparse: For command-line argument parsing.
        import sys: For handling system-specific parameters and functions.

    Functions:
        transferToBase64(img): Converts an image to a Base64 encoded string.
        transertoBytes(img): Decodes a Base64 string back into image bytes (currently for demonstration purposes).
        encrypt_image(input_path, output_path, key): Encrypts an image by swapping red and blue color channels.
        decrypt_image(input_path, output_path, key): Decrypts an image by reversing the red and blue channel swap.
        main(): Parses command-line arguments and calls the appropriate function based on the option provided.

    Note:
        The key parameter is not used in the current version of the script but is included for potential future extensions.
