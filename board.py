from typing import List
from task import Task, VALID_STATUSES


class Board:
    def __init__(self, tasks: List[Task] | None = None):
        self.tasks: List[Task] = tasks or []

    def add(self, title: str) -> Task:
        next_id = max((t.id for t in self.tasks), default=0) + 1
        task = Task(id=next_id, title=title)
        self.tasks.append(task)
        return task

    def move(self, task_id: int, status: str) -> Task:
        task = self._find(task_id)
        task.move(status)
        return task

    def remove(self, task_id: int) -> None:
        task = self._find(task_id)
        self.tasks.remove(task)

    def render(self) -> str:
        # BUG (v1.0): przy pustej liscie max() rzuca ValueError
        width = max(len(t.title) for t in self.tasks) + 4
        lines = []
        header = " | ".join(s.center(width) for s in VALID_STATUSES)
        lines.append(header)
        lines.append("-" * len(header))

        columns = {s: [t for t in self.tasks if t.status == s] for s in VALID_STATUSES}
        depth = max(len(col) for col in columns.values())
        for i in range(depth):
            row = []
            for s in VALID_STATUSES:
                col = columns[s]
                cell = f"#{col[i].id} {col[i].title}" if i < len(col) else ""
                row.append(cell.ljust(width))
            lines.append(" | ".join(row))
        return "\n".join(lines)

    def _find(self, task_id: int) -> Task:
        for t in self.tasks:
            if t.id == task_id:
                return t
        raise KeyError(f"Task with id={task_id} not found")
