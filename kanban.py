import argparse
import sys

import storage


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="kanban", description="Kanban Board CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_add = sub.add_parser("add", help="Dodaj zadanie")
    p_add.add_argument("title")

    p_move = sub.add_parser("move", help="Zmien status zadania")
    p_move.add_argument("task_id", type=int)
    p_move.add_argument("status", choices=["Todo", "InProgress", "Done"])

    p_rm = sub.add_parser("rm", help="Usun zadanie")
    p_rm.add_argument("task_id", type=int)

    sub.add_parser("show", help="Wyswietl tablice")

    args = parser.parse_args(argv)
    board = storage.load()

    if args.cmd == "add":
        t = board.add(args.title)
        print(f"Dodano #{t.id}: {t.title}")
    elif args.cmd == "move":
        t = board.move(args.task_id, args.status)
        print(f"#{t.id} -> {t.status}")
    elif args.cmd == "rm":
        board.remove(args.task_id)
        print(f"Usunieto #{args.task_id}")
    elif args.cmd == "show":
        print(board.render())

    storage.save(board)
    return 0


if __name__ == "__main__":
    sys.exit(main())
