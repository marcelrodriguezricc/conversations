# From https://pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html

# Dependencies:
import os # Library for interacting with the operating system.
import torch # PyTorch library for machine learning.
from torch import nn # Import Neural Network class.
from torch.utils.data import DataLoader # Import DataLoader class.
from torchvision import datasets, transforms  # Import datasets and transforms

# Get Device:
device = ( # Set the device for training model...
    "cuda" # Use GPU.
    if torch.cuda.is_available() # If GPU is not available...
    else "mps" # Use MPU.
    if torch.backends.mps.is_available() # If MPS is not available...
    else "cpu" # Use CPU.
)

print(f"Using {device} device") # Print the device selected for use.

class NeuralNetwork(nn.Module): # Define class Neural Network and inherit from nn.Module subclass.
    def __init__(self): # Function to initialize the nn.Module class.
        super().__init__() # Initialize nn.Module.
        self.flatten = nn.Flatten() # Reshape the input tensor into a one dimensional tensor.
        self.linear_relu_stack = nn.Sequential( # A sequence of fully connected linear layers interleaved with ReLu activation functions.
            nn.Linear(28*28, 512), # First layer, accepts the 28 * 28 greyscale images and outputs them as a tensor of size 512.
            nn.ReLU(), # Rectified Linear Unit activation function. Returns 0 if any negative input, and returns x for positive input. f(x) = max(0, x).
            nn.Linear(512, 512), # Second linear layer. Accepts and outputs tensor of size 512.
            nn.ReLU(), # Another rectified Linear Unit activation function.
            nn.Linear(512, 10), # Final layer, accepts an input tensor of size 512 and outputs a tensor of size 10, corresponding to number of output classes.
        )

    def forward(self, x): # This function tells the neural network to feedfoward.
        x = self.flatten(x)  # Reshape the input tensor into a one dimensional tensor.
        logits = self.linear_relu_stack(x) # Pass to our previously established sequential network.
        return logits # Return raw predictions.
    
# Print the Structure of the Neural Network:
model = NeuralNetwork().to(device) # Create an instance of the neural network, and move it to the device.
print(model) # Print the structure.

# Execute the Model:
X = torch.rand(1, 28, 28, device=device) # Generate a single 28 x 28 tensor filled with random numbers on the previously specified device.
logits = model(X) # Obtain the logits by passing the randomally generated tensor "X" to the model.
pred_probab = nn.Softmax(dim=1)(logits)
y_pred = pred_probab.argmax(1)
print(f"Predicted class: {y_pred}")