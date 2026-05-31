daily_pnl = 0
loss_streak = 0

def update(result):
    global daily_pnl, loss_streak

    if result > 0:
        daily_pnl += 1
        loss_streak = 0
    else:
        daily_pnl -= 1
        loss_streak += 1


def can_trade():

    if daily_pnl <= -20:
        return False

    if loss_streak >= 3:
        return False

    return True