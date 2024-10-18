import streamlit as st
import os
from pred import pred  # Import the pred function from pred.py (shelf life prediction)
from pred2 import predict_image1  # Import the predict_image1 function from pred2.py (fruit category prediction)

# Create a temporary directory for storing uploaded images
TEMP_DIR = 'temp'

# Streamlit app
st.title('Fruit Quality and Category Prediction')
st.write("Upload an image of a fruit to predict its quality and category.")

# File uploader for image upload
uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Ensure the temp directory exists
    os.makedirs(TEMP_DIR, exist_ok=True)

    # Save the uploaded file temporarily
    img_path = os.path.join(TEMP_DIR, uploaded_file.name)
    
    # Write the uploaded file to the temp directory
    with open(img_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Display the uploaded image
    st.image(img_path, caption='Uploaded Image', use_column_width=True)

    # Make prediction for shelf life using the pred function from pred.py
    predicted_shelf_life = pred(img_path)
    
    # Make prediction for fruit category using the predict_image1 function from pred2.py
    predicted_fruit_category = predict_image1(img_path)

    # Display the combined predictions
    st.write(f'Predicted Fruit Category: {predicted_fruit_category}')
    st.write(f'Predicted Shelf Life (in days): {predicted_shelf_life}')

    # Optionally, delete the temporary file after prediction
    os.remove(img_path)  # Uncomment if you want to remove the image after processing
