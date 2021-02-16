from dataclasses import dataclass


@dataclass
class Patient:
    name: str
    ailment: str

    def __lt__(self, other):
        return False
