import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
from box import ConfigBox
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the yaml file.

    Raises:
        ValueError: If the yaml file is empty 
        e: cannot be read.
    Returns:
        ConfigBox: ConfigBox object containing the contents of the yaml file.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories given in the list.

    Args:
        path_to_directories (list): List of paths to directories to be created.
        verbose (bool, optional): If True, logs the creation of directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):  
    """
    Saves a dictionary as a JSON file.

    Args:
        path (Path): Path where the JSON file will be saved.
        data (dict): Dictionary to be saved as JSON.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads a JSON file and returns its contents as a ConfigBox object.

    Args:
        path (Path): Path to the JSON file.
    
    Returns:
        ConfigBox: ConfigBox object containing the contents of the JSON file.
    """
    with open(path, "r") as f:
        content = json.load(f)
    logger.info(f"JSON file loaded from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves data as a binary file using joblib.

    Args:
        data (Any): Data to be saved.
        path (Path): Path where the binary file will be saved.
    """
    joblib.dump(data, path)
    logger.info(f"Binary file saved at: {path}")    

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads a binary file using joblib and returns its contents.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Contents of the binary file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the size of the file at the given path in kilobytes.

    Args:
        path (Path): Path to the file.

    Returns:
        str: Size of the file in kilobytes
    """
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    logger.info(f"Size of the file at {path} is {size_in_kb} KB")
    return f"{size_in_kb} KB"   

@ensure_annotations
def decodeImage(imgstring, fileName):
    """
    Decodes a base64 encoded image string and saves it as an image file.

    Args:
        imgstring (str): Base64 encoded image string.
        fileName (str): Name of the file to save the decoded image.
    """
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
    logger.info(f"Image decoded and saved as {fileName}")
    f.close()

@ensure_annotations
def encodeImageIntoBase64(imagePath):
    """
    Encodes an image file into a base64 string.

    Args:
        imagePath (str): Path to the image file.

    Returns:
        str: Base64 encoded string of the image.
    """
    with open(imagePath, "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    logger.info(f"Image at {imagePath} encoded into base64 string")
    return my_string            