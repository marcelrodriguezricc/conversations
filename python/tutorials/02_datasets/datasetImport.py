# Libraries:
import torch # PyTorch Library.
from torch.utils.data import Dataset # Data set class.
from torchvision import datasets # Pre downloaded data sets in PyTorch.
from torchvision.transforms import ToTensor # A function which converts a image or ndarray to a tensor. 
import matplotlib.pyplot as plt # Interface which allows us to visualize data.

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