from dataclasses import dataclass
from datetime import datetime


@dataclass
class Projects:
    id: int
    name: str
    user_id: int
    created_at: datetime

    def __str__(self):
        return self.name


@dataclass
class User:
    id: int
    username: str
    email: str

    def __str__(self):
        return self.username