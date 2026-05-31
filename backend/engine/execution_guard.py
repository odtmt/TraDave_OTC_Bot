# backend/engine/execution_guard.py

executed_pairs = {}


def can_execute(pair):

    if pair in executed_pairs:
        return False

    executed_pairs[pair] = True
    return True


def reset_guards():
    global executed_pairs
    executed_pairs = {}