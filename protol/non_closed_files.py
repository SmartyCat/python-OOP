def non_closed_files(files: list[str]) -> list[str]:
    return [file for file in files if not file.closed]
