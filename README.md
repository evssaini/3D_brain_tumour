# 🧠 3D brain tumour segmentation and visualisation for improved clinical understanding

## 📌 Overview

The project addresses the challenge of making segmentation outputs more interpretable and clinically useful through advanced visualisation techniques. A 3D U-Net was trained on the BraTS2021 multimodal MRI dataset to segment gliomas and their subregions, forming the foundation for a visual explanation. Incorporate Grad-CAM heatmaps to highlight spatial regions influencing predictions, voxel-level Softmax probability maps to show class confidence, and Monte Carlo Dropout-based variance maps to quantify uncertainty, and an interactive 3D web application to visualise the tumour section using the Marching Cubes algorithm, allowing clinicians to explore tumour morphology, assess model confidence, and understand the prediction rationale. This work demonstrates that visualising predictions, uncertainty, and network attention can bridge the gap between deep learning performance and clinical interpretability, supporting more informed decision-making in neuro-oncology.


For more detailed understanding, Medium: https://medium.com/@ershveers/3d-brain-tumour-segmentation-and-visualisation-for-improved-clinical-understanding-98ad5168f015




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

## 📈 Results

1. Example of tumour segmentation on axial slices [0,31,63,95,127]. Rows show MRI modalities (T1ce, FLAIR, T2), ground truth masks, and predicted masks. Colour representation- purple: background; blue: necrotic core; green: edema; yellow: enhancing tumour.
   
   <img width="1657" height="1618" alt="combined_visualization_axial" src="https://github.com/user-attachments/assets/0b0c8ce9-18e8-495a-9227-30433905a105" />

2. Grad-CAM Heatmap, for each class (Necrotic core, Edema, Tumour, and Enhancing Tumor), row-wise respectively, showing 5 slices [0,31,63,95,127], column-wise, for the axial plane, slice 95 shows the best tumour view, highlights the regions most important for the model’s prediction by weighting feature maps with their gradients. Brighter areas in the heatmap show regions that contributed more strongly to the chosen class.
   
   <img width="1799" height="922" alt="gradcam_heatmaps_axial" src="https://github.com/user-attachments/assets/8199fb00-f4d3-4009-9350-01624a03bf28" />
   

3.  Softmax Probability Map, for each class (Background, Necrotic core, Edema, and Enhancing Tumor), row-wise respectively, showing 5 slices [0,31,63,95,127], column-wise, for the axial plane, slice 95 shows the best tumour view, bright regions (yellow) represent high probability and strong model confidence, while darker regions (black) indicate lower probability and greater uncertainty about voxel belongs to that class.
   
   <img width="1799" height="1229" alt="softmax_probabilities_axial" src="https://github.com/user-attachments/assets/2415f2c4-f0d9-478c-9692-45ec39aaa443" />
   

4. Monte Carlo Uncertainty Map, for each class (Necrotic core, Edema, and Enhancing Tumor), row-wise respectively, showing 5 slices [0,31,63,95,127], column-wise, for the axial plane, slice 95 shows the best tumour view, brighter regions indicate high variance, where the model’s predictions fluctuate across runs, reflecting greater uncertainty. This is most visible near tumour boundaries, where tissue transitions are naturally ambiguous.
   
   <img width="1799" height="922" alt="uncertainty_heatmaps_axial" src="https://github.com/user-attachments/assets/adbe47bb-abcc-4472-a7c5-c998bd3f454d" />

5.  Whole 3D brain-tumour mesh of patient ID: BraTS2021 00281, with different functionalities (buttons, on top)

   <img width="1805" height="520" alt="Screenshot 2025-07-31 182820" src="https://github.com/user-attachments/assets/27016970-99b4-4cc1-b321-80dda621dde3" />

   <img width="690" height="539" alt="Screenshot 2025-07-31 182830" src="https://github.com/user-attachments/assets/ef4c3827-7e23-4af9-813f-5809486470e7" />







## 📈 Learning Outcomes
1. Applied deep learning to a real-world medical imaging problem.
2. Gained experience with 3D data reconstruction and visualisation.
3. Strengthened understanding of AI workflows in healthcare.
4. Improved skills in Python-based machine learning pipelines.

## 🔮 Future Improvements
1. Integration of advanced segmentation models.
2. Interactive 3D visualisation.
3. Deployment as a lightweight web.






