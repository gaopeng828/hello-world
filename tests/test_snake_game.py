import unittest

from snake_game import Direction, SnakeGame


class SnakeGameTests(unittest.TestCase):
    def test_board_too_small_raises_error(self):
        with self.assertRaises(ValueError):
            SnakeGame(width=3, height=4)

    def test_initial_state(self):
        game = SnakeGame(width=10, height=10, seed=1)
        self.assertEqual(len(game.snake), 3)
        self.assertEqual(game.direction, Direction.RIGHT)
        self.assertFalse(game.game_over)
        self.assertNotIn(game.food, game.snake)

    def test_step_moves_forward(self):
        game = SnakeGame(width=10, height=10, seed=1)
        old_head = game.snake[0]
        game.step()
        self.assertEqual(game.snake[0], (old_head[0] + 1, old_head[1]))
        self.assertEqual(len(game.snake), 3)

    def test_cannot_reverse_direction(self):
        game = SnakeGame(width=10, height=10, seed=1)
        game.change_direction(Direction.LEFT)
        game.step()
        self.assertEqual(game.direction, Direction.RIGHT)

    def test_eat_food_grows_snake_and_scores(self):
        game = SnakeGame(width=10, height=10, seed=1)
        head_x, head_y = game.snake[0]
        game.food = (head_x + 1, head_y)

        game.step()

        self.assertEqual(game.score, 1)
        self.assertEqual(len(game.snake), 4)
        self.assertNotIn(game.food, game.snake)

    def test_wall_collision_ends_game(self):
        game = SnakeGame(width=4, height=4, seed=1)
        game.snake = [(3, 2), (2, 2), (1, 2)]
        game.direction = Direction.RIGHT
        game.change_direction(Direction.RIGHT)
        game.step()
        self.assertTrue(game.game_over)

    def test_self_collision_ends_game(self):
        game = SnakeGame(width=8, height=8, seed=1)
        game.snake = [(3, 3), (4, 3), (4, 4), (3, 4), (2, 4), (2, 3)]
        game.direction = Direction.UP
        game.change_direction(Direction.RIGHT)
        game.step()
        self.assertTrue(game.game_over)

    def test_fill_last_cell_triggers_game_over(self):
        game = SnakeGame(width=4, height=4, seed=1)
        game.snake = [
            (1, 1),
            (0, 1),
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (3, 1),
            (2, 1),
            (2, 2),
            (3, 2),
            (3, 3),
            (2, 3),
            (1, 3),
            (0, 3),
            (0, 2),
        ]
        game.direction = Direction.DOWN
        game.change_direction(Direction.DOWN)
        game.food = (1, 2)

        game.step()

        self.assertEqual(game.score, 1)
        self.assertEqual(len(game.snake), 16)
        self.assertTrue(game.game_over)


if __name__ == "__main__":
    unittest.main()
