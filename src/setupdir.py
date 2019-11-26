from getpass import getuser
from pathlib import Path
from typing import Optional


def profile_dir() -> Optional[str]:
    user = getuser()
    profiles_dir = f"C:\\Users\\{user}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\"
    p = Path(profiles_dir)
    if p.is_dir():
        for profile in p.iterdir():
            if profile.is_dir():
                if "default" in profile.name.lower():
                    return str(profile)
    return None

# PROFILE = "C:\\Users\\s150209\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\5332jmf7.default"  # 会社PC
# PROFILE = "C:\\Users\\Tomoyuki Nakamura\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\2wsrx870.Default User"  # 自宅PC


def download_dir(dir: str = "download") -> Optional[str]:
    return __init_dir(dir)


def log_file(dir: str = "log") -> Optional[str]:
    log_dir = __init_dir(dir)
    if log_dir is None:
        return None

    return str(Path(log_dir).joinpath("geckodriver.log").resolve())


def __init_dir(dir: str) -> Optional[str]:
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
