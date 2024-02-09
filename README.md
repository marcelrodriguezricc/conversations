# MLIMS
Machine Learning for Integrating Media Systems

Works, Explorations, and Studies

After cloning the repository:

1. The "python" directory will require a virtual Python environment to run Python scripts.

    - PyTorch needs to be installed in the virtual environment by running: "pip3 install torch torchvision torchaudio" from the terminal while the virtual environment is active.

    - For some examples, the Matplotlib (https://matplotlib.org/) library for visualization with Python will also need to be installed in the virtual environment.

2. The "cpp" directory will require LibTorch (https://pytorch.org/) to run C++ applications. 

    - You may additionally have to install and move libomp.dylib in the "lib" subfolder. If you're on macOS, and have Homebrew (https://brew.sh/) installed, you can use the command "brew install libomp" from the terminal to install libomp.dylib.
