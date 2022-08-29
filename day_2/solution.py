from pathlib import Path
from typing import List


class DayTwoSolution:

    def __init__(self) -> None:
        self.filepath = Path("input_data.txt")
        self.data: List[str] = self.filepath.read_text().splitlines()
        self.horizontal: int = 0
        self.vertical: int = 0
        self.aim: int = 0

    def handle_update(self, direction: str, delta: str) -> None:
        mapping = dict(
            forward="+",
            down="+",
            up="-"
        )
        if direction == "forward":
            self.adjust_horizontal(int(f"{mapping[direction]}{delta}"))
            self.adjust_vertical(int(f"{mapping[direction]}{self.aim * int(delta)}"))
        else:
            # self.adjust_vertical(int(f"{mapping[direction]}{delta}")) uncomment for part 1
            self.adjust_aim(int(f"{mapping[direction]}{delta}"))

    def adjust_horizontal(self, delta: int) -> None:
        self.horizontal += delta

    def adjust_vertical(self, delta: int) -> None:
        self.vertical += delta

    def adjust_aim(self, delta: int) -> None:
        self.aim += delta

    def solution(self) -> int:
        for inp in self.data:
            direction, delta = inp.split(" ")
            self.handle_update(direction, delta)
        return self.horizontal * self.vertical


solution = DayTwoSolution()
print(solution.solution())
