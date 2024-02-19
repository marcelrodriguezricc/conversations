# GRADIENTS

In physics, a gradient is represented as a vector with a magnitude that quantifies a change in the value per unit distance. For example, if we wanted to observe the temperature gradient in a room, we might see how much the temperature changes from each square foot in the room. We divide the room up into square feet. We then draw an arrow which represents our gradient through the box from the neighboring box with the temperature to the neighboring box with the highest. The magnitude is the overall change in temperature across the footlong arrow, and the direction points from the lowest to the highest, giving the vector of our gradient.

We can also understand this in terms of derivatives. A derivative is the rate of change between two points in a function. A gradient is a derivative with more than one input variable. In the previous example, there are three input variables: the two dimensions of the room and the temperature. In machine learning, we're often dealing with more than one variable.

In machine learning, gradients can be described as the to the amount of error with respect to the weights and biases of each node. The gradient is calculated through an algorithm called backpropagation. During training, the model looks at the difference between the predicted output as compared to the expected output. Then, the backpropagation algorithm computes a gradient backwards from output to input, indicating how much the output would change if each parameter was to be adjusted by a small amount.

Using an optimization algorithm, the parameters are adjusted opposite to the gradient in a process called gradient descent. The amount by which the parameters are adjusted are controled by the learning rate. Too large a learning rate will cause the algorithm to overcorrect, while a small learning rate will slow the process all together.

This entire process is performed iteratively until the amount of error is at a sufficient level.