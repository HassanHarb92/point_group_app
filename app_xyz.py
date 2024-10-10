import streamlit as st
from pyscf import gto

# Function to parse XYZ file and return atom symbols and coordinates
def read_xyz(file_path):
    atoms = []
    coordinates = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines[2:]:  # Skip the first two lines (header)
            parts = line.split()
            atoms.append(parts[0])
            coordinates.append([float(parts[1]), float(parts[2]), float(parts[3])])
    
    return atoms, coordinates

# Function to determine the point group using PySCF
def get_point_group(atoms, coords):
    mol = gto.Mole()
    mol.build(
        atom=[(atom, coord) for atom, coord in zip(atoms, coords)], 
        symmetry=True
    )
    return mol.topgroup

st.title("Point Group Symmetry Determiner from XYZ")

# Allow user to upload an XYZ file
uploaded_file = st.file_uploader("Upload an XYZ file", type=["xyz"])

if uploaded_file:
    # Save the uploaded file
    with open("uploaded_molecule.xyz", "wb") as f:
        f.write(uploaded_file.getvalue())
    
    # Read the uploaded XYZ file
    atoms, coords = read_xyz("uploaded_molecule.xyz")
    
    # Determine the point group using PySCF
    point_group = get_point_group(atoms, coords)
    
    # Display the result
    st.subheader("Point Group Result")
    st.write(f"The determined point group for the molecule is: **{point_group}**")

