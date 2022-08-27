from pathlib import Path 


def solution():
    filepath = Path("inputdata.txt")
    data = filepath.read_text().splitlines()
    # data = [199,
    #         200,
    #         208,
    #         210,
    #         200,
    #         207,
    #         240,
    #         269,
    #         260,
    #         263]
    counter = 0
    for idx in range(1, len(data)):
        counter += 1 if int(data[idx]) > int(data[idx - 1]) else 0
    print(counter)
solution()