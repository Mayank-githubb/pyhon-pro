import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen size
width = 500
height = 500
screen = pygame.display.set_mode((width, height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Clock for frame rate control
clock = pygame.time.Clock()
class Snake:
    def __init__(self):
        self.size = 10
        self.x = width // 2
        self.y = height // 2
        self.x_change = 0
        self.y_change = 0
        self.snake_body = [(self.x, self.y)]

    def move(self):
        # Update head position
        self.x += self.x_change
        self.y += self.y_change

        # Check for edge collisions (game over)
        if self.x < 0 or self.x >= width or self.y < 0 or self.y >= height:
            return False

        # Check for body collisions (game over)
        for body_part in self.snake_body[1:]:
            if self.x == body_part[0] and self.y == body_part[1]:
                return False

        # Update snake body (except head)
        self.snake_body[:-1] = self.snake_body[1:]
        self.snake_body.append((self.x, self.y))

        # Return True to continue game
        return True

    def draw(self, screen):
        for x, y in self.snake_body:
            pygame.draw.rect(screen, green, [x, y, self.size, self.size])
def generate_food():
    # Randomly place food within screen boundaries
    x = round(random.randrange(0, width - food_size) / 10.0) * 10.0
    y = round(random.randrange(0, height - food_size) / 10.0) * 10.0
    return x, y

def game_loop():
    game_over = False
    snake = Snake()
    food_size = 10
    food_x, food_y = generate_food()

    # Main game loop
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            # Handle key presses for direction change

        # Check for food collision and grow snake
        if snake.x == food_x and snake.y == food_y:
            food_x, food_y = generate_food()
            snake.snake_body.append((snake.x, snake.y))

        # Update game objects
        game_over = not snake.move()

        # Clear screen and redraw elements
        screen.fill(black)
        pygame.draw.rect(screen, red, [food_x, food_y, food_size, food_size])
        snake.draw(screen)
        pygame.display.update()

        # Set game speed (adjust clock tick value)
        clock.tick(60)

# Quit Pygame and exit
pygame.quit()
