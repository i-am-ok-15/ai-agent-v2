import os
from functions.file_paths import abs_target_path, abs_working_path

def get_file_info(working_directory: str, directory: str = ".") -> str:

    try:
        working_path = abs_working_path(working_directory)
        target_path = abs_target_path(working_directory, directory)

        if os.path.commonpath([working_path, target_path]) != working_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_path):
            return f'Error: "{directory}" is not a directory'
        return f'Success: "{directory}" is within the working directory'
    except Exception as e:
        return f"Error: {e}"