import os
from functions.file_paths import abs_target_path, abs_working_path

def write_file(working_directory: str, file_path: str, content: str) -> str:

    try:
        working_path = abs_working_path(working_directory)
        target_path = abs_target_path(working_directory, file_path)

        if os.path.commonpath([working_path, target_path]) != working_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(target_path), exist_ok=True)

        with open(target_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"
    
schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Opens a file in write mode and then overwrites it with some content.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The file_path of the file to be overwriten with content.",
                },
                "content": {
                    "type": "string",
                    "description": "The content to be written into the target file path.",
                }
            },
            "required": ["file_path"],
        },
    },
}