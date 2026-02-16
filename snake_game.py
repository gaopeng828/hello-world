from __future__ import annotations

import random
import tkinter as tk
from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple


Coordinate = Tuple[int, int]


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    @property
    def vector(self) -> Coordinate:
        return self.value


OPPOSITE_DIRECTION = {
    Direction.UP: Direction.DOWN,
    Direction.DOWN: Direction.UP,
    Direction.LEFT: Direction.RIGHT,
    Direction.RIGHT: Direction.LEFT,
}


@dataclass
class GameConfig:
    width: int = 20
    height: int = 20
    cell_size: int = 20
    tick_ms: int = 140


@dataclass
class Particle:
    x: float
    y: float
    vx: float
    vy: float
    life: int
    max_life: int
    radius: float
    color: str


class SnakeGame:
    def __init__(self, width: int = 20, height: int = 20, seed: int | None = None):
        if width < 4 or height < 4:
            raise ValueError("Board size must be at least 4x4")

        self.width = width
        self.height = height
        self._random = random.Random(seed)
        self.score = 0
        self.game_over = False

        cx = width // 2
        cy = height // 2
        self.snake: List[Coordinate] = [(cx, cy), (cx - 1, cy), (cx - 2, cy)]
        self.direction = Direction.RIGHT
        self._next_direction = self.direction
        self.food = self._spawn_food()

    def change_direction(self, new_direction: Direction) -> None:
        if self.game_over:
            return
        if new_direction == OPPOSITE_DIRECTION[self.direction]:
            return
        self._next_direction = new_direction

    def step(self) -> None:
        if self.game_over:
            return

        self.direction = self._next_direction
        dx, dy = self.direction.vector
        head_x, head_y = self.snake[0]
        new_head = (head_x + dx, head_y + dy)

        if self._hits_wall(new_head):
            self.game_over = True
            return

        grow = new_head == self.food
        body_to_check = self.snake if grow else self.snake[:-1]
        if new_head in body_to_check:
            self.game_over = True
            return

        self.snake.insert(0, new_head)
        if grow:
            self.score += 1
            self.food = self._spawn_food()
        else:
            self.snake.pop()

    def _hits_wall(self, position: Coordinate) -> bool:
        x, y = position
        return x < 0 or x >= self.width or y < 0 or y >= self.height

    def _spawn_food(self) -> Coordinate:
        free_cells = [
            (x, y)
            for x in range(self.width)
            for y in range(self.height)
            if (x, y) not in self.snake
        ]
        if not free_cells:
            self.game_over = True
            return self.snake[0]
        return self._random.choice(free_cells)


class SnakeApp:
    def __init__(self, config: GameConfig):
        self.config = config
        self.game = SnakeGame(width=config.width, height=config.height)
        self._random = random.Random()
        self.particles: List[Particle] = []

        self.root = tk.Tk()
        self.root.title("Snake")

        self.canvas = tk.Canvas(
            self.root,
            width=config.width * config.cell_size,
            height=config.height * config.cell_size,
            bg="#111111",
            highlightthickness=0,
        )
        self.canvas.pack(padx=8, pady=8)

        self.status_var = tk.StringVar()
        self.status_label = tk.Label(self.root, textvariable=self.status_var)
        self.status_label.pack(pady=(0, 8))

        self.root.bind("<Up>", lambda _e: self.game.change_direction(Direction.UP))
        self.root.bind("<Down>", lambda _e: self.game.change_direction(Direction.DOWN))
        self.root.bind("<Left>", lambda _e: self.game.change_direction(Direction.LEFT))
        self.root.bind("<Right>", lambda _e: self.game.change_direction(Direction.RIGHT))
        self.root.bind("r", lambda _e: self._restart())

    def _restart(self) -> None:
        self.game = SnakeGame(width=self.config.width, height=self.config.height)
        self.particles.clear()

    def _draw_cell(self, x: int, y: int, color: str) -> None:
        size = self.config.cell_size
        x1, y1 = x * size, y * size
        x2, y2 = x1 + size, y1 + size
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#222222")

    def _cell_center(self, x: int, y: int) -> Tuple[float, float]:
        size = self.config.cell_size
        return (x * size + size / 2, y * size + size / 2)

    def _spawn_burst(self, x: float, y: float, count: int, speed: float, colors: List[str]) -> None:
        for _ in range(count):
            magnitude = speed * (0.4 + self._random.random())
            vx = magnitude * (self._random.random() * 2 - 1) * 0.9
            vy = magnitude * (self._random.random() * 2 - 1) * 0.9
            life = self._random.randint(8, 16)
            self.particles.append(
                Particle(
                    x=x,
                    y=y,
                    vx=vx,
                    vy=vy,
                    life=life,
                    max_life=life,
                    radius=self._random.uniform(1.5, 3.8),
                    color=self._random.choice(colors),
                )
            )

    def _update_particles(self) -> None:
        alive: List[Particle] = []
        for particle in self.particles:
            particle.x += particle.vx
            particle.y += particle.vy
            particle.vx *= 0.96
            particle.vy = particle.vy * 0.96 + 0.08
            particle.life -= 1
            if particle.life > 0:
                alive.append(particle)
        self.particles = alive

    def _draw_particles(self) -> None:
        for particle in self.particles:
            ratio = particle.life / particle.max_life
            radius = max(0.8, particle.radius * ratio)
            self.canvas.create_oval(
                particle.x - radius,
                particle.y - radius,
                particle.x + radius,
                particle.y + radius,
                fill=particle.color,
                outline="",
            )

    def _render(self) -> None:
        self.canvas.delete("all")
        fx, fy = self.game.food
        self._draw_cell(fx, fy, "#e63946")

        for index, (x, y) in enumerate(self.game.snake):
            color = "#52b788" if index else "#74c69d"
            self._draw_cell(x, y, color)

        self._draw_particles()

        if self.game.game_over:
            self.status_var.set(f"Game Over | Score: {self.game.score} | Press R to restart")
        else:
            self.status_var.set(f"Score: {self.game.score} | Arrows to move | R to restart")

    def _tick(self) -> None:
        prev_score = self.game.score
        prev_food = self.game.food
        was_game_over = self.game.game_over
        self.game.step()
        if self.game.score > prev_score:
            bx, by = self._cell_center(prev_food[0], prev_food[1])
            self._spawn_burst(bx, by, count=16, speed=2.5, colors=["#ffd166", "#ff9f1c", "#e63946"])
        if not was_game_over and self.game.game_over:
            head_x, head_y = self.game.snake[0]
            bx, by = self._cell_center(head_x, head_y)
            self._spawn_burst(bx, by, count=34, speed=3.4, colors=["#ff595e", "#ffca3a", "#8ac926"])
        self._update_particles()
        self._render()
        self.root.after(self.config.tick_ms, self._tick)

    def run(self) -> None:
        self._render()
        self.root.after(self.config.tick_ms, self._tick)
        self.root.mainloop()


def main() -> None:
    app = SnakeApp(GameConfig())
    app.run()


if __name__ == "__main__":
    main()
