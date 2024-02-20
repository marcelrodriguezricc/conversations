# From https://pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html

# Dependencies:
import os # Library for interacting with the operating system.
import torch # PyTorch library for machine learning.
from torch import nn # Import Neural Network class.
from torch.utils.data import DataLoader # Import DataLoader class.
from torchvision import datasets, transforms  # Import datasets and transforms


# Example Neural Network Build:

# Get Device:
device = ( # Set the device for training model...
    "cuda" # Use GPU.
    if torch.cuda.is_available() # If GPU is not available...
    else "mps" # Use MPS.
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

    def forward(self, x): # This function tells the neural network to feedforward.
        x = self.flatten(x)  # Reshape the input tensor into a one dimensional tensor.
        logits = self.linear_relu_stack(x) # Pass to our previously established sequential network.
        return logits # Return raw predictions.
    
# Print the Structure of the Neural Network:
model = NeuralNetwork().to(device) # Create an instance of the neural network, and move it to the device.
print(model) # Print the structure.

# Execute the Model:
X = torch.rand(1, 28, 28, device=device) # Generate a single 28 x 28 tensor filled with random numbers on the previously specified device.
logits = model(X) # Obtain the logits by passing the randomly generated tensor "X" to the model. Logits here is a tensor that contains the raw unnormalized scores.
pred_probab = nn.Softmax(dim=1)(logits) # Applies the SoftMax activation function to the convert the raw scores in the logits to probabilities.
y_pred = pred_probab.argmax(1) # Select the class with the highest probability, which in this case is index 1.
print(f"Predicted class: {y_pred}") # Print the predicted class.


# Layer Breakdown:

# Generate random tensor to feed to the model:
input_image = torch.rand(3,28,28) # Take a randomly generated tensor containing 3 28 X 28 images, and pass them to the network. 
print(f"Input image: {input_image.size()}") # Print the size on the tensor.

# Flatten the randomly generated tensor:
flatten = nn.Flatten() # Create an instance of the flatten class.
flat_image = flatten(input_image) # Flatten to a single dimension, three arrays of 784 grayscale pixel values (3 x 28 X 28).
print(f"Flattened image: {flat_image.size()}") # Print the size of the flattened tensor.

# Apply linear transformation using stored weights and biases.
layer1 = nn.Linear(in_features=28*28, out_features=20) # Create an instance of the linear class, with 28 x 28 input features and 20 output features.
hidden1 = layer1(flat_image) # Pass the flattened image to the linear layer.
print(f"Transformed image: {hidden1.size()}") # Print the size of the tensor after it's been passed through the linear layer.

print(f"Before ReLU: {hidden1}\n\n") # Print the tensor before it's been passed through the ReLU activation function.
hidden1 = nn.ReLU()(hidden1) # Pass the tensor through the ReLU activation function.
print(f"After ReLU: {hidden1}") # Print the tensor after it's been passed through the ReLU activation function.

# Sequential Chain Method:
seq_modules = nn.Sequential( # Create a sequence of operations to be performed on the input tensor.
    flatten, # Flatten the input tensor.
    layer1, # Pass the flattened tensor to the first linear layer.
    nn.ReLU(), # Perform the ReLu function.
    nn.Linear(20, 10) # Pass the tensor to the second linear layer.
)

input_image = torch.rand(3,28,28) # Take a randomly generated tensor containing 3 28 X 28 images, and pass them to the network. 
logits = seq_modules(input_image) # Apply the sequence of operations to the randomly generated tensor.

softmax = nn.Softmax(dim=1) # Create an instance of the SoftMax activation function.
pred_probab = softmax(logits) # Pass the logits to the SoftMax activation function.

print(f"Model structure: {model}\n\n") # Print the model structure.

for name, param in model.named_parameters(): # Print the parameters of the model.
    print(f"Layer: {name} | Size: {param.size()} | Values : {param[:2]} \n")