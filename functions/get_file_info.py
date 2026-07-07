import os
from functions.file_paths import abs_target_path, abs_working_path

def get_files_info(working_directory: str, directory: str = ".") -> str:

    try:
        working_path = abs_working_path(working_directory)
        target_path = abs_target_path(working_directory, directory)

        if os.path.commonpath([working_path, target_path]) != working_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_path):
            return f'Error: "{directory}" is not a directory'

        if directory == ".":
            info_string = ["Result for current directory:"]         
        else:
            info_string = [f"Result for '{directory}' directory:"]

        file_info_list = os.listdir(target_path)
        for file in file_info_list:
            try:
                file_path = abs_target_path(target_path, file)
                info_string.append(f"- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}")
            except Exception as e:
                info_string.append(f"Error: {e}")
        return "\n".join(info_string)
    
    except Exception as e:
        return f"Error: {e}"

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}