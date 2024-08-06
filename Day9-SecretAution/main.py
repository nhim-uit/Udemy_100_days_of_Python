# Udemy: Master Python by building 100 projects in 100 days
# Aug 06, 2024
# Day 9 - Secret Auction
def highest_bidder(record):
    highest_bid = 0
    winner = ''

    for k, v in record.items():
        if v > highest_bid:
            highest_bid = v
            winner = k

    print(f'The winner is {winner} with a bid of ${highest_bid}.')


def starter():
    name = input('What is your name? ')
    price = int(input('What is your bid? $'))
    return name, price


if __name__ == '__main__':
    end = 'yes'
    bids = {}

    while end == 'yes':
        name, price = starter()
        bids.update({name: price})
        end = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    highest_bidder(bids)


