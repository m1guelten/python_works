import pytest

from runner import speed_game
from snake import Snake


@pytest.fixture(scope="function")
def snake(request):
    return Snake(request.param)


@pytest.mark.parametrize(
    ("snake", "tail", "result"),
    [
        ((100, 100), [{"x": 300, "y": 120}, {"x": 330, "y": 120}], 40),
        (
            (100, 100),
            [
                {"x": 300, "y": 120},
                {"x": 300, "y": 120},
                {"x": 300, "y": 120},
                {"x": 330, "y": 120},
            ],
            30,
        ),
    ],
    indirect=["snake"],
)
def test_speed_game(snake, tail, result):
    snake.tail = tail
    assert speed_game(snake) == result
