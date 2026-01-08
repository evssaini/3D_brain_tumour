# 🧠 3D brain tumour segmentation and visualisation for improved clinical understanding

## 📌 Overview

The project addresses the challenge of making segmentation outputs more interpretable and clinically useful through advanced visualisation techniques. A 3D U-Net was trained on the BraTS2021 multimodal MRI dataset to segment gliomas and their subregions, forming the foundation for a visual explanation. Incorporate Grad-CAM heatmaps to highlight spatial regions influencing predictions, voxel-level Softmax probability maps to show class confidence, and Monte Carlo Dropout-based variance maps to quantify uncertainty, and an interactive 3D web application to visualise the tumour section using the Marching Cubes algorithm, allowing clinicians to explore tumour morphology, assess model confidence, and understand the prediction rationale. This work demonstrates that visualising predictions, uncertainty, and network attention can bridge the gap between deep learning performance and clinical interpretability, supporting more informed decision-making in neuro-oncology.


For better understanding, Medium: https://medium.com/@ershveers/3d-brain-tumour-segmentation-and-visualisation-for-improved-clinical-understanding-98ad5168f015




## 🛠️ Key Features
1. Preprocessing of brain MRI scans for tumour analysis.
2. Deep learning based tumour segmentation.
3. 3D reconstruction of tumour regions from segmented slices.
4. Visualisation of tumour volume and structure.
5. Modular and extensible codebase for experimentation and research.

## 🧩 Project Workflow
1. Input Data - MRI brain scans.
2. Preprocessing - Normalisation and preparation of imaging data.
3. Segmentation - Deep learning model identifies tumour regions.
4. 3D Reconstruction - Tumour volume reconstructed from segmented slices.
5. Visualisation - 3D tumour representation for analysis.

## ⚙️ Technologies Used
1. Python
2. PyTorch
3. NumPy
4. Matplotlib
5. scikit-image
6. Medical image processing techniques
7. Deep Learning
8. Computer Vision

## 🚀 Installation

Install dependecies:
```python
pip install -r requirements.txt
```

## ▶️ Usage
1. Add MRI scan data to the directory.
2. Run the preprocessing and segmentation scripts as outlined in the repository.
3. Execute the reconstruction module to generate a 3D tumour model.
4. Visualise the output using the provided visualisation scripts.
(Note: Sample datasets are not included due to size and licensing constraints.)

## 📈 Learning Outcomes
1. Applied deep learning to a real-world medical imaging problem.
2. Gained experience with 3D data reconstruction and visualisation.
3. Strengthened understanding of AI workflows in healthcare.
4. Improved skills in Python-based machine learning pipelines.

## 🔮 Future Improvements
1. Integration of advanced segmentation models.
2. Interactive 3D visualisation.
3. Deployment as a lightweight web.






