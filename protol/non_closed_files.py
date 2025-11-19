from typing import IO

def non_closed_files(files: list[IO]) -> list[str]:
    return [file for file in files if not file.closed]
