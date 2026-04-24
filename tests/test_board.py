import pytest

from board import Board


def test_add_assigns_incremental_ids():
    b = Board()
    t1 = b.add("A")
    t2 = b.add("B")
    assert (t1.id, t2.id) == (1, 2)


def test_move_changes_status():
    b = Board()
    t = b.add("A")
    b.move(t.id, "InProgress")
    assert t.status == "InProgress"


def test_move_rejects_invalid_status():
    b = Board()
    t = b.add("A")
    with pytest.raises(ValueError):
        b.move(t.id, "Blocked")


def test_render_empty_board_does_not_crash():
    """Regression test dla BUG-1 (hotfix/empty-board-crash)."""
    b = Board()
    # przed hotfixem to rzucalo ValueError z max()
    output = b.render()
    assert "Todo" in output
