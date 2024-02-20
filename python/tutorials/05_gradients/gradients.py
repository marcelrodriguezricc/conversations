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
loss.backward() # Function computes the gradients of tensors with the "requires_grad = True" tag.
print(w.grad) # Print the gradients for the weights.
print(b.grad) # Print the gradients for the bias.


z = torch.matmul(x, w) + b # Recompute the output tensor with the gradient computation.
print(z.requires_grad) # Print the "requires_grad" flag for the output tensor, which should be "True".

with torch.no_grad(): # Disable the gradient computation, for when we would like only do the forward computation by applying some input data.
    z = torch.matmul(x, w) + b # Recompute the output tensor without the gradient computation, 
print(z.requires_grad) # Print the "requires_grad" flag for the output tensor, which should be "False".

# Gradient Accumulation:

inp = torch.eye(4, 5, requires_grad=True) # Creates a 2D 4 x 5 tensor with ones on the diagonal and zeros elsewhere, and the "requires_grad = True" flag to compute gradients.
out = (inp+1).pow(2).t() # The output tensor is the result of the transpose of the square of the sum of the input tensor and 1.
out.backward(torch.ones_like(out), retain_graph=True) # Compute the gradients of the output tensor through backpropagation.
print(f"First call\n{inp.grad}") # Print the gradients of the first pass.
out.backward(torch.ones_like(out), retain_graph=True) # A second compute of the gradients. Notice the accumulation of the gradients.
print(f"\nSecond call\n{inp.grad}") # Print the gradients of the second pass.
inp.grad.zero_() # Zero the gradients of the input tensor.
out.backward(torch.ones_like(out), retain_graph=True) # After zeroing the gradients, a recomputation of them matches the first pass.
print(f"\nCall after zeroing gradients\n{inp.grad}") # Print the third pass, after the zeroing.