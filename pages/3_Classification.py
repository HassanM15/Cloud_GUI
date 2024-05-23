import streamlit as st
from PIL import Image, ImageOps
import numpy as np

st.set_option("deprecation.showfileUploaderEncoding", False)

st.markdown(
    """
    <div class="title-and-emoji-container">
        <h1>Garbage Classification Models 🗑️</h1>
    </div>
    """, unsafe_allow_html=True
)

st.write("We worked on three models which are:")

models = {
    "Vgg16": "98%",
    "Resnet": "100%",
    "Inception": "97%"
}

for model, accuracy in models.items():
    st.write(f"{model} with accuracy of <span style='color:brown'>{accuracy}</span>", unsafe_allow_html=True)

st.sidebar.success("Select a page above.")

file = st.file_uploader("Please Upload a Garbage Image...", type=["jpg", "png"])

if file is None:
    st.text("Please Upload an image.")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    

    predicted_class = "metal"
    
    if predicted_class == "metal":
        st.text("The image uploaded is metal.")
