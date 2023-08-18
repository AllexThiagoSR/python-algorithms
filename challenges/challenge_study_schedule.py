def study_schedule(permanence_period, target_time):
    if type(permanence_period) != list or type(target_time) != int:
        return None
    quantity = 0
    for period in permanence_period:
        if type(period[0]) != int or type(period[1]) != int:
            return None
        if period[0] <= target_time <= period[1]:
            quantity += 1
    return quantity


# permanence_period = [(2, 2), (4, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

# print(study_schedule(permanence_period, 2))
