def log_for(logfile: str, date_str: str) -> None:
    with open(
        f"log_for_{date_str}.txt", mode="w", encoding="utf-8"
    ) as output_file, open(logfile, encoding="utf-8") as input_file:
        for string in input_file:
            if date_str in string:
                output_file.write(string[string.index(date_str) + len(date_str) + 1 :])
