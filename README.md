# MLIMS
Machine Learning for Integrating Media Systems

Works, Explorations, and Studies

After cloning the repository:

1. Python Dependencies:

    - A virtual environment will need to be created in the cloned repository.

        - Here's an example using Conda (https://docs.conda.io/projects/conda/en/stable/#):

            - ``` conda create -n env-01 python=3.9 scipy=0.15.0 numpy ```

    - PyTorch (https://pytorch.org/).

        - Activate the virtual environment, where "ABOLSUTE-PATH-TO-YOUR-ENVRIONMENT":

            - ``` conda activate "ABSOLUTE-PATH-TO-YOUR-EVIRONMENT" ```

        - Then run the following to install PyTorch on the virtual envrionment:

            -   ``` pip3 install torch torchvision torchaudio ```

    - Matplotlib (https://matplotlib.org/) library for data visualization.
            
        - Activate the virtual environment, where "ABOLSUTE-PATH" is the absolute path to your virtual envrionment:

            - ``` conda activate "ABSOLUTE-PATH" ```

        - Then run the following to install Matplotlib:
            
            - ``` conda install matplotlib ```

    - Jupyter Lab (https://jupyter.org/) development environment.

        - Activate the virtual environment, where "ABOLSUTE-PATH" is the absolute path to your virtual envrionment:

            - ``` conda activate "ABSOLUTE-PATH" ```
            
         - Then run the following to install Jupyter Lab:

            - ``` pip install jupyterlab ```


2. C++ Dependencies:

    - LibTorch (https://pytorch.org/), a PyTorch library for C++.

        - Download LibTorch at https://pytorch.org/get-started/locally/ and move it to the "cpp" directory.

        - MacOS users should install libomp.dylib and move it to the "lib" subfolder of the "libtorch" directory using Homebrew (https://brew.sh/):

            - ``` brew install libomp ```