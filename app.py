import streamlit as st

# Function to determine point group based on new flowchart logic
def determine_point_group(is_high_symmetry, highest_cn, has_perpendicular_c2, has_horizontal_plane, has_vertical_plane, has_improper_rotation):
    """Determines the point group based on the flowchart logic."""
    
    if is_high_symmetry:
        if has_perpendicular_c2:
            return f"D{highest_cn}h" if has_horizontal_plane else f"D{highest_cn}d" if has_vertical_plane else f"D{highest_cn}"
        else:
            return "Td, Oh, Ih, C∞v, D∞h"  # High symmetry molecules
    else:
        if highest_cn == 1:
            return "C1"  # Low symmetry
        elif highest_cn > 1:
            if has_perpendicular_c2:
                if has_horizontal_plane:
                    return f"D{highest_cn}h"
                elif has_vertical_plane:
                    return f"D{highest_cn}d"
                else:
                    return f"D{highest_cn}"
            else:
                if has_horizontal_plane:
                    return f"C{highest_cn}h"
                elif has_vertical_plane:
                    return f"C{highest_cn}v"
                elif has_improper_rotation:
                    return f"S{2 * highest_cn}"
                else:
                    return f"C{highest_cn}"

# Streamlit app interface

st.title("Point Group Symmetry Identifier")

st.write("Answer the questions below to determine the point group of the molecule:")

# Ask if the molecule has high or low symmetry
is_high_symmetry = st.radio("Is the molecule of high symmetry?", ("Yes", "No")) == "Yes"

if not is_high_symmetry:
    highest_cn = st.slider("What is the highest order rotation axis (Cn)?", 1, 6, 1)
    
    if highest_cn > 1:
        has_perpendicular_c2 = st.radio("Does the molecule have perpendicular C2 axes to the principal Cn axis?", ("Yes", "No")) == "Yes"
    else:
        has_perpendicular_c2 = False

    has_horizontal_plane = st.radio("Does the molecule have a horizontal mirror plane (σh)?", ("Yes", "No")) == "Yes"
    has_vertical_plane = st.radio("Does the molecule have vertical mirror planes (σv)?", ("Yes", "No")) == "Yes"
    has_improper_rotation = st.radio("Does the molecule have an improper rotation axis (S2n)?", ("Yes", "No")) == "Yes"

    # Determine point group based on the user's answers
    point_group = determine_point_group(is_high_symmetry, highest_cn, has_perpendicular_c2, has_horizontal_plane, has_vertical_plane, has_improper_rotation)
else:
    point_group = "Td, Oh, Ih, C∞v, D∞h"  # High symmetry group options

# Display the result
st.subheader("Point Group Result")
st.write(f"The determined point group for the molecule is: **{point_group}**")

