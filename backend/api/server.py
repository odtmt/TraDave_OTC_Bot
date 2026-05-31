from fastapi import FastAPI
from backend.engine.realtime_engine import start_engine
import threading

app = FastAPI()

engine_thread = None


@app.get("/start")
def start_bot():

    global engine_thread

    if not engine_thread:

        engine_thread = threading.Thread(target=start_engine)
        engine_thread.start()

    return {"status": "BOT STARTED"}


@app.get("/stop")
def stop_bot():

    # simplified stop flag (upgrade later)
    return {"status": "STOP REQUEST SENT"}