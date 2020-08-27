from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int
    username: str
    email: str

    def __str__(self):
        return self.username


@dataclass
class Projects:
    id: int
    name: str
    user_id: int
    parent: User
    created_at: datetime

    def __str__(self):
        return self.name