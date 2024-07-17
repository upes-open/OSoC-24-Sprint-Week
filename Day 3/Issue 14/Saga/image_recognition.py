import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models


def load_and_preprocess_data():
    (training_images, training_labels), (testing_images, testing_labels) = datasets.cifar10.load_data()
    training_images, testing_images = training_images / 255.0, testing_images / 255.0
    return (training_images, training_labels), (testing_images, testing_labels)


def display_sample_images(training_images, training_labels):
    class_names = ['Plane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

    plt.figure(figsize=(10, 10))
    for i in range(16):
        plt.subplot(4, 4, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(training_images[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[training_labels[i][0]])

    plt.show()


def create_model():
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(32,32,3)))
    model.add(layers.MaxPooling2D((2,2)))
    model.add(layers.Conv2D(64, (3,3), activation='relu'))
    model.add(layers.MaxPooling2D((2,2)))
    model.add(layers.Conv2D(64, (3,3), activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))
    return model


def compile_and_train_model(model, training_images, training_labels, testing_images, testing_labels):
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(training_images, training_labels, epochs=20, validation_data=(testing_images, testing_labels))
    return model


def evaluate_model(model, testing_images, testing_labels):
    loss, accuracy = model.evaluate(testing_images, testing_labels)
    print(f"Loss: {loss}")
    print(f"Accuracy: {accuracy}")


def load_model():
    model = models.load_model('image_classifier.model')
    return model


def predict(model):
    img = cv.imread('<enter file name>')
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.imshow(img, cmap = plt.cm.binary)

    prediction = model.predict(np.array([img])/255)
    index = np.argmax(prediction)

    print(f"Prediction is: {class_names[index]}")

    plt.show()


def main():
    (training_images, training_labels), (testing_images, testing_labels) = load_and_preprocess_data()
    display_sample_images(training_images, training_labels)
    
    model = create_model()
    model = compile_and_train_model(model, training_images, training_labels, testing_images, testing_labels)
    evaluate_model(model, testing_images, testing_labels)

    model.save("image_classifier.model")


if __name__ == "__main__":
    main()
