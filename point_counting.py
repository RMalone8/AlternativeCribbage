import numpy as np
from itertools import chain, combinations

def point_check(hand: list, is_crib: bool = False) -> int:
    '''
    Expects a hand to be counted and the cut card is assumed to be the last card
    in the hand (Only really impacts the flush with the crib)
    '''
    total_points = 0
    run_multiplier = 1

    #print(f"The following hand is:")
    #for card in hand:
        #print(card['suit'] + " " + card['title'])

    # Card face value
    values = [card['value'] for card in hand]
    values.sort()

    # Card order value
    order_values = [card['order_value'] for card in hand]
    order_values.sort()
    order_values_set = list(sorted(set(order_values)))

    # Getting points for pairs
    pairs = [order_values.count(num) for num in order_values_set]
    total_points += sum([num*(num-1) for num in pairs])

    #print(f"Points after pairs: {total_points}")

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

    #print(f"Points after runs: {total_points}")

    # Getting points for 15s
    s = list(values)
    powerset = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    total_points += sum([2 for group in powerset if sum(group) == 15])

    #print(f"Points after fifteens: {total_points}")

    # Getting points for a flush
    if len(set([card["suit"] for card in hand])) == 1:
        total_points += 5
    elif len(set([card["suit"] for card in hand[:4]])) == 1 and not is_crib:
        total_points += 4

    #print(f"Points after flushes: {total_points}")

    return total_points

def point_check_pegging(pile: list):
    total_points = 0
    run_multiplier = 1
    pair_points = False

    #print(f"The pile so far is:")
    #for card in pile:
        #print(card['suit'] + " " + card['title'])

    # Card order value
    order_values = [card['order_value'] for card in pile]
    order_values = order_values[::-1]

    # Getting points for pairs on top of the pile
    if len(pile) > 1:
        counter = 1
        while order_values[0] - order_values[counter] == 0:
            counter += 1
            if counter == len(order_values):
                break
        if counter > 1:
            pair_points = True
        total_points += counter*(counter-1)
        #print(f"counter: {counter}")
    #print(f"Points after pairs: {total_points}")

    # Getting points for runs
    run_points = 0
    run_points_pairs = 0

    diffs = []
    # going through combinations of the first three cards and then beyond to see if we have any runs
    for j in range(3, len(order_values)+1):
        # each clump of cards must be sorted from the original pile order
        bunch = sorted(order_values[:j])
        #print(f"Bunch {bunch}")
        diffs.append(list(np.array([bunch[i+1] - bunch[i] for i in range(j-1)])))
        #print(diffs)

    for diff in diffs:
        # recording the longest run into run_points, which is when
        # the biggest difference between any given card is 1 and the
        # number of unique cards is at least 3
        if max(diff) == 1 and sum(diff) >= 2:
            length = len(diff)
            run_points = sum(diff) + 1
    if run_points:
        for num in list(set(order_values[:length+1])):
            if order_values[:length+1].count(num) > 1:
                run_points_pairs += order_values[:length+1].count(num)*(order_values[:length+1].count(num)-1)
                run_multiplier *= order_values[:length+1].count(num)
        # We counted points for the pair earlier, but since it's a part of the run
        # we must take it off of our total points
        if pair_points:
            #print(f"Taking off the pair points of: {counter*(1-counter)}")
            total_points -= counter*(counter-1)
    total_points += run_multiplier*run_points
    total_points += run_points_pairs

    #print(f"Run Points: {run_points}")
    #print(f"Run Multiplier: {run_multiplier}")
    #print(f"Run Pair Points: {run_points_pairs}")

    # Getting points for a flush (looking at the top and then moving down)
    flush_count = 1
    if len(pile) >= 4:
        suits = [card["suit"] for card in pile][::-1]
        top_suit = suits[0]
        while top_suit == suits[flush_count]:
            flush_count += 1
            if flush_count >= len(pile):
                break
        #print(flush_count)
        total_points += flush_count if flush_count >= 4 else 0
        
    #print(f"Total points after flush: {total_points}")

    # Getting points for reaching 15 or 31
    if sum([card["value"] for card in pile]) == 15:
        total_points += 2
    elif sum([card["value"] for card in pile]) == 31:
        total_points += 1

    #print(f"Total Points: {total_points}")

    return total_points
