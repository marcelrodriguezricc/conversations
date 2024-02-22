# From https://pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html

# Dependencies:
import torch # Import PyTorch library.
import numpy as np # Import NumPy library.

# Creation:
tensor = torch.rand(3,4, dtype=float) # Create a two-dimensional tensor filled with random floating point values and shape 3 x 4.

# Device Selection:
if torch.cuda.is_available(): # If the GPU is available...
    print(f"\nGPU Available \n") # Print that the GPU is available.
    tensor = tensor.to("cuda") # Run this Tensor on the GPU.
else: # Else if the GPU is unavailable...
    print(f"\nGPU Unavailable \n") # Print that the GPU is unavailable.

# Print:
print(f"Shape of tensor: {tensor.shape} \n") # Print the shape parameter.
print(f"Datatype of tensor: {tensor.dtype} \n") # Print the datatype parameter.
print(f"Device tensor is stored on: {tensor.device} \n") # Print the device parameter.
print(f"Tensor contents: \n {tensor} \n") # Print contents.