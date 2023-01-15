import random

RESULTS = ["大吉", "吉", "凶", "大凶"]

def cmd():
    result = random.choice(RESULTS)
    print(f"本日の運勢は... {result}")
