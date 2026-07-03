import os

def get_files_info(working_directory: str, directory: str = ".") -> str:

    try:
        abs_working_path = os.path.abspath(working_directory)
        abs_target_path = os.path.normpath(os.path.join(abs_working_path, directory))

        if os.path.commonpath([abs_working_path, abs_target_path]) != abs_working_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(abs_target_path):
            return f'Error: "{directory}" is not a directory'
        return f'Success: "{directory}" is within the working directory'
    except Exception as e:
        return f"Error: {e}"