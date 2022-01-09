import pygame
import settings as s


# Move paddle depending on key press
def movement(key):
    if key == pygame.K_UP or key == pygame.K_w:
        return -s.PADDLE_SPEED
    if key == pygame.K_DOWN or key == pygame.K_s:
        return s.PADDLE_SPEED
    else:
        return 0


# Fix bug in which movemnt is jittery if pressing multiple movement buttons
def smoothmove(key, playerY_change):
    if playerY_change < 0:
        if key == pygame.K_UP or key == pygame.K_w:
            return 0
        else:
            return playerY_change
    if playerY_change > 0:
        if key == pygame.K_DOWN or key == pygame.K_s:
            return 0
        else:
            return playerY_change
    else:
        return playerY_change


# Check if player is going out of bounce and prevent it
def oob(playerY):
    if playerY <= 0:
        return 0
    elif playerY >= s.WIN_HEIGHT - s.PADDLE_HEIGHT:
        return s.WIN_HEIGHT - s.PADDLE_HEIGHT
    else:
        return playerY
