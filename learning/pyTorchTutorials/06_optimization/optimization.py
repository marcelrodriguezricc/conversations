# From https://pytorch.org/tutorials/beginner/basics/optimization_tutorial.html#

# Import:
import torch # Import the PyTorch library.
from torch import nn # Import the neural network module from PyTorch.
from torch.utils.data import DataLoader # Import the DataLoader class from PyTorch.
from torchvision import datasets # Import the datasets module from torchvision.
from torchvision.transforms import ToTensor # Import the function which transforms images to tensors.

# Load the FashionMNIST data set to use for training.
training_data = datasets.FashionMNIST(
    root = "data", # This is where the data will be stored.
    train = True, # This specifies the data set will be used for training and not testing.
    download = True, # This will allow the data set to be downloaded if not available at root.
    transform = ToTensor() # This specifies the feature and label transformations, in this case to a tensor.
)

# Load the FashionMNIST data set separately to use for testing.
test_data = datasets.FashionMNIST(
    root = "data", # This is where the data will be stored.
    train = False, # This specifies the data set will be used for testing and not training.
    download = True, # This will allow the data set to be downloaded if not available at root.
    transform = ToTensor() # This specifies the feature and label transformations, in this case to a tensor.
)
train_dataloader = DataLoader(training_data, batch_size=64) # Create a DataLoader object for the training data set.
test_dataloader = DataLoader(test_data, batch_size=64) # Create a DataLoader object for the testing data set.

# Neural Network:
class NeuralNetwork(nn.Module): # Create a neural network class which inherits from the nn.Module class.
    def __init__(self): # Initialize the neural network.
        super().__init__() # Initialize the parent class.
        self.flatten = nn.Flatten() # Flatten the input tensor to make it one dimensional.
        self.linear_relu_stack = nn.Sequential( # Determine the sequence which the neural network will follow.
            nn.Linear(28*28, 512), # Create a linear layer with 28*28 input features and 512 output features.
            nn.ReLU(), # Apply the ReLU activation function.
            nn.Linear(512, 512), # Create a linear layer with 512 input features and 512 output features.
            nn.ReLU(), # Apply the ReLU activation function.
            nn.Linear(512, 10), # Create a linear layer with 512 input features and 10 output features.
        )

    def forward(self, x): # Define the forward pass function for the neural network to make predictions.
        x = self.flatten(x) # Flatten the input tensor to be one dimensional
        logits = self.linear_relu_stack(x)  # Pass the input tensor through the linear_relu_stack to make predictions.
        return logits # Return the predictions.

model = NeuralNetwork() # Create an instance of the neural network named model.

# Optimization Hyperparameters:
learning_rate = 1e-3 # Set the learning rate for the model, which will determine how much to update parameters at each epoch.
batch_size = 64 # Number of data samples to work through before updating the internal model parameters.
epochs = 5 # Number of times to iterate over the dataset.

# Initialize the Loss Function:
loss_fn = nn.CrossEntropyLoss() # Use the Cross Entropy Loss function to determine the loss of the model.

# Initialize the Optimizer:
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate) # Use the Stochastic Gradient Descent optimizer to update the model parameters based on our set learning rate.

# Train Loop Function:
def train_loop(dataloader, model, loss_fn, optimizer):
    print("HERE")
    size = len(dataloader.dataset) # Get the size of the dataset.
    model.train()# Set the model to training mode - important for batch normalization and dropout layers. Unnecessary in this situation but added for best practices
    for batch, (X, y) in enumerate(dataloader): # Iterate through the data loader.
        pred = model(X) # Feed the data into the model to make predictions.
        loss = loss_fn(pred, y) # Apply the loss function of the model.

        # Backpropagation:
        loss.backward() # Backpropagate the loss function to update the model parameters.
        optimizer.step() # Update the model parameters based on the loss function.
        optimizer.zero_grad() # Reset the gradients to zero.

        if batch % 100 == 0: # Print the loss and the number of samples processed every 100 batches.
            loss, current = loss.item(), batch * batch_size + len(X) # Get the loss and the number of samples processed.
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]") # Print the loss and the number of samples processed.

# Test Loop Function:
def test_loop(dataloader, model, loss_fn):
    model.eval() # Set the model to evaluation mode,  important for batch normalization and dropout layers. Unnecessary in this situation but added for best practices.
    size = len(dataloader.dataset) # Get the size of the dataset.
    num_batches = len(dataloader) # Get the number of batches in the dataset.
    test_loss, correct = 0, 0 # Initialize the test loss and correct predictions to 0.

    with torch.no_grad(): # Turn off gradient tracking for the model during test mode, also serves to reduce unnecessary gradient computations and memory usage for tensors with requires_grad = True.
        for X, y in dataloader: # Iterate through the data loader.
            pred = model(X) # Feed the data into the model to make predictions.
            test_loss += loss_fn(pred, y).item() # Add the calculated loss to the test loss variable.
            correct += (pred.argmax(1) == y).type(torch.float).sum().item() # Add the number of correct predictions to the correct variable.

    test_loss /= num_batches # Get the average loss.
    correct /= size # Get the average number of correct predictions.

    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n") # Print the test error, accuracy, and average loss.

# Initialize the Loss Function:
loss_fn = nn.CrossEntropyLoss() # Use the Cross Entropy Loss function to determine the loss of the model.

# Initialize the Optimizer:
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate) # Use the Stochastic Gradient Descent optimizer to update the model parameters based on our set learning rate.

epochs = 10 # Increase the number of epochs to 10.

for t in range(epochs): # Iterate through the number of epochs.
    print(f"Epoch {t+1}\n-------------------------------") # Print the current epoch.
    train_loop(train_dataloader, model, loss_fn, optimizer) # Run the training function.
    test_loop(test_dataloader, model, loss_fn) # Run the testing function.
print("Done!") # Print "Done!" when the training and testing loops are complete.