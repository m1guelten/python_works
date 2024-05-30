import pytest

from snake import Snake


@pytest.fixture(scope="function")
def snake(request):
    return Snake(request.param)


@pytest.mark.parametrize(
    ("snake", "vector", "result"),
    [
        ((120, 120), "UP", (120, 90)),
        ((120, 120), "DOWN", (120, 150)),
        ((120, 120), "LEFT", (90, 120)),
        ((120, 120), "RIGHT", (150, 120)),
    ],
    indirect=["snake"],
)
def test_move(snake, vector, result):
    # snake = Snake(koord)
    snake.vector = vector
    # snake.x, snake.y = koord[0], koord[1]
    snake.move()
    assert snake.x == result[0] and snake.y == result[1]


@pytest.mark.parametrize(
    ("snake", "result"),
    [((120, 120), True), ((300, 300), True), ((120, 120), True), ((300, 90), False)],
    indirect=["snake"],
)
def test_collision_myself(snake, result):
    snake.tail = [
        {"x": 300, "y": 120},
        {"x": 300, "y": 150},
        {"x": 330, "y": 150},
        {"x": 330, "y": 120},
        {"x": 330, "y": 90},
        {"x": 300, "y": 90},
        {"x": 270, "y": 90},
    ]
    assert snake._collision_myself() == result


@pytest.mark.parametrize(
    ("snake", "tail", "result"),
    [
        (
            (270, 120),
            [{"x": 300, "y": 120}, {"x": 330, "y": 120}],
            [{"x": 330, "y": 120}, {"x": 270, "y": 120}],
        ),
        (
            (420, 120),
            [{"x": 330, "y": 120}, {"x": 360, "y": 120}, {"x": 390, "y": 120}],
            [{"x": 360, "y": 120}, {"x": 390, "y": 120}, {"x": 420, "y": 120}],
        ),
    ],
    indirect=["snake"],
)
def test_rewrite_tail(snake, tail, result):
    snake.tail = tail
    snake.rewrite_tail()
    assert snake.tail == result
