from pathlib import Path 


def solution():
    filepath = Path("inputdata.txt")
    data = filepath.read_text().splitlines()
    counter = 0
    for idx in range(1, len(data)):
        counter += 1 if int(data[idx]) > int(data[idx - 1]) else 0
    return counter
solution()