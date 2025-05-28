import numpy as np

# Decryption Section

def reverse_patches_reordering_process(image, chaotic_sequence):
    """
    Permutes a 3D image cube slice-wise along a given chaotic sequence.
    
    Args:
    - image: 3D NumPy array representing the image cube (depth, height, width).
    - chaotic_sequence: List or array of indices for permutation.
    
    Returns:
    - Permuted 3D image cube.
    - Original permutation order (for reversal).
    """
    # Get the depth (number of slices) of the image cube
    depth = image.shape[0]
    
    # Convert chaotic sequence to indices within valid range
    permuted_order = np.array(chaotic_sequence) * depth
    permuted_order = (permuted_order % depth).astype(int)
    
    # Apply the permutation to reorder the slices along the z-axis
    for i in reversed(range(depth)):
        if i != permuted_order[i]:
            t = np.copy(image[i,:,:])
            image[i,:,:] = np.copy(image[permuted_order[i],:,:])
            image[permuted_order[i],:,:] = np.copy(t)
    
    return image, permuted_order

def rotate_minus_90_x(rotated_image):
    """
    Reverses the rotation of a 3D image cube by -90 degrees along the x-axis.
    
    Args:
    - rotated_image: Rotated 3D NumPy array representing the image cube (depth, height, width).
    
    Returns:
    - Original 3D image cube before rotation.
    """
    original_image = np.rot90(rotated_image, -1, axes=(1, 2))  # Rotate back by -90 degrees along x-axis
    return original_image


def rotate_minus_90_y(rotated_image):
    """
    Reverses the rotation of a 3D image cube by -90 degrees along the x-axis.
    
    Args:
    - rotated_image: Rotated 3D NumPy array representing the image cube (depth, height, width).
    
    Returns:
    - Original 3D image cube before rotation.
    """
    original_image = np.rot90(rotated_image, -1, axes=(0, 2))  # Rotate back by -90 degrees along x-axis
    return original_image
