import os
import json
import base64
import joblib

from pathlib import Path
from typing import Any

import yaml
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError

from thorax_ai.utils.logger import logger


# ============================================================
# 1. READ YAML FILE
# ============================================================

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox.
    """

    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)

            logger.info(f"YAML file loaded successfully: {path_to_yaml}")

            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("YAML file is empty")

    except Exception as e:
        raise e


# ============================================================
# 2. CREATE DIRECTORIES
# ============================================================

@ensure_annotations
def create_directories(
    path_to_directories: list,
    verbose: bool = True
):
    """
    Creates directories if they do not already exist.
    """

    for path in path_to_directories:

        os.makedirs(path, exist_ok=True)

        if verbose:
            logger.info(f"Created directory at: {path}")


# ============================================================
# 3. SAVE JSON
# ============================================================

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves dictionary data into a JSON file.
    """

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"JSON file saved at: {path}")


# ============================================================
# 4. LOAD JSON
# ============================================================

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads JSON file and returns it as ConfigBox.
    """

    with open(path, "r") as f:
        content = json.load(f)

    logger.info(f"JSON file loaded from: {path}")

    return ConfigBox(content)


# ============================================================
# 5. SAVE BINARY FILE
# ============================================================

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves Python object/model into a binary file using joblib.
    """

    joblib.dump(data, path)

    logger.info(f"Binary file saved at: {path}")


# ============================================================
# 6. LOAD BINARY FILE
# ============================================================

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads a binary file using joblib.
    """

    data = joblib.load(path)

    logger.info(f"Binary file loaded from: {path}")

    return data


# ============================================================
# 7. GET FILE SIZE
# ============================================================

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns file size in KB.
    """

    size_in_kb = round(os.path.getsize(path) / 1024)

    return f"~ {size_in_kb} KB"


# ============================================================
# 8. DECODE BASE64 IMAGE
# ============================================================

def decodeImage(imgstring, fileName):
    """
    Decodes a Base64 encoded image and saves it to a file.
    """

    imgdata = base64.b64decode(imgstring)

    with open(fileName, "wb") as f:
        f.write(imgdata)

    logger.info(f"Image decoded and saved at: {fileName}")


# ============================================================
# 9. ENCODE IMAGE INTO BASE64
# ============================================================

def encodeImageIntoBase64(croppedImagePath):
    """
    Encodes an image file into Base64.
    """

    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())