import numpy as np
import cv2


def cube_transformation(patch_size):
    cube_R = np.zeros((patch_size, patch_size, patch_size), dtype=np.uint8)
    cube_G = np.zeros((patch_size, patch_size, patch_size), dtype=np.uint8)
    cube_B = np.zeros((patch_size, patch_size, patch_size), dtype=np.uint8)
    for i in range(patch_size):
        # Construct the filename of the patch
        patch_filename = f"patches/{i+1}.png"  # adjust the path as necessary
        # Read the patch using OpenCV
        patch = cv2.imread(patch_filename, 1)
        patchB,patchG,patchR = cv2.split(patch)
        # Insert the patch into the cube at the corresponding position
        z_position = i  # assuming patches are stacked along the z-axis
        cube_R[z_position, :, :] = patchR
        cube_G[z_position, :, :] = patchG
        cube_B[z_position, :, :] = patchB
    return cube_R, cube_G, cube_B
