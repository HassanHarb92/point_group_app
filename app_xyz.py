import streamlit as st
from pyscf import gto

# Dictionary to look up atomic numbers for calculating the total electron count
atomic_numbers = {
    'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10, 
    'Na': 11, 'Mg': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18,
    # Add more elements as needed
}

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

# Function to determine the total number of electrons
def calculate_total_electrons(atoms):
    total_electrons = sum(atomic_numbers[atom] for atom in atoms)
    return total_electrons

# Function to automatically assign spin based on electron count
def determine_spin(total_electrons):
    if total_electrons % 2 == 0:
        return 0  # Singlet (spin = 0)
    else:
        return 1  # Doublet (spin = 1)

# Function to determine the point group using PySCF
def get_point_group(atoms, coords, total_electrons):
    # Automatically determine spin
    spin = determine_spin(total_electrons)
    
    mol = gto.Mole()
    mol.build(
        atom=[(atom, coord) for atom, coord in zip(atoms, coords)], 
        charge=0,  # Assuming neutral molecule for simplicity
        spin=spin,  # Spin automatically set based on electron count
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
    
    # Calculate the total number of electrons
    total_electrons = calculate_total_electrons(atoms)
    
    # Determine the point group using PySCF
    try:
        point_group = get_point_group(atoms, coords, total_electrons)
        # Display the result
        st.subheader("Point Group Result")
        st.write(f"The determined point group for the molecule is: **{point_group}**")
    except RuntimeError as e:
        st.error(f"An error occurred: {e}")

