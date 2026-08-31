import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes or runs a Python script (.py file) in the working directory and returns its output.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Relative path to the Python file to execute (e.g. 'main.py').",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional command-line arguments to pass to the script.",
                },
            },
            "required": ["file_path"],
        },
    },
}

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        abs_file_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_file_path, file_path))
        valid_target_file = os.path.commonpath([abs_file_path, target_file]) == abs_file_path
        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_file]
        if args:
            command.extend(args)
        completed_process = subprocess.run(command,cwd=abs_file_path, capture_output=True, text=True, timeout=30)

        output = []
        if completed_process.returncode != 0:
            output.append(f"Process exited with code {completed_process.returncode}")

        stdout_content = completed_process.stdout
        stderr_content = completed_process.stderr
        if not stdout_content and not stderr_content:
            output.append("No output produced")
        else:
            if stdout_content:
                output.append(f"STDOUT:\n{stdout_content}")
            if stderr_content:
                output.append(f"STDERR:\n{stderr_content}")
        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"