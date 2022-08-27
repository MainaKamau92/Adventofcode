from pathlib import Path


class DayOneSolution:

    def __init__(self) -> None:
        self.filepath = Path("inputdata.txt")
        self.data = self.filepath.read_text().splitlines()
        self.counter = 0

    def part1(self) -> int:
        for idx in range(1, len(self.data)):
            self.counter += 1 if int(self.data[idx]) > int(self.data[idx - 1]) else 0
        return self.counter

    def part2(self) -> int:
        for idx in range(0, len(self.data)):
            self.counter += 1 if sum(list(map(lambda x: int(x), self.data[idx:idx + 3]))) < sum(
                list(map(lambda x: int(x), self.data[idx + 1:idx + 4]))) else 0
        return self.counter


if __name__ == "__main__":
    inst = DayOneSolution()
    print(inst.part2())
