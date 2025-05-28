
# Enhanced Multiple Color Image Encryption Utilizing 3D Chaotic Maps with Iterative Sub-image Randomization and Fusion

This repository contains the official implementation of the encryption algorithm proposed in the paper:

**"Enhanced Multiple Color Image Encryption Utilizing 3D Chaotic Maps with Iterative Sub-image Randomization and Fusion"**  
*by Khalid M. Hosny, Yasmin M. Elnabawy, Ahmed M. Elshewey, and Rania A. Salama*  
Submitted to *The Visual Computer* (Springer).

---

## 🔍 Overview

This project presents a multiple color image encryption technique that combines:
- 3D chaotic maps for generating complex pseudo-random sequences,
- Iterative sub-image randomization,
- A fusion technique to securely handle multiple RGB images simultaneously.

The code enables both encryption and decryption with full control over channels, patches, and chaotic behavior.

---

## 📁 Directory Structure

```
├── Main.ipynb                         # Jupyter notebook example
├── encryption.py                      # Main encryption module
├── decryption.py                      # Main decryption module
├── chaotic_maps.py                    # Implementation of chaotic maps
├── patch_extraction.py                # Extract sub-image patches
├── patches_reordering.py              # Reorder patches
├── reverse_patches_reordering.py      # Recover original patch order
├── transformation.py                  # Patch transformations
├── im512/                             # Input RGB images (512x512)
├── output_patches_R/                  # Red channel output
├── output_patches_G/                  # Green channel output
├── output_patches_B/                  # Blue channel output
```

---

## ⚙️ Requirements

Install the dependencies with:

```bash
pip install numpy opencv-python matplotlib scikit-image
```

Tested with Python 3.8+

---

## 🚀 How to Run

### Option 1: Jupyter Notebook
Run the `Main.ipynb` file to see a full pipeline from encryption to decryption.

### Option 2: Command Line

```bash
python encryption.py
python decryption.py
```

Make sure your input images are located in the `im512/` directory.

---

## 📌 Citation

If you use this code, please cite:

```
Khalid M. Hosny, Yasmin M. Elnabawy, Ahmed M. Elshewey, Rania A. Salama,
"Enhanced Multiple Color Image Encryption Utilizing 3D Chaotic Maps with Iterative Sub-image Randomization and Fusion",
The Visual Computer, Springer, 2025.
```

---

## 🔗 Permanent Archive

The source code will be archived via Zenodo with a DOI upon paper acceptance. The GitHub repository will also remain accessible.

---

## 📬 Contact

For questions or feedback, please contact:  
**Khalid M. Hosny**  
Email: k_hosny@zu.edu.eg

**Yasmin M. Elnabawy**
Email: yasmin.el-nabawy@fci.suezuni.edu.eg
