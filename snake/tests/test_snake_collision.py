import pytest

from apple import Apple
from snake import Snake
from snake_collision import apple_collision, wall_collision


@pytest.fixture(scope="function")
def apple(request):
    return Apple(request.param)


@pytest.fixture(scope="function")
def snake(request):
    return Snake(request.param)


@pytest.mark.parametrize(
    ("snake", "result"),
    [
        ((120, 120), True),
        ((-30, 120), False),
        ((30, -30), False),
        ((1000, 120), False),
        ((30, 1200), False),
    ],
    indirect=["snake"],
)
def test_wall_collision(snake, result):
    assert wall_collision(snake) is result


@pytest.mark.parametrize(
    ("snake", "apple", "result"),
    [
        ((120, 120), (120, 120), True),
        ((90, 120), (180, 90), False),
        ((30, 60), (180, 120), False),
    ],
    indirect=["snake", "apple"],
)
def test_apple_collision(snake, apple, result):
    assert apple_collision(snake, apple) is result
