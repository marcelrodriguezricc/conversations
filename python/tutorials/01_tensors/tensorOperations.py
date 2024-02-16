# From https://pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html

# Dependencies:
import torch # Import PyTorch library.
import numpy as np # Import NumPy library.

# Indexing and Slicing:
tensor = torch.ones(4, 4) # Create a two dimensional 4 x 4 tensor, filled with scalars values of 1.
print(f"\n1. First row: \n  {tensor[0]}\n") # Print the first row of the tensor.
print(f"2. First column: \n  {tensor[:, 0]}\n") # Print the first column of the tensor.
print(f"3. Last column: \n  {tensor[..., -1]}\n") # Print the last column of the tensor.
tensor[:, 1] = 0 # Replace the second column of the tensor with zeroes.
print(f"4. Altered Tensor: \n  {tensor}\n") # Print the contents of the tensor after the column replacement.

# Joining:
tensorVert = torch.cat([tensor, tensor, tensor], dim=0)
print(f"5. Joined Vertically: \n  {tensorVert}\n")
tensorHoriz = torch.cat([tensor, tensor, tensor], dim=1)
print(f"6. Joined Horizontally: \n  {tensorHoriz}\n")

# Matrix Multiplication:
y1 = tensor @ tensor.T # Perform a matrix multiplication of tensor "tensor" and a transposition of itself (swapped dimensionality).
y2 = tensor.matmul(tensor.T) # This is the same as y1.
y3 = torch.rand_like(y1) # Create a new tensor with the same parameters at y1 but filled with random scalar values.
torch.matmul(tensor, tensor.T, out=y3) # Perform the multiplication of tensor "tensor" and it's transpoititon, but store the calculation in tensor y3.
print(f"7. Matrix Mult: \n  y1: {y1}\n \n  y2: {y2}\n \n  y3: {y3}\n") # Print contents of tensor. They're all the same.

# Element Multiplication:
z1 = tensor * tensor # Perform an element multiplication of tensor "tensor" and itself.
z2 = tensor.mul(tensor) # Same as above.
z3 = torch.rand_like(tensor) # Create a tensor with the same parameters as "tensor" but filled with random scalar values.
torch.mul(tensor, tensor, out=z3) # Multiply tensor "tensor" by itself and store the calculation in tensor z3.
print(f"8. Element Mult: \n  z1: {z1}\n \n  z2: {z2}\n \n  z3: {z3}\n") # Print contents of tensor. They're all the same.

# Aggregation:
agg = tensor.sum() # Aggregate tensor into a single element by adding all scalar values in tensor together.
agg_item = agg.item() # Convert the one-element tensor into a Python numerical value.
print(f"9. Aggregation: \n Number:",agg_item, "\n Type:", type(agg_item), "\n") # Print the Python numerical value and the class of item.

# In Place Operations:
tensor.add_(5) # Add 5 to each element in the tensor.
print(f"10. In Place: \n {tensor}\n") # Print tensor contents.

# Tensor to NumPy Array:
t = torch.ones(5) # Create a single-dimensional tensor named "t" with 5 values equal to 1.
n = t.numpy() # Make a NumPy array named "n" equal to the tensor "t."
print(f"11. Tensor to NumPy Array: \n t before: {t}\n n before: {n}") # Print tensor and NumPy array contents.
t.add_(1) # Add 1 to each scalar value in the tensor, the same will be done to the NumPy array.
print(f" t after: {t}\n n after: {n}") # Print tensor and NumPy array contents after the element addition.