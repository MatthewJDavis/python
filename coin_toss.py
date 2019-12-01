import random

def coin_toss():
    """Simulate a random coin toss with the outcome being heads or tails"""
    if random.randrange(1, 3) == 1:
        return 'Heads'
    else:
        return 'Tails'


def most_in_a_row(item_list):
    """ Calculate the most times an item appears in a list contiguously"""
    highest_count = 0
    count = 0

    for item in item_list:
        if highest_count == 0:
            current_item = item

        if current_item == item:
            count += 1
            if count > highest_count:
                highest_count = count
        else:
            current_item = item
            count = 1
    return current_item, highest_count

if __name__ == '__main__':
    outcome = []
    for i in range (1000):
        outcome.append(coin_toss())
    print(outcome)
    print(most_in_a_row(outcome))
    print('Total Tails {}'.format(outcome.count('Tails')))
    print('Total Heads {}'.format(outcome.count('Heads')))


