import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

GRAVITY = 1
JUMP_STRENGTH = 5.7
PILLAR_GAP = 120
PILLAR_WIDTH = 50
PILLAR_SPEED = 2
FPS = 30


class Game:
    def __init__(self):
        """Initializes the game variables."""
        self.bird_y = HEIGHT // 2
        self.bird_velocity = 0
        self.running = True
        self.status_code = 0
        self.pillar_x = WIDTH
        self.pillar_top = random.randint(50, HEIGHT - PILLAR_GAP - 50)
        self.pillar_bottom = self.pillar_top + PILLAR_GAP

        self.window_open = False

    def show(self):
        """Opens the game window."""
        global screen
        if not self.window_open:
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Flappy Bird Clone")
            self.window_open = True

    def close(self):
        """Hides the game window."""
        self.window_open = False

    def quitGame(self):
        """Quits the entire game."""
        pygame.display.quit()
        self.window_open = False

    def jump(self):
        """Makes the bird jump by setting an upward velocity."""
        if self.running:
            self.bird_velocity = -JUMP_STRENGTH

    def update(self):
        """Updates the bird's position and pillar movement."""
        if not self.running:
            return

        self.bird_velocity += GRAVITY
        self.bird_y += self.bird_velocity
        self.pillar_x -= PILLAR_SPEED

        if self.bird_y > HEIGHT or self.bird_y < 0:
            self.running = False
            self.status_code = -1

        if 85 < self.pillar_x < 115:
            if self.bird_y < self.pillar_top or self.bird_y > self.pillar_bottom:
                self.running = False
                self.status_code = -2

        if self.pillar_x < -PILLAR_WIDTH:
            self.pillar_x = WIDTH
            self.pillar_top = random.randint(50, HEIGHT - PILLAR_GAP - 50)
            self.pillar_bottom = self.pillar_top + PILLAR_GAP

    def getDetails(self):
        """Returns the game state."""
        if not self.running:
            return self.status_code
        return [self.bird_y, self.pillar_top, self.pillar_bottom, self.pillar_x]

    def draw(self):
        """Draws the game elements onto the screen."""
        if not self.window_open:
            return
        
        screen.fill(WHITE)
        pygame.draw.circle(screen, BLUE, (100, int(self.bird_y)), 15)
        pygame.draw.rect(screen, GREEN, (self.pillar_x, 0, PILLAR_WIDTH, self.pillar_top))
        pygame.draw.rect(screen, GREEN, (self.pillar_x, self.pillar_bottom, PILLAR_WIDTH, HEIGHT - self.pillar_bottom))

        if not self.running:
            font = pygame.font.SysFont(None, 50)
            text = font.render("Game Over", True, RED)
            screen.blit(text, (WIDTH // 3, HEIGHT // 2))

        pygame.display.update()


if __name__ == "__main__":
    """Runs the game externally in a loop for testing."""
    game = Game()
    clock = pygame.time.Clock()
    game.show()

    for _ in range(500):
        time.sleep(0.0003)

        if _ % 25 == 0:
            game.jump()

        game.update()
        print(game.getDetails())

        if game.status_code in [-1, -2]:
            break

        game.draw()
        clock.tick(FPS)

    game.close()
    pygame.quit()