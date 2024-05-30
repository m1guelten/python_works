

from constants import SQUARE_HEIGHT, SQUARE_WIDTH
from utils import generate_position


def random_choice(a):
    return 15


def test_generate_position(mocker):
    mocker.patch("random.choice", random_choice)
    result = generate_position()
    assert result == (random_choice(1) * SQUARE_WIDTH, random_choice(1) * SQUARE_HEIGHT)
