import demoqa
import os
from pathlib import Path


def resourse(path):
    file_path = str(Path(demoqa.__file__)
                    .parent
                    .parent
                    .joinpath(f'resources/{path}'))
    return os.path.abspath(file_path)
