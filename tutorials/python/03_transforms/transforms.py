# From https://pytorch.org/tutorials/beginner/basics/data_tutorial.html

# Import:
import torch # PyTorch library for machine learning.
from torchvision import datasets # Dataset class from TorchVision.
from torchvision.transforms import ToTensor, Lambda #  Functions for transforming data to normalized tensors and the labels to one-hot encoded tensors.

# Dataset Creation:
ds = datasets.FashionMNIST(
    root = "data", # Directory where the dataset will be stored.
    train = True, # Dataset will be used for training.
    download = True, # Dataset will be downloaded for the internet if not already.
    transform = ToTensor(), # Convert the images to tensors.
    target_transform = Lambda( # Lamba function which converts label to one-hot encoded tensor of size 10.
        lambda y: torch.zeros(10, # Size of zero tensor.
        dtype=torch.float).scatter_(0, torch.tensor(y),  # Scatter writes all values from tensor "src" into self at index-nth tensor.
        value=1)) # Assigns a value of 1 on the index as given by label y.
)


