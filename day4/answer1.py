with open('day4\\input.txt', 'r') as f:
    data = [line.strip() for line in f]
    numbers = data[0]
    cards = data[1:]
    

def get_cards(card_list: list) -> dict[list]:
    counter = 0
    bingo_cards = {}

    for line in card_list:
        if line == '':
            counter += 1
            print(f'Creating Bingo Card {counter}')
            bingo_cards[counter] = []
        else:
            print(line)
            bingo_cards[counter] += [line]
    return bingo_cards

bingo_cards = get_cards(cards)
print(bingo_cards)
print(f'Bingo Numbers: {numbers}')


def get_winner(bingo_cards: list, bingo_numbers) -> int:
    for num in bingo_numbers:
        for card in bingo_cards:
            for row in card:
                if num in row:
                    pass
                    # mark num
                    # triple nested loop omegalul
    answer = 0 # answer is sum of all UNMARKED numbers on the winning board.
    return answer

answer = get_winner(bingo_cards, numbers)
print(f'Answer: {answer}')