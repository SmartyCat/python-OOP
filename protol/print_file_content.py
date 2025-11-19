def print_file_content(filename: str) -> None:
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print("Файл не найден")

