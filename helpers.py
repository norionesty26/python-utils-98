import os
import shutil
from typing import List, Optional

def ensure_dir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)

def cleanup_temp_files(directory: str, pattern: Optional[str] = None) -> List[str]:
    deleted_files = []
    if not os.path.exists(directory):
        return deleted_files

    for filename in os.listdir(directory):
        if pattern and pattern not in filename:
            continue
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
                deleted_files.append(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                deleted_files.append(file_path)
        except OSError:
            continue
    return deleted_files

def get_file_stats(path: str) -> dict:
    stat = os.stat(path)
    return {
        'size': stat.st_size,
        'mode': oct(stat.st_mode),
        'modified': stat.st_mtime
    }

def list_files_recursive(directory: str) -> List[str]:
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list