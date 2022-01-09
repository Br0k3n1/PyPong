import pygame

# Window settings
WIN_WIDTH = 800
WIN_HEIGHT = 600

# Background settings
BG = pygame.image.load("Imgs/pongbg.png")

# Clock settings
CLOCK = pygame.time.Clock()

# Paddle settings
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 85
PADDLE_SPEED = 6

# Ball settings
BALL_RADIUS = 7
BALL_SPEED = 7
OFF_PADDLE_SPEED = 11

# Miscellaneous settings
RANDOM_BALL_STARTDIR = -1  # -1 = True and 1 = False
MAX_ANGLE = 70
MIN_ANGLE = 30
