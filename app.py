# http://127.0.0.1:5000

from flask import Flask, render_template_string, jsonify, redirect, url_for
import plotly.graph_objects as go
import plotly.utils
import numpy as np
import nibabel as nib
from skimage.measure import marching_cubes
import os
import json

app = Flask(__name__)

# 1 Configuration

TEST_DATA_DIR = "D:/MSc_Project/DATASET/BraTS2021_Training_Data"

CLASS_CONFIG = {
    1: {"name": "Necrotic Core", "color": "red", "opacity": 1.0},
    2: {"name": "Edema", "color": "green", "opacity": 0.3},
    4: {"name": "Enhancing Tumor", "color": "blue", "opacity": 0.5}
}

# 2 Helper Functions

def load_nifti_file(file_path):
    '''Loads a NIfTI file and returns the data and header info.'''

    try:
        nib_img = nib.load(file_path)
        data = nib_img.get_fdata()
        print(f"Loaded file: {os.path.basename(file_path)}. Shape: {data.shape}")
        return data, nib_img
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None, None
    

def generate_mesh(binary_mask, spacing, mesh_name="Mesh"):
    '''Generates a 3D mesh from a binary mask using Marching Cubes.'''  
    if not np.any(binary_mask):
        print(f"{mesh_name} is empty. Skipping mesh generation.")
        return None
    
    try:
        verts, faces, _, _ = marching_cubes(binary_mask, level=0.5, spacing=spacing)
        print(f"Mesh for '{mesh_name}' created with {len(verts)} vertices.")
        return {'vertices': verts, 'faces': faces}
    
    except Exception as e:
        print(f"Marching Cubes failed for {mesh_name}: {e}")
        return None
    
# Flask Web Routes

@app.route('/')
def index():
    '''Renders a homepage with a dropdown of patient IDs.'''
    try:
        patients = [p for p in os.listdir(TEST_DATA_DIR) if os.path.isdir(os.path.join(TEST_DATA_DIR, p))]
        return render_template_string("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Select Patient</title>
                <style>
                    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
                           display: flex; align-items: center; justify-content: center; height: 100vh;
                           background-color: #111; color: #eee; margin: 0; }
                    .container { text-align: center; background-color: #222; padding: 40px; border-radius: 10px; box-shadow: 0 0 20px rgba(0,0,0,0.5); }
                    h1 { margin-top: 0; }
                    select { width: 100%; padding: 10px; margin-bottom: 20px; border-radius: 5px; background-color: #333; color: #eee; border: 1px solid #444; }
                    button { padding: 10px 20px; font-size: 1em; color: white; background-color: #007bff; border: none; border-radius: 5px; cursor: pointer; }
                    button:hover { background-color: #0056b3; }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>3D Brain Tumor Visualizer</h1>
                    <form id="patient-form" target="_blank">
                        <select id="patient-select">
                            {% for patient in patients %}
                                <option value="{{ patient }}">{{ patient }}</option>
                            {% endfor %}
                        </select>
                        <button type="submit">Visualize</button>
                    </form>
                </div>
                <script>
                    const form = document.getElementById('patient-form');
                    const select = document.getElementById('patient-select');
                    form.addEventListener('submit', function(e) {
                        e.preventDefault();
                        const patientId = select.value;
                        form.action = `/plot/${patientId}`;
                        form.submit();
                    });
                </script>
            </body>
            </html>
        """, patients=sorted(patients))
    except FileNotFoundError:
            return "<h1>Error: Data directory not found.</h1><p>Please check the TEST_DATA_DIR path in app.py.</p>"


# Route for displaying the 3D plot in a new tab
@app.route('/plot/<patient_id>')
def plot(patient_id):
    '''Generates and displays the 3D plot for the selected patient.'''
    patient_folder = os.path.join(TEST_DATA_DIR, patient_id)

    # Load gorund truth and T1 scan
    gt_mask, gt_nib = load_nifti_file(os.path.join(patient_folder, f"{patient_id}_seg.nii.gz"))
    t1_scan, t1_nib = load_nifti_file(os.path.join(patient_folder, f"{patient_id}_t1.nii.gz"))

    if gt_mask is None or t1_scan is None:
        return f"<h1>Error: Could not load data for patient {patient_id}</h1><p>Ensure both _seg.nii.gz and _ti.nii.gz files exist.</p>"
    
    # Generate Meshes
    spacing = gt_nib.header.get_zooms()[:3]

    # Generate tumor mesh
    tumor_meshes = {}
    for label, config in CLASS_CONFIG.items():
        binary_mask = (gt_mask == label)
        tumor_meshes[label] = generate_mesh(binary_mask, spacing, mesh_name=config['name'])

    # Generate brain mesh 
    brain_binary_mask = t1_scan > 0
    brain_mesh = generate_mesh(brain_binary_mask, spacing, mesh_name='Brain')

    # Create a PlotLy figure
    plot_traces = []
    lighting_effects = dict(ambient=0.6, diffuse=1.0, specular=0.3, roughness=0.5, fresnel=0.2)

    # Add brain mesh first, so it is in the background
    if brain_mesh:
        trace = go.Mesh3d(
            x=brain_mesh['vertices'][:,0], y=brain_mesh['vertices'][:,1], z=brain_mesh['vertices'][:,2],
            i=brain_mesh['faces'][:,0], j=brain_mesh['faces'][:,1], k=brain_mesh['faces'][:,2],
            color='gray', opacity=0.2, # Semi-transparent gray for the brain
            lighting=lighting_effects,
            name='Brain'
        )

        plot_traces.append(trace)

    # Add tumor
    for label, config in CLASS_CONFIG.items():
        if tumor_meshes.get(label):
            mesh_data = tumor_meshes[label]
            trace = go.Mesh3d(
                x=mesh_data['vertices'][:,0], y=mesh_data['vertices'][:,1],z=mesh_data['vertices'][:,2],
                i=mesh_data['faces'][:,0],j=mesh_data['faces'][:,1], k=mesh_data['faces'][:,2],
                color=config['color'], opacity=config['opacity'],
                lighting=lighting_effects, lightposition=dict(x=100, y=200, z=50),
                name=config['name'], hoverinfo='name'
            )
            plot_traces.append(trace)

    fig = go.Figure(data=plot_traces)

    # Layout

    buttons = []
    num_tumor_traces = len(plot_traces) - (1 if brain_mesh else 0)

    visibility_all = [True] * len(plot_traces)
    buttons.append(dict(label="Show All", method="update", args=[{"visible": visibility_all}]))

    visibility_tumor_only = [False] + [True] * num_tumor_traces if brain_mesh else [True] * num_tumor_traces
    buttons.append(dict(label="Tumor Only", method="update", args=[{"visible": visibility_tumor_only}]))

    for i, trace in enumerate(plot_traces):
        visibility = [False] * len(plot_traces)
        visibility[i] = True
        buttons.append(dict(label=trace.name, method="update", args=[{"visible": visibility}]))

    fig.update_layout(
        title_text=f"3D Tumor Visualization: {patient_id}",
        updatemenus=[
            dict(
                type="buttons", direction="right",
                x=0.5, xanchor="center", y=1.15, yanchor="top",
                buttons=buttons,
                bgcolor='white', font=dict(color='black'), bordercolor='black'
            )
        ],
        scene=dict(
            xaxis=dict(showticklabels=False, title=dict(text='X', font=dict(color='white'))),
            yaxis=dict(showticklabels=False, title=dict(text='Y', font=dict(color='white'))),
            zaxis=dict(showticklabels=False, title=dict(text='Z', font=dict(color='white'))),
            camera_eye=dict(x=1.8, y=1.8, z=1.8),
            bgcolor='rgb(17, 17, 17)',
        ),
        legend=dict(bgcolor='rgba(0,0,0,0.5)', bordercolor='rgba(255,255,255,0.2)', font=dict(color='white')),
        margin=dict(l=0, r=0, b=0, t=40),   
        paper_bgcolor='rgb(17, 17, 17)',
        font=dict(color='white')

    )

    plot_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
    return render_template_string("""
            <!DOCTYPE html>
            <html>
                <head>
                    <title>3D Plot: {{ patient_id }}</title>
                    <style> body { margin: 0; padding: 0; background-color: rgb(17, 17, 17); } </style>
                </head>
                <body>
                    {{ plot_html | safe }}
                </body>
            </html>
    """, plot_html=plot_html, patient_id=patient_id)


# Run the application

if __name__ == '__main__':
    app.run(debug=True)
            




    
































