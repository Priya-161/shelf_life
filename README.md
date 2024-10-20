Fruit Shelf Life Detection
Project Overview
This project aims to classify fruits and predict their shelf life based on annotated images using a pre-trained MobileNetV2 model. We collected and labeled 5,000 images across 7 types of fruits. The fruits are categorized into four subclasses indicating their freshness state, and their observed shelf life was recorded in days. This project builds two models:

category.h5 – Predicts the category of the fruit (e.g., Fresh, Semifresh, Rotten).
full_model.h5 – Predicts the shelf life in days.
Additionally, an app (app.py) allows users to upload images and receive predictions on both the fruit type and its shelf life.

Dataset Overview
The dataset contains 7 fruit types with 4 freshness categories each. Below is the annotated information used for training:
![Screenshot (45)](https://github.com/user-attachments/assets/7a230bec-c6dc-4e8b-bdd6-ffe26ac4a907)
Preprocessing and Model Training

Data Preprocessing:
All 5,000 images were preprocessed and normalized for training.
Labels were stored in label.csv, which maps the images to their categories and shelf life.

Model Architecture:
MobileNetV2 (pre-trained on ImageNet) was used as the base model for transfer learning.
Two models were built:
Category Model: Trains to predict the fruit type and its freshness state.
Shelf Life Model: Predicts the expected number of days remaining for the fruit's shelf life.


Fruit Shelf Life Detection - GitHub Project
Project Overview
This project aims to classify fruits and predict their shelf life based on annotated images using a pre-trained MobileNetV2 model. We collected and labeled 5,000 images across 7 types of fruits. The fruits are categorized into four subclasses indicating their freshness state, and their observed shelf life was recorded in days. This project builds two models:

category.h5 – Predicts the category of the fruit (e.g., Fresh, Semifresh, Rotten).
full_model.h5 – Predicts the shelf life in days.
Additionally, an app (app.py) allows users to upload images and receive predictions on both the fruit type and its shelf life.

Dataset Overview
The dataset contains 7 fruit types with 4 freshness categories each. Below is the annotated information used for training:

Fruit Category	Observed Shelf Life (days)
Apple Fresh	9-14
Apple Semifresh	4-8
Apple Semirotten	1-3
Apple Rotten	0
Banana Fresh	6-9
Banana Semifresh	2-5
Banana Semirotten	1
Banana Rotten	0
Peach Fresh	9-12
Peach Semifresh	4-8
Peach Semirotten	1-3
Peach Rotten	0
Pear Fresh	9-14
Pear Semifresh	4-8
Pear Semirotten	1-3
Pear Rotten	0
Mango Fresh	7-12
Mango Semifresh	3-6
Mango Semirotten	1-2
Mango Rotten	0
Orange Fresh	7-10
Orange Semifresh	3-6
Orange Semirotten	1-2
Orange Rotten	0
Melon Fresh	7-10
Melon Semifresh	3-6
Melon Semirotten	1-2
Melon Rotten	0
Preprocessing and Model Training
Data Preprocessing:

All 5,000 images were preprocessed and normalized for training.
Labels were stored in label.csv, which maps the images to their categories and shelf life.
Model Architecture:

MobileNetV2 (pre-trained on ImageNet) was used as the base model for transfer learning.
Two models were built:
Category Model: Trains to predict the fruit type and its freshness state.
Shelf Life Model: Predicts the expected number of days remaining for the fruit's shelf life.
Saved Models:

category.h5: Predicts the category of the fruit.
full_model.h5: Predicts the shelf life in days.
Application: app.py
The app.py script allows users to upload an image through a user interface. It loads both the models (category.h5 and full_model.h5) and provides the following outputs:

Fruit Type and Category (e.g., Apple Fresh, Banana Rotten).
Predicted Shelf Life in days.

Installation and Setup
1.Clone the Repository
2.Install Dependencies:pip install -r requirements.txt
3.Run the Application:streamlit run app.py

Usage Instructions
1.Upload an Image through the web app interface.
2.Receive Predictions:
Category: E.g., "Apple fresh".
Shelf Life: E.g., "9-14 days".
