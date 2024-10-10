
import streamlit as st

# Function to determine point group based on flowchart logic
def determine_point_group(is_linear, has_inversion_center, has_multiple_rotation_axes, has_c5, highest_cn, has_perpendicular_cn2, has_horizontal_plane, has_sigma_v, has_s2n):
    """Determines the point group based on the answers from the user."""
    
    if is_linear:
        if has_inversion_center:
            return "D∞h"
        else:
            return "C∞v"
    else:
        if has_multiple_rotation_axes:
            if has_inversion_center:
                if has_c5:
                    return "Ih"  # Icosahedral group
                else:
                    return "Oh"  # Octahedral group
            else:
                return "Td"  # Tetrahedral group
        else:
            if has_inversion_center:
                if highest_cn == 1:
                    return "Ci"  # Inversion center only
                elif highest_cn == 2:
                    if has_perpendicular_cn2:
                        return "Dnh"
                    else:
                        return "Dnd"
                else:
                    return "Dnh"  # General case for Dnh
            else:
                if highest_cn == 1:
                    if has_horizontal_plane:
                        return "Cs"  # Reflection plane only
                    else:
                        return "C1"  # No symmetry elements
                elif highest_cn == 2:
                    if has_horizontal_plane:
                        return "C2h"  # C2 axis and horizontal plane
                    else:
                        return "C2v"  # C2 axis and vertical planes
                elif has_s2n:
                    return "S2n"
                else:
                    return "Cn"

# Streamlit app interface

st.title("Point Group Symmetry Identifier")

st.write("Answer the questions below to determine the point group of the molecule:")

# Ask questions based on the flowchart
is_linear = st.radio("Is the molecule linear?", ("Yes", "No")) == "Yes"

if is_linear:
    has_inversion_center = st.radio("Does the molecule have an inversion center?", ("Yes", "No")) == "Yes"
    point_group = determine_point_group(is_linear, has_inversion_center, None, None, None, None, None, None, None)
else:
    has_multiple_rotation_axes = st.radio("Does the molecule have two or more rotation axes (Cn, n > 2)?", ("Yes", "No")) == "Yes"
    
    if has_multiple_rotation_axes:
        has_inversion_center = st.radio("Does the molecule have an inversion center?", ("Yes", "No")) == "Yes"
        if not has_inversion_center:
            has_c5 = st.radio("Does the molecule have a C5 axis?", ("Yes", "No")) == "Yes"
        point_group = determine_point_group(is_linear, has_inversion_center, has_multiple_rotation_axes, has_c5, None, None, None, None, None)
    else:
        has_inversion_center = st.radio("Does the molecule have an inversion center?", ("Yes", "No")) == "Yes"
        highest_cn = st.slider("What is the highest rotation axis (Cn)?", 1, 6, 1)
        has_perpendicular_cn2 = st.radio("Is there a perpendicular C2 axis to the highest Cn?", ("Yes", "No")) == "Yes"
        has_horizontal_plane = st.radio("Does the molecule have a horizontal reflection plane (σh)?", ("Yes", "No")) == "Yes"
        has_sigma_v = st.radio("Does the molecule have vertical reflection planes (σv)?", ("Yes", "No")) == "Yes"
        has_s2n = st.radio("Does the molecule have improper rotation (S2n)?", ("Yes", "No")) == "Yes"
        
        point_group = determine_point_group(is_linear, has_inversion_center, has_multiple_rotation_axes, None, highest_cn, has_perpendicular_cn2, has_horizontal_plane, has_sigma_v, has_s2n)

# Display the result
st.subheader("Point Group Result")
st.write(f"The determined point group for the molecule is: **{point_group}**")

