# From https://pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html

# Dependencies:
import torch # Import PyTorch library for machine learning.

# Simple Example:
x = torch.ones(5)  # Input tensor.
y = torch.zeros(3)  # Expected output.
w = torch.randn(5, 3, requires_grad = True) # A random tensor of size 5 x 3 is generated for the weights. The "requires_grad = True" flag indicates that we want to compute gradients with respect to these tensors during the backward pass.
b = torch.randn(3, requires_grad = True) # A random tensor of size 3 is generated for the bias. The "requires_grad = True" flag indicates that we want to compute gradients with respect to these tensors during the backward pass.
z = torch.matmul(x, w) + b # Output of the model, the result of the matrix multiplication of the input tensor and the weights, plus the bias.
loss = torch.nn.functional.binary_cross_entropy_with_logits(z, y) # This is the loss function, comparing the predicted output of the model to the expected output.
print(f"Gradient function for z = {z.grad_fn}") # Print the gradient function for z.
print(f"Gradient function for loss = {loss.grad_fn}") # Print the gradient function for the loss.

# Compute Gradients:
loss.backward() # Function computes the gradients of tensors with the"requires_grad = True" tag.
print(w.grad) # Print the gradients for the weights.
print(b.grad) # Print the gradients for the biases.
