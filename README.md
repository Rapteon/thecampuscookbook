# The Campus Cookbook

A user-friendly online platform for viewing and posting recipes effortlessly.

## Setup for development

### Install the following software

1. VSCode
2. Anaconda or Miniconda. Ensure you can run the `conda` command through your terminal.
3. Git

### Setup conda environment

1. Navigate to the checked-out repository folder: `cd thecampuscookbook`
2. Run the command: `conda env create`. This will use the **environment.yml** file  
to create the development environment.
3. Activate the conda environment using the command: `conda activate cookbook`

### Setup pre-commit hook for auto-formatting code.

1. Ensure the conda environent for the project is activated. Check the section for creating  
a Conda environment.
2. Run the command `pre-commit install` if activating your environment for the first time.
3. Autoformatting of Python code happens when you commit your code using `git commit`.
In case the formatter decides the code is not formatted, you will see a *failed* message after  
trying to commit the changes. This means the file has been formatted, but your changes  
have not been committed. After the *failed* message, simply commit the changes again.
4. If you would like to run the formatter manually, you can run it like `black <file_name>.py`.

### Other Conda options

#### Updating Conda environment

1. Create a new environment with the required dependencies:
`conda create -n cookbook python==3.11 django pillow black pre-commit`
2. Navigate to the checked-out repository and export the environment.:
`conda env export -n cookbook --ignore-channels --from-history -f environment.yml` 
3. Commit the **environment.yml** file to version control. Ensure that it does
not have platform-specific dependencies.

#### Removing a Conda environment

1. Deactivate the environment by running: `conda deactivate`
2. Remove the environment by running: `conda env remove -n cookbook`
