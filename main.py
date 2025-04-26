def remove_invalid_lines(document):
    split_lines = document.split("\n")
    print(f"Split: {split_lines}")
    filtered_lines = filter(lambda line: not line.startswith("-"), split_lines)
    print(f"Filtered: {filtered_lines}")
    results = "\n".join(filtered_lines)
    return results