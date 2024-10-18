import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import os

IMG_SIZE1 = 224
model_path = 'category.h5'
model = tf.keras.models.load_model(model_path)

def load_and_preprocess_image1(img_path1):
    """Load and preprocess the image for prediction."""
    img1 = image.load_img(img_path1, target_size=(IMG_SIZE1, IMG_SIZE1))
    img_array1 = image.img_to_array(img1)
    img_array1 = np.expand_dims(img_array1, axis=0)  # Add batch dimension
    img_array1 = img_array1 / 255.0  # Rescale to [0, 1]
    return img_array1

def predict_image1(img_path1):
    """Make a prediction for a single image using the loaded model and display it."""
    # Load and preprocess the image
    img_array1 = load_and_preprocess_image1(img_path1)

    # Make predictions
    predictions1 = model.predict(img_array1)
    predicted_class1 = np.argmax(predictions1, axis=1)

    # Map predicted class back to the class name
    #class_labels1 = list(train_generator1.class_indices.keys())
    #print(class_labels1)
    class_labels1=['Apple Fresh', 'Apple Rotten', 'Apple Semifresh', 'Apple Semirotten', 'Banana Fresh', 'Banana Rotten', 'Banana Semifresh', 'Banana Semirotten', 'Mango Fresh', 'Mango Rotten', 'Mango Semifresh', 'Mango Semirotten', 'Melon Fresh', 'Melon Rotten', 'Melon Semifresh', 'Melon Semirotten', 'Orange Fresh', 'Orange Rotten', 'Orange Semifresh', 'Orange Semirotten', 'Peach Fresh', 'Peach Rotten', 'Peach Semifresh', 'Peach Semirotten', 'Pear Fresh', 'Pear Rotten', 'Pear Semifresh', 'Pear Semirotten']
    predicted_label1 = class_labels1[predicted_class1[0]]

    # Display the image and prediction results
    '''plt.imshow(image.load_img(img_path1))
    plt.axis('off')  # Turn off axis
    plt.title(f'Predicted class: {predicted_label1}')
    plt.show()'''
    return predicted_label1 
    

# Example usage
'''img_path1 = 'test\\banana_2-981-_jpg.rf.5d3ec25a187f2c0441e69962c617b9ec.jpg'  # Replace with your image path
predict_image1(img_path1)'''