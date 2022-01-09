import settings as s
import main as m


# Calculate if ball hit paddle
def ball_paddle(ballx, playerx, bally, playery):
    if ballx >= playerx and ballx < playerx + s.PADDLE_WIDTH:
        if bally >= playery and bally <= playery + s.PADDLE_HEIGHT:
            return True
        else:
            return False
    else:
        return False


# Calculate if ball is out of bounce
def balloob(ballx):
    if ballx >= s.WIN_WIDTH - s.BALL_RADIUS * 2:
        return True

    if ballx - s.BALL_RADIUS * 2 <= 0:
        return True
    else:
        return False


def ballwall(bally, ychange):
    if bally + ychange <= 0 or bally + ychange >= s.WIN_HEIGHT:
        return True
    else:
        return False


def ball_opponent(ballx, bally, oppenentx, oppoenenty):
    if ballx - s.BALL_RADIUS <= oppenentx + s.PADDLE_WIDTH and ballx > oppenentx:
        if bally >= oppoenenty and bally <= oppoenenty + s.PADDLE_HEIGHT:
            return True
        else:
            return False
    else:
        return False
