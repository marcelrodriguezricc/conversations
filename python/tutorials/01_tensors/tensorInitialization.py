# From https://pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html

# Dependencies:
import torch # Import PyTorch library.
import numpy as np # Import NumPy library.

# From data:
data = [[1, 2],[3, 4]] # Create a two-dimensional matrix.
x_data = torch.tensor(data) # Embed the matrix in a tensor.
print(f"\nTensor from Data: \n {x_data} \n") # Print contents.

# From NumPy array:
np_array = np.array(data) # Embed the tensor in a NumPy array.
x_np = torch.from_numpy(np_array) # Create a tensor from the NumPy array.
print(f"Tensor from Numpy Array: \n {x_np} \n") # Print contents.

# From another Tensor:
x_ones = torch.ones_like(x_data) # Retain the property of the x_data tensor.
print(f"Ones Tensor from Tensor: \n {x_ones} \n") # Print contents.
x_rand = torch.rand_like(x_data, dtype=torch.float) # Override the datatype property of x_data tensor.
print(f"Random Tensor from Tensor: \n {x_rand} \n") # Print contents.

# Created from a predetermined shape with random or constant values:
shape = (2,3,) # Determines the dimensionality of the tensor.
rand_tensor = torch.rand(shape) # Fill the tensor of shape "shape" with random numbers.
print(f"Random Tensor from Shape: \n {rand_tensor} \n") # Print contents.
ones_tensor = torch.ones(shape) # Fill the tensor of shape "shape" with scalar 1.
print(f"Ones Tensor from Shape: \n {ones_tensor} \n") # Print contents.
zeros_tensor = torch.zeros(shape) # Fill the tensor of shape "shape" with scalar 0.
print(f"Zeros Tensor from Shape: \n {zeros_tensor}") # Print contents.