The project addresses the challenge of making segmentation outputs more interpretable and clinically useful through advanced visualization techniques. A 3D U-Net was trained on the BraTS2021 multimodal MRI dataset to segment gliomas and their subregions, forming the foundation for a visual explanation. Incorporate Grad-CAM heatmaps to highlight spatial regions influencing predictions, voxel-level Softmax probability maps to show class confidence, and Monte Carlo Dropout-based variance maps to quantify uncertainty, and an interactive 3D web application to visualise the tumor section using the Marching Cubes algorithm, allowing clinicians to explore tumor morphology, assess model confidence, and understand the prediction rationale. This work demonstrates that visualising predictions, uncertainty, and network attention can bridge the gap between deep learning performance and clinical interpretability, supporting more informed decision-making in neuro-oncology.



Steps to create a virtual environment to run the 3D mesh web application file (app.py) on your machine (Windows).
1.	Open Command Prompt and navigate to the folder where the project is stored. This ensures that the virtual environment folder is created alongside the project file.
For example:
D:
cd MSc_Project\CODE

2.	Create the virtual environment, use pythons built in ‘venv’ module to create a new isolated environment and make sure you have latest python version.

For example:
python -m venv myenv

3.	Activate the environment

For example:
myenv\Scripts\activate

4.	Install necessary libraries
pip install --upgrade "itkwidgets[lab]" torch numpy nibabel scikit-image ipywidgets zarr jupyterlab ipykernel

5.	Link environment to Jupyter, use ipykernel to install a new ‘kernel’
python -m ipykernel install --user --name=myenv --display-name="Python (My MSc Project)"

6.	Launch and select kernel, launch JupyterLab and, within the notebook, change the kernel to ‘Python (My MSc Project)’, to ensure the notebook runs in correct, isolated environment.


Steps to run the 3D brain tumor segmentation file (3D_Tumor_Seg.ipynb) on google colab.
1.	Download the dataset (BraTS2021 dataset)
Link: https://www.cancerimagingarchive.net/analysis-result/rsna-asnr-miccai-brats-2021/
You might need to download IBM aspera connect plugin for faster download, it is available in the link above.
 

This is the image for reference, you must click on this button to get the dataset.
And then upload the dataset in google drive.

2.	Mount your google drive with google colab.
a.	from google.colab import drive
b.	drive.mount('/content/drive')

This is the code to mount your drive.

3.	You might to change the folder/file directories in the file wrt your drive folder structure(where you stored your BraTS2021 dataset).
4.	You have to create some directories before running the data split code so that the images/mask, and train – validation and test sets are stores properly.
5.	A folder called ‘Checkpoints’, where the saved model weights are present, can be used to run the test model, unless one wants to train the model again.



