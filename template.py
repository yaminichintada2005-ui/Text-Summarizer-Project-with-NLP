import os
from pathlib import Path
import logging

# Configure basic logging [2]
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s: %(levelname)s: %(message)s]' # Example format: ASCII time, level name, and message [5]
)

# Define project name and file list [6]
project_name = "text_summarizer" [6]

list_of_files = [
    # CI/CD configuration files [6], [7]
    ".github/workflows/.gitkeep", 
    
    # Source Code Structure (modular coding approach) [8], [9], [10], [11]
    f"src/{project_name}/__init__.py", # Essential for treating the folder as a local package [8]
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/utils/__init__.py", 
    f"src/{project_name}/utils/common.py", 
    f"src/{project_name}/logging/__init__.py", 
    f"src/{project_name}/config/__init__.py", 
    f"src/{project_name}/config/configuration.py", 
    f"src/{project_name}/pipeline/__init__.py", 
    f"src/{project_name}/entity/__init__.py", 
    f"src/{project_name}/constants/__init__.py", 
    
    # Configuration and Application Files [11], [3]
    "config/config.yaml",
    "params.yaml", # For model related parameters [11]
    "app.py",
    "main.py",
    "Dockerfile", # For building a Docker image for deployment [11]
    "requirements.txt", # Lists all required libraries [3]
    "setup.py", # For local package setup [3]
    
    # Notebook Experiment folder [3]
    "research/trials.ipynb", 
    "test.py"
]

# Core logic to create the directories and files [3], [4]
for filepath in list_of_files:
    # Convert path to the appropriate format based on the operating system (handling Windows backward slash vs. Linux forward slash) [4], [12]
    filepath = Path(filepath) 
    
    # Separate the directory path from the file name [13]
    filedir, filename = os.path.split(filepath) 

    if filedir != "": 
        # Create directories if they don't exist
        os.makedirs(filedir, exist_ok=True) 
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create the file only if it doesn't exist OR if it exists but is empty (size is 0) [15], [16]
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # Creates an empty file [15]
            logging.info(f"Creating empty file: {filepath}") 
    else:
        # If the file exists and is not empty, log that it is being ignored [15], [16]
        logging.info(f"{filename} is already exist") 