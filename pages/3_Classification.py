import streamlit as st
import pickle
import numpy as np
from PIL import Image, ImageOps
import os

st.set_option("deprecation.showfileUploaderEncoding", False)

@st.cache_data
def load_model(model_path):
    with open(model_path, 'rb') as f: 
        model = pickle.load(f)
    return model

# Construct the file path to the ResNet101 model
base_dir = os.path.dirname(__file__)  # Get the directory of the current script
model_path = os.path.join(base_dir, "multipage_app", "best_weightsvgg.h5")

# Custom CSS for the layout
custom_css = """
<style>
.title-and-emoji-container {
    display: flex;
    align-items: center;
}
.title-and-emoji-container h1 {
    margin-right: 10px;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Display the title with the trash emoji
st.markdown(
    """
    <div class="title-and-emoji-container">
        <h1>Garbage Classification Models 🗑️</h1>
    </div>
    """, unsafe_allow_html=True
)

# Write model information
st.write("We worked on three models which are:")

# Define the model names and their accuracies
models = {
    "Vgg16": "98%",
    "Resnet": "100%",
    "Inception": "97%"
}

# Display model information
for model, accuracy in models.items():
    st.write(f"{model} with accuracy of <span style='color:brown'>{accuracy}</span>", unsafe_allow_html=True)

st.sidebar.success("Select a page above.")

file = st.file_uploader("Please Upload a Garbage Image...", type=["jpg", "png"])

def import_and_predict(image_data, model):
    size = (150, 150)
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    img = np.asarray(image)
    img_reshape = img[np.newaxis, ...]
    prediction = model.predict(img_reshape)
    return prediction

if file is None:
    st.text("Please Upload an image.")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    class_names = ["glass", "metal", "paper", "plastic", "shoes"]
    class_index = np.argmax(predictions)
    string = 'This image is classified as:' + class_names[class_index]
    st.success(string)
