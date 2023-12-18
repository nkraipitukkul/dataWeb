import streamlit as st

st.set_page_config(page_title="Face Generation Web", page_icon=":cold_sweat:", layout="wide")

st.title("Face Generation")
st.write("GAN Model: controller_age015id025exp02hai04ori02gam15")

st.write("Input image: ")
st.image('./input.jpg')

selected_control = st.selectbox("Pick one", ["None", "Expression", "Gamma", "Hair", "Orientation","Age"])

if selected_control == "Age":
    st.write("Output image: ")
    st.image('./age.jpg')
elif selected_control == "Expression":
    st.write("Output image: ")
    st.image('./expression.jpg')
elif selected_control == "Gamma":
    st.write("Output image: ")
    st.image('./gamma.jpg')
elif selected_control == "Hair":
    selected_color = st.radio("Pick one color", ["Black", "Blonde"])
    if selected_color == "Black":
        st.write("Output image: ")
        st.image('./hair_black.jpg')
    else:
        st.write("Output image: ")
        st.image('./hair_blonde.jpg')
elif selected_control == "Orientation":
    st.write("Output image: ")
    st.image('./orientation.jpg')
else:
    st.write("Please select option")