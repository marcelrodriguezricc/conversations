# MLIMS
Machine Learning for Integrating Media Systems

Works, Explorations, and Studies

After cloning the repository:

1. Python Dependencies:

    - A virtual environment will need to be created in the cloned repository.

        - Here's an example using [Conda](https://docs.conda.io/projects/conda/en/stable/#):

            - ``` conda create -n env-01 python=3.9 scipy=0.15.0 numpy ```

    - [PyTorch](https://pytorch.org/) library for machine learning.

        - Activate the virtual environment, where "ABOLSUTE-PATH" is the absolute path to your virtual envrionment:

            - ``` conda activate "ABSOLUTE-PATH" ```

        - Run the following to install PyTorch inside of the virtual envrionment:

            -   ``` conda install torch torchvision torchaudio ```

    - [Matplotlib](https://matplotlib.org/) library for data visualization.
            
        - Activate the virtual environment, where "ABOLSUTE-PATH" is the absolute path to your virtual envrionment:

            - ``` conda activate "ABSOLUTE-PATH" ```

        - Run the following to install Matplotlib inside of the virtual environment:
            
            - ``` conda install matplotlib ```

    - [Pandas](https://pandas.pydata.org/) library for data analysis and manipulation.

        - Activate the virtual environment, where "ABOLSUTE-PATH" is the absolute path to your virtual envrionment:

            - ``` conda activate "ABOLUTE-PATH" ```
        
        - Run the following to install Pandas inside of the virtual environment:

            - ``` conda install pandas ```


2. C++ Dependencies:

    - [LibTorch](https://pytorch.org/), a PyTorch library for C++.

        - [Download LibTorch here](https://pytorch.org/get-started/locally/) and move it to the "cpp" directory.

        - MacOS users should install libomp.dylib and move it to the "lib" subfolder of the "libtorch" directory using [Homebrew](https://brew.sh/):

            - ``` brew install libomp ```