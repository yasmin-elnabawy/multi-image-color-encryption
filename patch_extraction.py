from PIL import Image
import numpy as np
import os

def patch_extraction_proc(image_size,patch_size,num_img,input_folder):
    num_patches_per_image = (image_size // patch_size) ** 2  # 4 patches per image
    # Assuming you have a list of 32 image filenames, you can loop through them
    image_filenames = []  # List of your 32 image filenames
    for i in range(num_img):
        image_filenames.append(f'{input_folder}/{i+1}.png')
        # List to store all patches
        # all_patches = []
    # Counter for unique filenames
    patch_counter = 1
    for filename in image_filenames:
        img = Image.open(filename)
        
        # Extract patches from the image
        for i in range(image_size // patch_size):
            for j in range(image_size // patch_size):
                # Calculate the top-left corner of the patch
                left = j * patch_size
                top = i * patch_size
                right = left + patch_size
                bottom = top + patch_size
                
                # Crop the patch
                patch = img.crop((left, top, right, bottom))

                # Generate filename for the patch
                patch_filename = os.path.join('patches/', f"{patch_counter}.png")

                # Save the patch
                patch.save(patch_filename)

                # Increment patch counter
                patch_counter += 1

    print("All patches saved successfully.")
