# From https://pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html

# Import:
import torch # Import the PyTorch library.
import torchvision.models as models # Import the models module from the torchvision library.

# Loading and Saving Model Weights:
model = models.vgg16(weights='IMAGENET1K_V1') # Load the pre-trained VGG16 model from the torchvision library.
torch.save(model.state_dict(), 'model_weights.pth') # Save the model weights to a file named "model_weights.pth".

model = models.vgg16() # Create an untrained instance of the VGG16 model.
model.load_state_dict(torch.load('model_weights.pth')) # Load the model weights from the file "model_weights.pth".
model.eval() # Set the model to evaluation mode.

torch.save(model, 'model.pth')  # Save model with structure, as opposed to just weights.
model = torch.load('model.pth') # Then the model can be loaded with the structure and weights.