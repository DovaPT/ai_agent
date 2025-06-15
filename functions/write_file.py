import os


def write_file(working_directory, file_path, content):
    working_path = os.path.abspath(working_directory)
    real_file_path = os.path.abspath(
        os.path.abspath(os.path.join(working_path, file_path))
    )
    if working_path not in real_file_path:
        return f'Error: Cannot write to  "{file_path}" as it is outside the permitted working directory'
    with open(real_file_path, "w") as f:
        f.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
