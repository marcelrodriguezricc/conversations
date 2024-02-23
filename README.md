# Conversations with my Computer

Works, explorations, and studies into machine learning for integrating media systems by Marcel Rodriguez-Riccelli.

After cloning the repository:

1. Python Dependencies:

    - A virtual environment will need to be created in the cloned repository, where "ENV-NAME" is the name of your choosing for your virtual environment.

        - Here's an example using [Conda](https://docs.conda.io/projects/conda/en/stable/#):

            - ``` conda create -name "ENV-NAME" ```

    - [PyTorch](https://pytorch.org/) library for machine learning.

        - Activate the virtual environment, where "ABSOLUTE-PATH" is the absolute path to your virtual environment:

            - ``` conda activate "ABSOLUTE-PATH" ```

        - Run the following to install PyTorch inside of the virtual environment:

            -   ``` conda install torch torchvision torchaudio ```

    - [Matplotlib](https://matplotlib.org/) library for data visualization.
            
        - Activate the virtual environment, where "ABSOLUTE-PATH" is the absolute path to your virtual environment:

            - ``` conda activate "ABSOLUTE-PATH" ```

        - Run the following to install Matplotlib inside of the virtual environment:
            
            - ``` conda install matplotlib ```

    - [Pandas](https://pandas.pydata.org/) library for data analysis and manipulation.

        - Activate the virtual environment, where "ABSOLUTE-PATH" is the absolute path to your virtual environment:

            - ``` conda activate "ABSOLUTE-PATH" ```
        
        - Run the following to install Pandas inside of the virtual environment:

            - ``` conda install pandas ```


2. C++ Dependencies:

    - [LibTorch](https://pytorch.org/), a PyTorch library for C++.

        - [Download LibTorch here](https://pytorch.org/get-started/locally/) and move it to the "cpp" directory.

        - MacOS users should install libomp.dylib and move it to the "lib" subfolder of the "libtorch" directory using [Homebrew](https://brew.sh/):

            - ``` brew install libomp ```

3. Submodules:

    - Get all submodules for the repository.

        - ``` git submodule update --init --recursive ```