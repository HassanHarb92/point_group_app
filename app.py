import streamlit as st

def determine_point_group(is_linear, has_inversion_center, num_rotation_axes, has_reflection_planes):
    """Determines the point group based on the user inputs."""
    
    if is_linear:
        if num_rotation_axes == 1:
            return "C∞v"  # Linear molecules with a single rotation axis
        else:
            return "D∞h"  # Linear molecules with two or more rotation axes
    else:
        if has_inversion_center:
            if num_rotation_axes == 0:
                return "Ci"  # Molecule with inversion center but no other symmetry
            elif num_rotation_axes == 1:
                if has_reflection_planes:
                    return "C2h"  # One C2 axis with inversion center and reflection plane
                else:
                    return "C2i"  # One C2 axis with inversion center but no reflection plane
            elif num_rotation_axes > 1:
                return "Oh"  # High symmetry (octahedral)
        else:
            if num_rotation_axes == 0 and has_reflection_planes:
                return "Cs"  # Reflection plane only
            elif num_rotation_axes == 1:
                return "C2v"  # One C2 axis with reflection planes
            elif num_rotation_axes == 2:
                return "D2h"  # Two C2 axes with reflection planes
            else:
                return "Unknown symmetry group"

# Streamlit app interface

st.title("Point Group Symmetry Identifier")

st.write("Welcome to the point group identifier! Please answer the following questions about the molecular structure.")

# Ask questions
is_linear = st.radio("Is the molecule linear?", ("Yes", "No")) == "Yes"
has_inversion_center = st.radio("Does the molecule have an inversion center?", ("Yes", "No")) == "Yes"
num_rotation_axes = st.slider("How many rotation axes (Cn) does the molecule have?", 0, 3, 0)
has_reflection_planes = st.radio("Does the molecule have reflection planes?", ("Yes", "No")) == "Yes"

# Determine the point group
point_group = determine_point_group(is_linear, has_inversion_center, num_rotation_axes, has_reflection_planes)

# Display the result
st.subheader("Point Group Result")
st.write(f"The determined point group for the molecule is: **{point_group}**")

