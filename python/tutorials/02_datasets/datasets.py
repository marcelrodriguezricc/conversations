# From https://pytorch.org/tutorials/beginner/basics/data_tutorial.html

# Dependencies:
import torch # PyTorch Library.
from torch.utils.data import Dataset # Dataset class to store and reference stored data.
from torch.utils.data import DataLoader # Dataloader class for fast data retrieval.
from torchvision import datasets # Pre downloaded data sets in PyTorch.
from torchvision.transforms import ToTensor # A function which converts a image or ndarray to a tensor. 
import matplotlib.pyplot as plt # Interface which allows us to visualize data.
import os # Library for interacting with the operating system.
import pandas as pd # Library for data analysis and manipulation.
from torchvision.io import read_image # Function which converts images into tensors.

# Loading Datasets:

# Training:
training_data = datasets.FashionMNIST( # Load the FashionMNIST data set to use for training.
    root="data", # This is where the data will be stored.
    train=True, # This specifies the data set will be used for training and not testing.
    download=True, # This will allow the data set to be downloaded if not available at root.
    transform=ToTensor() # This specifies the feature and label transformations, in this case to a tensor.
)

# Testing:
test_data = datasets.FashionMNIST( # Load the FashionMNIST data set separately to use for testing.
    root="data", # This is where the data will be stored.
    train=False, # This specifies the data set will be used for testing and not training.
    download=True, # This will allow the data set to be downloaded if not available at root.
    transform=ToTensor() # This specifies the feature and label transformations, in this case to a tensor.
)

# "Fashion-MNIST is a dataset of Zalando’s article images consisting of 60,000 training examples and 10,000 test examples.
# Each example comprises a 28 × 28 grayscale image and an associated label from one of 10 classes."

# Visualizing data set:
labels_map = { # An array which gives a name to each of the 10 class labels.
    0: "T-Shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",
}

figure = plt.figure(figsize=(8, 8)) # Create the Matplotlib interface.
cols, rows = 3, 3 # The columns and rows of our index map for the Matplotlib interface.
for i in range(1, cols * rows + 1): # Iterate through each item.
    sample_idx = torch.randint(len(training_data), size=(1,)).item() # Generate a random interger from 0 to the length of the data set.
    img, label = training_data[sample_idx] # Grab the nth sample of our data set, with n being the randomally generated integer.
    figure.add_subplot(rows, cols, i) # Add sample to plot.
    plt.title(labels_map[label]) # Title the sample with the label.
    plt.axis("off") # Turn axis off.
    plt.imshow(img.squeeze(), cmap="gray") # Show sample image.
plt.show() # Open a window with the Matplotlib interface after all samples are loaded.

# Creating a Custom Dataset:
class CustomImageDataset(Dataset):
    # Initialize the directory containing the images, annotations file, and both transforms.
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotations_file) # Initialize a CSV plain text file for the annotations.
        self.img_dir = img_dir  # Initialize a directory where the images will be stored.
        self.transform = transform # Optional parameter which will store transformation functions for the data.
        self.target_transform = target_transform # Allow data transforms for the labels and images respectively.

    # Get the number of labels in our image set.
    def __len__(self):
        return len(self.img_labels) # Function returns the length of the list of labels.

    # Load and return sample from dataset at given index.
    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0]) # Find the path to "index" -th row of the 0th column of the image directory.
        image = read_image(img_path) # Retrieve the image, and convert it into a tensor.
        label = self.img_labels.iloc[idx, 1] # Retreive the corresponding label.
        if self.transform: # Check for a transform associated with the image...
            image = self.transform(image) # And apply it to the image.
        if self.target_transform: # Check for a transform associated with the label...
            label = self.target_transform(label) # And apply it to the label.
        return image, label # Return the selected image and associated label with the transforms applied.
    
train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True) # Train the DataLoader from FashionMNIST training dataset. Data will be shuffled after iteration.
test_dataloader = DataLoader(test_data, batch_size=64, shuffle=True) # Test the DataLoader. Train the DataLoader from FashionMNIST testing. dataset. Data will be shuffled after iteration.
train_features, train_labels = next(iter(train_dataloader)) # Fetch the data for the features
print(f"Feature batch shape: {train_features.size()}") # Print out the shape of the feature batch.
print(f"Labels batch shape: {train_labels.size()}") # Print out the shape of the label batch.
img = train_features[0].squeeze() # Get the first image.
label = train_labels[0] # Get the first label.
plt.imshow(img, cmap="gray") # Load the image to be shown.
plt.show() # Show the image.
print(f"Label: {label}") # Print the label.