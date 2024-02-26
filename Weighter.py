def weighter(edge: dict, weights: dict) -> dict: 
    """
    weights of format:
    {
        "lift": float,
        "novice": float,
        "easy": float,
        "intermediate": float,
        "advanced": float
    }
    returns the node weight as float
    """
    weight = 1 # default weight
    weight = weights.get(edge.get("difficulty"))
    weight = edge.get("duration") * edge.get("distance_prop") * weight

    return weight