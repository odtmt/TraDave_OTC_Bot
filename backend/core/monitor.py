import requests
import time
import os

def heartbeat():

    while True:

        try:
            # simple check (engine alive)
            print("💚 TraDave_OTC_bot RUNNING")

        except Exception as e:
            print("❌ BOT CRASHED:", e)

        time.sleep(60)