# DATASETS

A data set is quite simply a collection of data organized into a structure. They're usually taken from a specific source for a corresponding purpose. They can be accessed for training and tuning machine learning models in pattern recognition in analytical and predictive processes.

PyTorch allows users to implement data sets with two primitives:

1. Dataset (torch.utils.data.Dataset) which stores the samples and corresponding labels.

2. DataLoader (torch.utils.data.DataLoader): wraps an iterable around the dataset to allow easy access to samples.

These allow the user to use pre-loaded datasets, as well as ones of their own creation.
