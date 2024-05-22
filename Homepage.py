import streamlit as st
import base64
from streamlit_lottie import st_lottie
import requests
import json

st.set_page_config(
    page_title='EcoClassify',
    page_icon='🏠',
    layout="wide"
)

# Function to load image and convert to base64
def load_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Load image and convert to base64
image_path = "Cloud_GUI/assets/fb118e148378c52027364cb47e9f67b0-removebg-preview.png"
image_base64 = load_image(image_path)

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



# Custom CSS for the layout
custom_css = """
<style>
.title-and-image-container {
    display: flex;
    align-items: center;
}

.name-box {
    font-size: 1.6rem;
    font-weight: bolder;
    color: brown;
    border: 2px solid grey;
    border-radius: 10px;
    background-color: #d3d3d3;
    padding: 5px;
    text-align: center;
    margin: 70px 0;
}
.id-box {
    font-size: 1rem;
    color: black;
    margin-top: 5px;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="title-and-image-container">
        <h1>Welcome To EcoClassify !</h1>
        <img src="data:image/png;base64,{image_base64}" width="200">
    </div>
    """, unsafe_allow_html=True
)

st.sidebar.success("Select a page above.")

col1, col2, col3 = st.columns(3)
col1.markdown('<div class="name-box">Hassan Mostafa<div class="id-box">213529</div></div>', unsafe_allow_html=True)
col2.markdown('<div class="name-box">Mariam Ahmed<div class="id-box">213545</div></div>', unsafe_allow_html=True)
col3.markdown('<div class="name-box">Haidy Haitham<div class="id-box">212539</div></div>', unsafe_allow_html=True)

