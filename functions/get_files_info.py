import os


def get_files_info(working_directory, directory=None):
    working_path = os.path.abspath(working_directory)
    if directory is None:
        directory = "."
    real_path = os.path.realpath(os.path.join(working_path, directory))

    if working_path not in real_path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if os.path.isdir(real_path):
        lst_dir = os.listdir(real_path)
    else:
        return f'Error: "{directory}" is not a directory'

    out = []
    for item in lst_dir:
        item_path = os.path.join(real_path, item)
        is_dir = os.path.isdir(item_path)
        file_size = os.path.getsize(item_path)
        out.append(f"- {item}: file_size={file_size}, is_dir={is_dir}")

    return "\n".join(out)
