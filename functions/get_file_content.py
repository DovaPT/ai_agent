import os

MAX_CHARS = 10000


def get_file_content(working_directory, file_path):
    working_path = os.path.abspath(working_directory)
    real_file_path = os.path.abspath(
        os.path.abspath(os.path.join(working_path, file_path))
    )
    if working_path not in real_file_path:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(real_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    with open(real_file_path, "r") as f:
        contents = f.read(MAX_CHARS)
        if len(f.read()) > MAX_CHARS:
            contents += f'\n[...File "{file_path}" truncated at 10000 characters]'
    return contents
