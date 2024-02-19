# TENSORS

Tensors are a class defined by PyTorch to store and operate on multi-dimensional arrays of numbers. They're used as the to allow neural networks to do work on complex data sets.

They can be used in several ways:
 
1. Unit Values: Tensors can be used in place of unit values such as scalars, arrays, or matricies, In this way, tensors can express higher dimensionalities. This enables learning of complex data types, such as images or videos.

2. Fully Connected Layers: Tensors can be used in place of entire layers of nodes, containing all of the units, weights, and baises for an entire layer. This allows for efficient computation of gradients when applying techniques like backpropagation.

Tensors are specifically designed to be able to be operated on by parallel processing units such as a GPU or TPU to expidite calculation.

Tensor decomposition, or representing a tensor as a sum of more simple tensors, can be used to extract meaningful patterns from complex multidimensional data.