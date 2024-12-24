import os


def get_file_path(file_name):
    """Retrieves the file path, starting at the project root."""
    project_root = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    file_path = os.path.join(project_root, file_name)
    absolute_path = os.path.abspath(file_path)
    return absolute_path