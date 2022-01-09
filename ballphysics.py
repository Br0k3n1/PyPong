import math
import settings as s


# Calculate angle off of paddle
def get_angle_from_paddle(bally, playery):

    # Calculate distance from middle of paddle
    paddle_center = playery + round(s.PADDLE_HEIGHT / 2)
    d = paddle_center - (bally)
    smalld = round(d / (s.PADDLE_HEIGHT / 2), 2)

    # Calculate direction
    if smalld >= 0:
        dir = 1
        d = smalld
    else:
        dir = -1
        d = smalld * dir

    # Calculate angle
    if d == 0:
        angle = 0
    else:
        angle = round(s.MAX_ANGLE * (1 - d))

    # Limit angle from getting to small
    if angle < s.MIN_ANGLE:
        angle = s.MIN_ANGLE

    # More leniency against determing if the ball hit the middle of the paddle
    if angle > s.MAX_ANGLE - 10 and angle <= s.MAX_ANGLE:
        angle = 0
    if angle < -s.MAX_ANGLE and angle > s.MAX_ANGLE - 10:
        angle = 0

    # Correct angle deppending on direction
    angle = angle * dir
    return angle


# Calulcate endpoints off of paddle
def get_endpoints_paddle(ballx, bally, angle):

    # Calculate direction
    if angle >= 0:
        dir = 1
    else:
        dir = -1

    # Calculate adjacent
    if dir == 1:
        adjacent = bally
    if dir == -1:
        adjacent = s.WIN_HEIGHT - bally

    # Caluclate opposite
    if ballx < s.WIN_WIDTH / 2:
        opposite = round(math.tan(angle * math.pi / 180) * adjacent)
    else:
        opposite = round(math.tan(angle * math.pi / 180) * adjacent) * dir

    # Calculate endpoints
    if angle == 0:
        if ballx < s.WIN_WIDTH / 2:
            endpointx = s.WIN_WIDTH
            endpointy = bally
        else:
            endpointx = 0
            endpointy = bally
    else:
        endpointx = ballx - opposite

        if dir == 1:
            endpointy = 0
        else:
            endpointy = s.WIN_HEIGHT

    if endpointx < 0:
        endpointx = 200

    return endpointx, endpointy


# Determines x and y velocity
def get_x_and_y_vel(endx, endy, ballx, bally):
    xvel = endx - ballx
    yvel = endy - bally

    if xvel >= 0:
        xdir = 1
    else:
        xdir = -1
    if yvel >= 0:
        ydir = 1
    else:
        ydir = -1

    # Lowers x and y velocity
    if yvel == 0:
        xvel = xvel / (xvel / s.OFF_PADDLE_SPEED) * xdir
    else:
        xvel = xvel / (yvel / s.OFF_PADDLE_SPEED) * ydir
        yvel = yvel / (yvel / s.OFF_PADDLE_SPEED) * ydir

    if yvel >= 10:
        yvel -= yvel - 7
        xvel -= yvel - 7
    if yvel <= -10:
        yvel += yvel * -1 - 7
        xvel += yvel * -1 - 7

    if xvel >= 15:
        xvel -= xvel - 10
        yvel -= xvel - 10
    if xvel <= -15:
        xvel += xvel * -1 - 10
        yvel += xvel * -1 - 10

    return xvel, yvel


def get_angle_from_wall(ballx, bally, playerx, paddlecontact):
    adjacent = playerx - ballx

    if bally < 50:
        opposite = 600 - paddlecontact
    else:
        opposite = 0 - paddlecontact

    angle = math.tanh(opposite / adjacent)
    return angle


def get_endpoints_wall(ballx, bally, angle, paddlecontactx):
    opposite = ballx

    adjacent = opposite / math.tan(angle)

    if paddlecontactx < s.WIN_WIDTH / 2:
        endx = s.WIN_WIDTH
    if paddlecontactx >= s.WIN_WIDTH / 2:
        endx = 0

    endy = bally + adjacent

    return endx, endy
