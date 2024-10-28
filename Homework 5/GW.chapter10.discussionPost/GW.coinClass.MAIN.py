from GWcoinClass import Coin

def main():
    # create two instances of the coin class:
    coin1 = Coin()
    coin2 = Coin()

    #  innitialize the same side to zero
    same_side = 0
    head_count = 0
    tails_count = 0
    
    # toss each coin 100 times
    for count in range(100):
        coin1.toss()
        coin2.toss()

        if coin1.get_sideup() == 'Heads' and coin2.get_sideup() == 'Heads':
            head_count += 1
            same_side += 1

        elif coin1.get_sideup() == 'Tails' and coin2.get_sideup() == 'Tails':
            tails_count += 1
            same_side += 1

    print(f'The coins landed on the same side a total of {same_side} times. ')
    print(f'The coins landed on heads {head_count} times. ')
    print(f'The coins landed on tails {tails_count} times. ')

if __name__ == '__main__':
    main()
