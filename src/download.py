from pathlib import Path
from typing import Optional


def download_dir(dir: str = "download") -> Optional[str]:
    path = Path(dir)
    if path.is_file():
        return None

    if not path.exists():
        path.mkdir()
        return str(path.resolve())

    # 既存のディレクトリ
    for content in path.iterdir():
        if content.is_file():
            content.unlink()
        elif content.is_dir():
            __deep_rmdir(content)
    return str(path.resolve())


def __deep_rmdir(path: Path):
    if path.is_dir():
        for content in path.iterdir():
            if content.is_file():
                content.unlink()
            elif content.is_dir():
                __deep_rmdir(content)
        path.rmdir()
