import os

def custom_path(script_dir, file_name) -> str:
    parent_dir = os.path.split(script_dir)[0]
    file_path = os.path.join(parent_dir, file_name)
    return  file_path