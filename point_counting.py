import numpy as np
from itertools import chain, combinations

def point_check(hand: list, cut_card: list = [{"title": "Blank", "suit": "Blank", "color": "White", "value": 100, "order_value": 100}], crib: bool = False) -> int:
    total_points = 0
    run_multiplier = 1

    hand_w_cut = hand + cut_card

    print(f"The following hand is:")
    for card in hand_w_cut:
        print(card['suit'] + " " + card['title'])

    # Card face value
    values = [card['value'] for card in hand_w_cut]
    values.sort()

    # Card order value
    order_values = [card['order_value'] for card in hand_w_cut]
    order_values.sort()
    order_values_set = list(sorted(set(order_values)))

    # Getting points for pairs
    pairs = [order_values.count(num) for num in order_values_set]
    total_points += sum([num*(num-1) for num in pairs])

    print(f"Points after pairs: {total_points}")

    # Getting points for runs - rigged in a way to work for all 5-card hands: only keeps track on the highest run in a hand
    ordered_differences = np.array([order_values_set[i+1] - order_values_set[i] for i in range(len(order_values_set)) if i < len(order_values_set) - 1])
    runs = np.split(ordered_differences, np.where(ordered_differences > 1)[0])
    counter = max([sum(run==1) for run in runs]) + 1

    # Checking for double runs, triple runs, double-double runs, etc
    just_added = False
    for i in range(len(ordered_differences)):
        if ordered_differences[i] == 1:
            if order_values.count(order_values_set[i]) > 1 and not just_added:
                run_multiplier *= order_values.count(order_values_set[i])
            elif just_added:
                just_added = False
            if order_values.count(order_values_set[i+1]) > 1:
                run_multiplier *= order_values.count(order_values_set[i+1])
                just_added = True
    total_points += counter*run_multiplier if counter > 2 else 0

    print(f"Points after runs: {total_points}")

    # Getting points for 15s
    s = list(values)
    powerset = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    total_points += sum([2 for group in powerset if sum(group) == 15])

    print(f"Points after fifteens: {total_points}")

    # Getting points for a flush
    if len(set([card["suit"] for card in hand])) == 1 and hand[0]["suit"] == cut_card[0]["suit"]:
        total_points += 5
    elif len(set([card["suit"] for card in hand])) == 1 and not crib:
        total_points += 4

    print(f"Points after flushes: {total_points}")

    return total_points

def point_check_pegging(pile: list, previous_run_points: int):
    total_points = 0
    run_multiplier = 1

    print(f"The pile so far is:")
    for card in pile:
        print(card['suit'] + " " + card['title'])

    # Card face value
    values = [card['value'] for card in pile]
    values.sort()

    # Card order value
    order_values = [card['order_value'] for card in pile]
    order_values = order_values[::-1]

    # Getting points for pairs on top of the pile
    counter = 1
    while order_values[0] - order_values[counter] == 0:
        counter += 1
        if counter == len(order_values):
            break

    total_points += counter*(counter-1)
    print(f"counter: {counter}")
    print(f"Points after pairs: {total_points}")

    # Getting points for runs
    run_points = 0
    new_prev_points = 0
    length = 0

    diffs = []
    for j in range(3, len(order_values)+1):
        bunch = sorted(order_values[:j])
        print(f"Bunch {bunch}")
        diffs.append(list(np.array([bunch[i+1] - bunch[i] for i in range(j-1)])))
        print(diffs)

    for diff in diffs:
        #print(diff)
        if max(diff) == 1 and sum(diff) >= 2:# and sum(diff) > run_points - 1:#diff.count(1) > diff.count(0):
            length = len(diff)
            run_points = sum(diff) + 1

    if run_points:
        #print(order_values[:length+1])
        for num in list(set(order_values[:length+1])):
            if order_values[:length+1].count(num) > 1:
                run_multiplier *= order_values[:length+1].count(num)
    print(f"Run mult: {run_multiplier}")
    # Annoying that I have to fix it for triple runs but alas
    if run_multiplier > 1:
        run_points = run_multiplier*run_points + run_multiplier if run_multiplier != 3 else 15
        print(f"RUN POINTS {run_points}")
        new_prev_points = run_points
        # Then take off the points from the previously counted pairs:
        run_points -= counter*(counter-1)
    else:
        new_prev_points = run_points
    # For now this works ok but I wonder if as the last card moves out and an attempt to add onto the run of the remaining
    # 4 cards will cause this to have issues...
    total_points += run_points if run_points > previous_run_points else 0 

    print(f"Points after runs: {total_points}")

    # Getting points for reaching 15 or 31
    if sum([card["value"] for card in pile]) == 15:
        total_points += 2
    elif sum([card["value"] for card in pile]) == 31:
        total_points += 1

    print(f"Total Points: {total_points}")

    return total_points, new_prev_points