import os
import subprocess


def run_python_file(working_directory, file_path):
    working_path = os.path.abspath(working_directory)
    real_file_path = os.path.abspath(
        os.path.abspath(os.path.join(working_path, file_path))
    )
    if working_path not in real_file_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    elif not os.path.exists(real_file_path):
        return f'Error: File "{file_path}" not found'
    elif not real_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        run_info = subprocess.run(
            ["python3", os.path.relpath(real_file_path)],
            capture_output=True,
            timeout=30,
        )
    except Exception as e:
        return f"Error: executing Python file: {e}"

    out = ""
    if run_info.stdout:
        out += f"STDOUT: {run_info.stdout.decode()}\n"
    if run_info.stderr:
        out += f"STDERR: {run_info.stderr.decode()}\n"
    if run_info.returncode != 0:
        out += f"Proccess exited with code {run_info.returncode}\n"
    if len(out) == 0:
        out = "No output produced."

    return out
