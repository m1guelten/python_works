from unittest import TestCase
from main import field_start, game_start_data
width, height = 6, 6
# test_arr_game = field_start()
# print(test_arr_game)


class TestGame(TestCase):
    def test_field_get(self):
        test_arr_game = field_start()
        self.assertEqual(test_arr_game[2][2], 0)
        self.assertEqual(test_arr_game[2][3], 0)
        self.assertEqual(test_arr_game[2][4], 0)
    def



