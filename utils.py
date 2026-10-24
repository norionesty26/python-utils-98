import os
import shutil
from typing import Union, List
from pathlib import Path

def ensure_directory(path: Union[str, Path]) -> Path:
    dir_path = Path(path)
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path

def clean_directory(path: Union[str, Path]) -> None:
    target = Path(path)
    if target.exists():
        for item in target.iterdir():
            if item.is_file() or item.is_symlink():
                item.unlink()
            elif item.is_dir():
                shutil.rmtree(item)

def get_file_list(directory: Union[str, Path], extension: str = "*") -> List[Path]:
    return list(Path(directory).glob(f"*.{extension.lstrip('.')}"))

def safe_remove(path: Union[str, Path]) -> bool:
    try:
        target = Path(path)
        if target.is_file() or target.is_symlink():
            target.unlink()
            return True
        return False
    except OSError:
        return False

def format_byte_size(size: int, suffix: str = 'B') -> str:
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti']:
        if size < 1024:
            return f"{size:.2f} {unit}{suffix}"
        size /= 1024
    return f"{size:.2f} Pi{suffix}"