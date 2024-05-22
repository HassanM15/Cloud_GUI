import streamlit as st
st.title("About Our Dataset!👋")
st.write("The Garbage Image Dataset consists of images of garbage items collected from nearby localities using smartphones. The dataset is categorized into five different classes. Each category represents a specific type of garbage item commonly found in everyday waste. The purpose of the Garbage Image Dataset is to provide a collection of labelled images of garbage items from different categories. The dataset can be used to train and evaluate deep learning models for garbage classification tasks. By training models on this dataset, they can learn to classify real world images of garbage items into one of the predefined categories.")
st.write("it consists of 10 classes:")
import streamlit as st

import streamlit as st

# Write the data
data = """
Metal: 1869  
Glass: 4097  
Biological: 985  
Paper: 2727  
Battery: 945  
Trash: 834  
Cardboard: 2341  
Shoes: 1977  
Clothes: 5325  
Plastic: 2542
"""

# Define emojis for each class
emojis = {
    "Metal": "🔩",
    "Glass": "🥛",
    "Biological": "🌱",
    "Paper": "📄",
    "Battery": "🔋",
    "Trash": "🗑️",
    "Cardboard": "📦",
    "Shoes": "👟",
    "Clothes": "👕",
    "Plastic": "🥤"
}

# Split the data into lines
lines = data.strip().split('\n')

# Divide data into groups of three
grouped_lines = [lines[i:i+3] for i in range(0, len(lines), 3)]

# Display grouped data
for group in grouped_lines:
    col1, col2, col3 = st.columns(3)
    for line in group:
        class_name, number = line.split(':')
        class_name = class_name.strip()
        number = number.strip()
        col1.write(f"{emojis.get(class_name, '')} {class_name}")
        col2.write(f"<span style='color:brown'>{number}</span>", unsafe_allow_html=True)
        col3.write("")
