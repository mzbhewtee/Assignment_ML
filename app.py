import streamlit as st
from PIL import Image
import os
import warnings
import numpy as np
import pickle

warnings.filterwarnings('ignore')

# # Specify the path to the model
# model_path = 'C:/Users/Hp/Downloads/model.pkl'

# # Load the saved model using pickle
# with open(model_path, 'rb') as file:
#     loaded_model = pickle.load(file)

# Function to detect defects
# def detect_defect(image_path):
#     img = Image.open(image_path)
#     img = img.convert("RGB")  # Ensure the image is in RGB format
#     img = img.resize((224, 224))  # Resize image if needed
#     img = np.array(img) / 255.0  # Normalize pixel values
#     img = np.expand_dims(img, axis=0)  # Add batch dimension

#     # Make predictions using the loaded model
#     prediction = loaded_model.predict(img)

#     # Check the prediction result
#     if prediction[0][0] >= 0.5:  # Assuming binary classification (defect or non-defect)
#         result = "Defect Detected"
#     else:
#         result = "No Defect Detected"

#     return result

st.set_page_config(page_title="Car Defect Detector", page_icon=":car:", layout="wide")

st.title("Car Defect Detector")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

fl = st.file_uploader(":file_folder: Upload a file", type=(["jpg", "jpeg", "png"]))

col1, col2 = st.columns(2)

with col1:
    if fl is not None:
        filename = fl.name
        st.write(filename)
        img = Image.open(fl)
        st.image(img, width=300)

        # Save the image temporarily
        img.save(filename)
        image_path = os.path.join(os.getcwd(), filename)
        # detection_result = detect_defect(image_path)
    else:
        st.write("Please upload a file")

with col2:
    st.write("")
    st.write("")
    st.write("### :bar_chart: Defects")
    # If uploaded image is a car, write Yes and check in front, else No and cross in front
    if fl is not None:
        st.write("#### :car: Yes :heavy_check_mark:")
        # st.write(f"#### :wrench: Defect {detection_result}")
        st.write("#### :chart_with_upwards_trend: Confidence :100:")
    else:
        st.write("#### :car: No :x:")
        st.write("Kindly Upload a car image")
