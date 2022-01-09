import pygame
import random
import sys
import settings as s
import movement as m
import collision as c
import ballphysics as bp
import ai

# Initialize pygame
pygame.init()

# Create Window
WIN = pygame.display.set_mode((s.WIN_WIDTH, s.WIN_HEIGHT))

# Title
pygame.display.set_caption("Pong")

# Background
def backround(x, y):
    WIN.blit(s.BG, (x, y))


# Paddle
class paddle:
    def __init__(self):
        self.x = 700
        self.y = round(s.WIN_HEIGHT / 2) - s.PADDLE_HEIGHT
        self.paddleY_change = 0

    def update(self, x, y):
        pygame.draw.rect(WIN, (255, 255, 255), [x, y, s.PADDLE_WIDTH, s.PADDLE_HEIGHT])


# Initialize player and opponent
player = paddle()
opponent = paddle()
opponent.x = 100


# Ball
class gameball:
    def __init__(self):
        self.x = round(s.WIN_WIDTH / 2) - s.BALL_RADIUS
        self.y = round(s.WIN_HEIGHT / 2) + s.BALL_RADIUS
        self.ballX_change = s.BALL_SPEED
        self.ballY_change = 0

    def update(self, x, y):
        pygame.draw.circle(WIN, (255, 255, 255), (x, y), s.BALL_RADIUS)

    def startup():
        ball.x = round(s.WIN_WIDTH / 2) - s.BALL_RADIUS
        ball.y = round(s.WIN_HEIGHT / 2) + s.BALL_RADIUS
        ball.ballX_change = ball.ballX_change * random.choice(
            [s.RANDOM_BALL_STARTDIR, 1]
        )


# Score
class score:
    def __init__(self):
        self.x = 600
        self.y = 100
        self.score = 0
        self.FONT = pygame.font.Font("freesansbold.ttf", 32)

    def update(self):
        shown_score = self.FONT.render(str(self.score), True, (255, 255, 255))
        WIN.blit(shown_score, (self.x, self.y))


playerscore = score()
opponentscore = score()
opponentscore.x = 200


# Initialize ball
ball = gameball()

# Main loop
def main():
    # Variables
    endx = 1000
    endy = 0
    paddlecontacty = None
    paddlecontactx = None
    framecounter = 0

    run = True
    while run:
        # Set framerate
        s.CLOCK.tick(60)

        # Event controller
        for event in pygame.event.get():
            # Check quit
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            # Player movement
            if event.type == pygame.KEYDOWN:
                player.paddleY_change += m.movement(event.key)

            if event.type == pygame.KEYUP:
                player.paddleY_change = m.smoothmove(event.key, player.paddleY_change)

            # Restart
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    gameball.startup()
                    ball.ballX_change = s.BALL_SPEED

        # Move player
        player.y += player.paddleY_change
        player.y = m.oob(player.y)

        # Check ball and paddle collision
        if c.ball_paddle(ball.x, player.x, ball.y, player.y):
            angle = bp.get_angle_from_paddle(ball.y, player.y)
            endx, endy = bp.get_endpoints_paddle(ball.x, ball.y, angle)
            ball.ballX_change, ball.ballY_change = bp.get_x_and_y_vel(
                endx, endy, ball.x, ball.y
            )
            paddlecontacty = ball.y
            paddlecontactx = ball.x

        # Check if ball is touching the wall
        if c.ballwall(ball.y, ball.ballY_change):
            angle = bp.get_angle_from_wall(ball.x, ball.y, player.x, paddlecontacty)
            endx, endy = bp.get_endpoints_wall(ball.x, ball.y, angle, paddlecontactx)
            ball.ballX_change, ball.ballY_change = bp.get_x_and_y_vel(
                endx, endy, ball.x, ball.y
            )

        # Check if ball is out of bounds and restarts
        if c.balloob(ball.x):
            if framecounter == 0:
                if ball.x > s.WIN_WIDTH / 2:
                    opponentscore.score += 1
                else:
                    playerscore.score += 1

            ball.x = -900
            ball.y = s.WIN_HEIGHT / 2
            framecounter += 1
            ball.ballX_change = 0
            if framecounter == 60:
                framecounter = 0
                ball.ballX_change = s.BALL_SPEED
                ball.ballY_change = 0
                gameball.startup()

        # Check if ball touching opponennt
        if c.ball_opponent(ball.x, ball.y, opponent.x, opponent.y):
            angle = bp.get_angle_from_paddle(ball.y, opponent.y)
            endx, endy = bp.get_endpoints_paddle(ball.x, ball.y, angle)
            ball.ballX_change, ball.ballY_change = bp.get_x_and_y_vel(
                endx, endy, ball.x, ball.y
            )
            paddlecontacty = ball.y
            paddlecontactx = ball.x

        # Move opponent
        upordown = ai.upordown(ball.x, ball.y, opponent.y, ball.ballY_change)
        opponent.paddleY_change = s.PADDLE_SPEED * upordown

        # Move ball
        ball.x += ball.ballX_change
        ball.y += ball.ballY_change

        # Move oppenent
        opponent.y += opponent.paddleY_change
        opponent.y = m.oob(opponent.y)

        # Draw
        backround(0, 0)
        player.update(player.x, player.y)
        playerscore.update()
        opponent.update(opponent.x, opponent.y)
        opponentscore.update()
        ball.update(ball.x, ball.y)
        pygame.display.flip()


if __name__ == "__main__":
    main()
