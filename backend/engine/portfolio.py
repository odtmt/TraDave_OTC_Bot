bots = {
    "OTC_MAIN": True,
    "OTC_SCALPER": True,
    "OTC_RECOVERY": False
}


def get_active_bots():

    return [b for b, active in bots.items() if active]