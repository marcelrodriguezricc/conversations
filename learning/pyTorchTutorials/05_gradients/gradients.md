# GRADIENTS

In physics, a gradient is represented as a vector with a magnitude that quantifies a change in the value per unit distance. For example, if we wanted to observe the temperature gradient in a room, we might see how much the temperature changes from each square foot in the room as seen from directly overhead. We divide the room up into square feet. We then draw an arrow which represents our gradient through the box from the neighboring box with the temperature to the neighboring box with the highest. The magnitude is the overall change in temperature across the foot-long arrow, and the direction points from the lowest to the highest, giving the vector of our gradient.

We can also understand this in terms of derivatives. A derivative is the amount of change between two points in a function. A gradient is a derivative with more than one input variable. In the previous example, there are two input variables for which we calculate two derivatives, the amount of change in temperature per square foot in the x, and the amount of change in temperature per square foot in the y. Similarly, in machine learning we're often dealing with more than one variable.

In machine learning, the term gradient is used to describe the amount of error with respect to the weights and biases of each node throughout the network. The gradient is calculated through an algorithm called backpropagation. During training, the model looks at the difference between the predicted output as compared to the expected output to compute the cost, or amount of error. Then, the backpropagation algorithm computes a gradient backwards from output to input, indicating how much the output would change if each parameter was to be adjusted by a small amount. In the same way we calculated the derivatives for multiple input variables in our physics example, here we're calculating the derivatives of the amount of loss for cost, activation, and bias for each node.

PyTorch has a build in differentiation algorithm to compute gradients for any computational graph called *torch.autograd*. This is how neural networks are tuned and optimized to desired effect.