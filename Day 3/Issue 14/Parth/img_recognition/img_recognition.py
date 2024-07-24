import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions

def load_image(image_path):
    # Load an image from file
    img = cv2.imread(image_path)
    # Convert the image to RGB (OpenCV loads as BGR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Resize the image to the size expected by the model
    img = cv2.resize(img, (224, 224))
    # Convert the image to a numpy array
    img_array = np.array(img)
    # Add a batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    # Preprocess the image array
    img_array = preprocess_input(img_array)
    return img_array

def predict_image(model, img_array):
    # Perform prediction
    predictions = model.predict(img_array)
    # Decode predictions to class names
    decoded_predictions = decode_predictions(predictions, top=3)[0]
    return decoded_predictions

def main(image_path):
    # Load the pre-trained MobileNetV2 model
    model = MobileNetV2(weights='imagenet')
    # Load and preprocess the image
    img_array = load_image(image_path)
    # Predict the image
    predictions = predict_image(model, img_array)
    # Print the predictions
    for i, (imagenet_id, label, score) in enumerate(predictions):
        print(f"{i+1}. {label}: {score:.4f}")

# Replace 'path_to_your_image.jpg' with the path to your image
image_path = 'car1.png'
main(image_path)
