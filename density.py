def classify_density(person_count, lower_threshold=20, upper_threshold=120):
    if person_count < lower_threshold:
        return "Undercrowded"
    elif person_count > upper_threshold:
        return "Overcrowded"
    else:
        return "Moderate"
