import random

def ai_select(servers):
    best = None
    best_score = float('inf')
    for s in servers:
        load = s.get_load()
        prediction = load + random.randint(0,10)
        score = 0.7*load + 0.3*prediction
        if score < best_score:
            best_score = score
            best = s
    return best

def normal_select(servers):
    return servers[0]  # always pick first (bad strategy)
