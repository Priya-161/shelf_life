Fruit Shelf Life Detection

Project Overview

This project aims to classify fruits and predict their shelf life based on annotated images using a pre-trained MobileNetV2 model. We collected and labeled 5,601 images across 7 types of fruits. The fruits are categorized into four subclasses indicating their freshness state, and their observed shelf life was recorded in days. This project builds two models:

Weight File Generated:
* category.h5 – Predicts the category of the fruit (e.g., Fresh, Semifresh,SemiRotten, Rotten).
* full_model.h5 – Predicts the shelf life in days.
  
Additionally, an app (app.py) allows users to upload images and receive predictions on both the fruit type and its shelf life.

Dataset Overview

The dataset contains 7 fruit types .We monitored various fruit types over several days and compiled the observations into a dataset.Below is the annotated information used for training:

![Screenshot (45)](https://github.com/user-attachments/assets/7a230bec-c6dc-4e8b-bdd6-ffe26ac4a907)

* Data Preprocessing:
   1. All 5,000 images were preprocessed and normalized for training.
   2. Labels were stored in label.csv, which maps the images to their categories and shelf life.

* Model Training
* Model Architecture:
  
   MobileNetV2, a pre-trained lightweight CNN model, is used as the base model with ImageNet weights.
   Additional classification layers are added on top.
   GlobalAveragePooling2D for dimensionality reduction.
   Dense layers (with 256 neurons) for further feature extraction.
   Dropout layer (0.5) for regularization.
   Softmax output layer to classify into multiple fruit categories.
   MobileNetV2 (pre-trained on ImageNet) was used as the base model for transfer learning.

Two models were built:
* Category Model: Trains to predict the fruit type and its freshness state.
* full_model.h5: Predicts the shelf life in days. (accuracy: 0.8893844485282898)
  
Application: app.py

The app.py script allows users to upload an image through a user interface. It loads both the models (category.h5 and full_model.h5) and provides the following outputs:
  1. Fruit Type and Category 
  2. Predicted Shelf Life in days.

Installation and Setup

1.Clone the Repository
2.Install Dependencies:pip install -r requirements.txt
3.Run the Application:streamlit run app.py

Usage Instructions
1.Upload an Image through the web app interface.
2.Receive Predictions:
Category: E.g., "Apple fresh".
Shelf Life: E.g., "9-14 days".

![p](https://github.com/user-attachments/assets/ccc089c4-a628-4e61-b633-131a6a5e3cad)

