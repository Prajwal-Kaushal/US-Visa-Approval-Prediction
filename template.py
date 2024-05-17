import os
from pathlib import Path

project_name = "us_visa" # root folder name
list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml"
]
# to install it as local file we need to have a __init__.py file in the root folder

for filepath in list_of_files:
    filepath = Path(filepath) # converting the list_of_files to Path object, because it is a path and in windows path is given by \ to avoit any issue i did this
    filedir, filename = os.path.split(filepath) # my list contains all the files and folders in the root folder, so i need to split the path to get the folder name and file name
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # checking if the folder is already present or not, if not then create the folder
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # checking if the file is already present or not, if not then create the file
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")