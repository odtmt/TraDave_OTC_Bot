# backend/core/time_utils.py

from datetime import datetime, timezone


def get_entry_time():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def get_timestamp():
    return datetime.now(timezone.utc).timestamp()