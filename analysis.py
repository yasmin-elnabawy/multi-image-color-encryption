import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import entropy

def histogram(img,color):
    plt.hist(img.flatten(), bins=256, color=color,alpha=0.7)  # Adjust bins as needed
    plt.xlabel('Value',fontweight='bold')
    plt.ylabel('Frequency',fontweight='bold')
    plt.title('Histogram of 1D Array',fontweight='bold')
    plt.xticks(fontweight='bold')
    plt.yticks(fontweight='bold')
    plt.grid(False)
    plt.show()


def entropy_analysis(img):
    # Flatten the image to 1D array
    flattened_image = img.flatten()
    # Compute the histogram (counts of each unique pixel value)
    histogram, bin_edges = np.histogram(flattened_image, bins=256, range=(0, 255), density=True)
    # Calculate entropy
    entropy_value = entropy(histogram, base=2)
    entropy_value_rounded = round(entropy_value, 4)
    return entropy_value_rounded