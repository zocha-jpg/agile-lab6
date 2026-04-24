import json
from pathlib import Path
from typing import List

from task import Task
from board import Board


DEFAULT_PATH = Path("board.json")


def load(path: Path = DEFAULT_PATH) -> Board:
    if not path.exists():
        return Board()
    raw = json.loads(path.read_text(encoding="utf-8"))
    tasks: List[Task] = [Task.from_dict(d) for d in raw.get("tasks", [])]
    return Board(tasks)


def save(board: Board, path: Path = DEFAULT_PATH) -> None:
    payload = {"tasks": [t.to_dict() for t in board.tasks]}
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
