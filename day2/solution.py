from pathlib import Path


class DayTwoSolution:

    def __init__(self) -> None:
        self.filepath = Path("input_data.txt")
        self.data = self.filepath.read_text().splitlines()
        self.horizontal = 0
        self.vertical = 0

    def handle_update(self, direction, delta):
        mapping = dict(
            forward="+",
            down="+",
            up="-"
        )
        if direction == "forward":
            self.adjust_horizontal()

    def adjust_horizontal(self, delta):
        self.horizontal += delta

    def adjust_vertical(self, delta):
        self.vertical += delta

    def navigation(self) -> None:
        for inp in self.data:
            direction, delta = inp.split(" ")
            print(inp)


solution = DayTwoSolution()
solution.navigation()
