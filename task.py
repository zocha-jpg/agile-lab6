from dataclasses import dataclass, asdict, field
from datetime import datetime


VALID_STATUSES = ("Todo", "InProgress", "Done")


@dataclass
class Task:
    id: int
    title: str
    status: str = "Todo"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))

    def move(self, new_status: str) -> None:
        if new_status not in VALID_STATUSES:
            raise ValueError(f"Invalid status '{new_status}'. Allowed: {VALID_STATUSES}")
        self.status = new_status

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(**data)
