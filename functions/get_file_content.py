import os
from config import MAX_CHARS
from functions.get_file_info import get_file_info
from functions.file_paths import abs_target_path, abs_working_path

def get_file_content(working_directory: str, file_path: str) -> str:

    try:
        working_path = abs_working_path(working_directory)
        target_path = abs_target_path(working_directory, file_path)

        if os.path.commonpath([working_path, target_path]) != working_path:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(abs_target_path(working_directory, file_path), "r") as f:
            content = f.read(MAX_CHARS)
            if f.read(MAX_CHARS + 1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return f"{file_path} length: {len(content)}\n{file_path} truncated: {'truncated' in content}\n Truncated content: {content[:2000]}"
    except Exception as e:
        return f"Error: {e}"