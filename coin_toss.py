import random
import sys

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
    return highest_count


    
def most_one_side_in_a_row(item_list):
    """ Calculate the most times each side appears in a list contiguously"""
    heads_count = 0
    tails_count = 0
    max_heads_count = 0
    max_tails_count = 0
    current_item = ''
    count = 0
    for item in item_list:
        current_item = item
        count += 1
        if current_item == 'Heads':
            heads_count += count
            if heads_count > max_heads_count:
                max_heads_count = heads_count
                tails_count = 0
                count = 0
            count = 0
            tails_count = 0
        else:
            tails_count += count
            if tails_count > max_tails_count:
                max_tails_count = tails_count
                heads_count = 0
                count = 0
            count = 0
            heads_count = 0

    return max_heads_count, max_tails_count

def main():
    outcome = []
    if len(sys.argv) > 1:
        number_to_toss = sys.argv[1]
    else:
        number_to_toss = 10
    for i in range (int(number_to_toss)):
        outcome.append(coin_toss())
    print(outcome)  
    print('Coin was tossed {} times'.format(len(outcome)))
    print('Highest in a row: {} '.format(most_in_a_row(outcome)))
    print('Total Tails {}'.format(outcome.count('Tails')))
    print('Total Heads {}'.format(outcome.count('Heads')))
    a = most_one_side_in_a_row(outcome)
    print('Most Heads in a row: {}\nMost Tails in a row: {} '.format(a[0], a[1]))

if __name__ == '__main__':
    main()