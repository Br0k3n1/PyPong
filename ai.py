import settings as s


def upordown(ballx, bally, opponenty, ballychange):
    if ballx > s.WIN_WIDTH / 2:
        if ballychange > 0 and bally > opponenty + s.PADDLE_HEIGHT / 2:
            return 0
        if ballychange < 0 and bally < opponenty + s.PADDLE_HEIGHT / 2:
            return 0
        if ballychange < 0 and bally > opponenty + s.PADDLE_HEIGHT / 2:
            return -1
        if ballychange > 0 and bally < opponenty + s.PADDLE_HEIGHT / 2:
            return 1

    if ballychange == 0 and opponenty < bally and opponenty + s.PADDLE_HEIGHT > bally:
        return 0

    if bally > opponenty + s.PADDLE_HEIGHT / 2:
        return 1
    else:
        return -1
