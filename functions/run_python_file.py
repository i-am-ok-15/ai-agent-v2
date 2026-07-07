import os
import sys
import subprocess
from functions.file_paths import abs_target_path, abs_working_path

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:

    try:
        working_path = abs_working_path(working_directory)
        target_path = abs_target_path(working_directory, file_path)

        if os.path.commonpath([working_path, target_path]) != working_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if file_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_path]
        if args:
            for arg in args:
                if arg not in command:
                    command.extend(arg)

        completed_process = subprocess.run(command, cwd=working_path, capture_output=True, text=True, timeout=30)
        
        output_string = ""
        if completed_process.returncode != 0:
            output_string += f"Process exited with code {completed_process.returncode}\n"
        if not completed_process.stdout and not completed_process.stderr:
            output_string += "No output produced"
        else:
            output_string += f"STDOUT: {completed_process.stdout}\n"
            output_string += f"STDERR: {completed_process.stderr}"
        return output_string

    except Exception as e:
        return f"Error: executing Python file: {e}"
